import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (TimeoutException, NoSuchElementException, StaleElementReferenceException,
                                        WebDriverException)
from constants import artist_tracks


def fetch_play_count(artist_name, track_urls):
    options = Options()
    options.add_argument("user-data-dir=/home/mrsepiol/.config/google-chrome/Default")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    total_play_count = 0
    track_play_counts = []  # To store play counts for individual tracks

    print(f"Fetching play counts for {artist_name}...")

    for i in range(0, len(track_urls), 2):
        urls_batch = track_urls[i:i + 2]

        # Open new tabs and navigate to the URLs
        for idx, url in enumerate(urls_batch):
            while True:
                try:
                    if idx == 0:
                        driver.get(url)
                    else:
                        driver.execute_script(f"window.open('{url}', '_blank');")
                    break
                except WebDriverException as e:
                    if 'ERR_INTERNET_DISCONNECTED' in str(e):
                        print(f"Internet disconnected. Retrying to open URL: {url}...")
                        time.sleep(15)
                    else:
                        raise

        # Wait for all tabs to load
        retries = 0
        while retries < 3:
            try:
                for idx in range(len(urls_batch)):
                    driver.switch_to.window(driver.window_handles[idx])

                    # Wait until the title element is present
                    track_name_element = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.TAG_NAME, 'title')))

                    # Wait until the play count element is present
                    play_count_element = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="playcount"]')))

                # If all elements are found, break out of retry loop
                break
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
                print(f"Error loading page for batch starting with URL: {urls_batch[0]}. Retrying...")
                time.sleep(15)
                retries += 1

        # Fetch play counts from all loaded tabs
        for idx, url in enumerate(urls_batch):
            driver.switch_to.window(driver.window_handles[idx])

            try:
                track_name_element = driver.find_element(By.TAG_NAME, 'title')
                track_name = track_name_element.get_attribute("textContent").split('—')[0].strip()

                play_count_element = driver.find_element(By.CSS_SELECTOR, 'span[data-testid="playcount"]')
                play_count_text = play_count_element.text
                play_count_digits = re.findall(r'\d+', play_count_text)
                play_count = float(''.join(play_count_digits))

                total_play_count += play_count

                print(f"Play Count for {track_name} ({url}): {play_count}")

                # Append track details to the list
                track_play_counts.append({
                    'Artist': artist_name,
                    'Track Name': track_name,
                    'URL': url,
                    'Play Count': int(play_count)  # Convert to int for consistency
                })
            except NoSuchElementException:
                print(f"Could not find play count for {url}.")

        # Close all tabs except the first one to reuse it in the next iteration
        while len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()

        driver.switch_to.window(driver.window_handles[0])

    driver.quit()

    return total_play_count, track_play_counts


# Open a CSV file to write the individual track play counts
with open('track_playcounts_charts.csv', 'w', newline='') as csvfile:
    track_fieldnames = ['Artist', 'Track Name', 'URL', 'Play Count']
    track_writer = csv.DictWriter(csvfile, fieldnames=track_fieldnames)
    track_writer.writeheader()

    with open('playcount_charts.csv', 'w', newline='') as csvfile:
        fieldnames = ['Artist', 'Total Play Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for artist, tracks in artist_tracks.items():
            total_play_count, track_play_counts = fetch_play_count(artist, tracks)
            print(f"Total play count for {artist}: {total_play_count}")

            writer.writerow({'Artist': artist, 'Total Play Count': int(total_play_count)})

            # Write individual track play counts to the CSV
            for track in track_play_counts:
                track_writer.writerow(track)
