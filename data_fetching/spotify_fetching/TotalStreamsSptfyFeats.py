import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from constants import artist_charts_tracks  # Import the artist_charts_tracks dictionary


def fetch_play_count(artist_name, track_urls):
    options = Options()
    options.add_argument("user-data-dir=/home/mrsepiol/.config/google-chrome/Default")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    total_play_count = 0

    print(f"Fetching play counts for {artist_name}...")
    for url in track_urls:
        page_loaded = False
        retries = 0

        while not page_loaded and retries < 5:  # Retry up to 5 times
            try:
                driver.get(url)

                # Wait for the title element to confirm the page has loaded
                track_name_element = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'title')))
                track_name = track_name_element.get_attribute("textContent").split('—')[0].strip()

                # At this point, the page is considered loaded
                page_loaded = True

                # Attempt to find the play count element
                try:
                    play_count_element = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-testid="playcount"]')))
                    play_count_text = play_count_element.text
                    play_count_digits = re.findall(r'\d+', play_count_text)
                    play_count = float(''.join(play_count_digits))
                    total_play_count += play_count

                    print(f"Play Count for {track_name} ({url}): {play_count}")
                except Exception as e:
                    print(f"No play count found for {track_name} ({url}).")

            except Exception as e:
                print(f"Error loading page for URL: {url}. Retrying...")
                time.sleep(5)
                retries += 1

    driver.quit()

    return total_play_count


with open('playcount_charts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Artist', 'Total Play Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for artist, tracks in artist_charts_tracks.items():
        total_play_count = fetch_play_count(artist, tracks)
        print(f"Total play count for {artist}: {total_play_count}")

        total_play_count = int(total_play_count)
        writer.writerow({'Artist': artist, 'Total Play Count': total_play_count})
