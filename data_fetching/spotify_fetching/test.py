import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import artist_tracks  # Import the artist_tracks dictionary


def fetch_play_count(artist_name, track_urls):
    options = Options()
    options.add_argument("user-data-dir=/home/mrsepiol/.config/google-chrome/Default")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    total_play_count = 0
    track_play_counts = []  # To store play counts for individual tracks

    print(f"Fetching play counts for {artist_name}...")
    for url in track_urls:
        page_loaded = False
        retries = 0

        while not page_loaded and retries < 5:  # Retry up to 5 times
            try:
                driver.get(url)

                # Fetch the track name from the title tag
                track_name_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'title')))
                track_name = track_name_element.get_attribute("textContent").split('—')[0].strip()

                play_count_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="playcount"]')))

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

                page_loaded = True

            except Exception as e:
                print(f"Error loading page for URL: {url}. Retrying...")
                time.sleep(5)
                retries += 1

    driver.quit()

    return total_play_count, track_play_counts


# Open a CSV file to write the individual track play counts
with open('track_playcounts.csv', 'w', newline='') as csvfile:
    track_fieldnames = ['Artist', 'Track Name', 'URL', 'Play Count']
    track_writer = csv.DictWriter(csvfile, fieldnames=track_fieldnames)
    track_writer.writeheader()

    with open('playcount.csv', 'w', newline='') as csvfile:
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
