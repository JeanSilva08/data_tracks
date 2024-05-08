import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def fetch_play_count(artist_name, track_urls):
    # Define Chrome options and specify the profile directory
    options = Options()
    options.add_argument("user-data-dir=/home/mrsepiol/.config/google-chrome/Default")
    options.add_argument("--headless")  # Run in headless mode

    # Initialize Chrome webdriver with options
    driver = webdriver.Chrome(options=options)

    # Initialize total play count for the artist
    total_play_count = 0

    # Fetch play count for each track URL in batches
    batch_size = 10  # Adjust batch size as needed
    print(f"Fetching play counts for {artist_name}...")
    for i in range(0, len(track_urls), batch_size):
        batch_urls = track_urls[i:i + batch_size]
        # Load all track pages in the batch
        for url in batch_urls:
            driver.get(url)
        # Wait for all play count elements to be located
        play_count_elements = WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[data-testid="playcount"]')))
        # Extract play counts and sum them up
        for play_count_element in play_count_elements:
            play_count_text = play_count_element.text
            play_count_digits = re.findall(r'\d+', play_count_text)
            play_count = float(''.join(play_count_digits))
            total_play_count += play_count
            print("Play Count:", play_count)

    # Close the browser
    driver.quit()

    return total_play_count


# Dictionary of artist names and their corresponding track URLs #
artist_tracks = {
    "Mainstreet": ['https://open.spotify.com/intl-pt/track/5t2RXNtjGIzKPGiNYSU6FG',
                   "https://open.spotify.com/intl-pt/track/7MybxBlifyFeyfds4x4g5p",
                   "https://open.spotify.com/intl-pt/track/1DFl6V6pItoSRoCDR6zzAy",
                   "https://open.spotify.com/intl-pt/track/315JaAW5Ed3C7rnKOGMg6e",
                   "https://open.spotify.com/intl-pt/track/5V3CmFA57izQ3cwZFEpmle",
                   "https://open.spotify.com/intl-pt/track/6Kow39MGiBWCypfj14oZ6A",
                   "https://open.spotify.com/intl-pt/track/6LKdX3mQwwOblLhBCfmGlU",
                   "https://open.spotify.com/intl-pt/track/0MW2WCZsE8BALPlGM9oVyd",
                   "https://open.spotify.com/intl-pt/track/49NyXYwAtRZcjTojDdffrz",
                   "https://open.spotify.com/intl-pt/track/1o3YckJFGqTcs4oHsTp6I8",
                   "https://open.spotify.com/intl-pt/track/095tiFEdBunjDaXo428cDj",
                   "https://open.spotify.com/intl-pt/track/15I6cAW7N022uQ51FJmRPB",
                   "https://open.spotify.com/intl-pt/track/2twZl1jsRbJRTNCE6VB6eW",
                   "https://open.spotify.com/intl-pt/track/6rCAD1L3H87qRNGGVli37l",
                   "https://open.spotify.com/intl-pt/track/6S00iFG7VSum4SgXoNXha8",
                   "https://open.spotify.com/intl-pt/track/3by89k8zGClgmQgz9SbtKp",
                   "https://open.spotify.com/intl-pt/track/5zHgKTl9uTZqUfdbszAU3W",
                   "https://open.spotify.com/intl-pt/track/79SdFOAZlkc2xrlNJPRrn6",
                   "https://open.spotify.com/intl-pt/track/44v9eNGRuwFDXzPWu2GkHP",
                   "https://open.spotify.com/intl-pt/track/63HYpMDcQo0Fryhmje08Bl",
                   "https://open.spotify.com/intl-pt/track/37LWZe5mdHIKuXBh8GuwlH",
                   "https://open.spotify.com/intl-pt/track/24Qz27YhZ8eVnJl6sD6hyd",
                   "https://open.spotify.com/intl-pt/track/6yadp6uXJpV1ZvKcu73Ji0",
                   "https://open.spotify.com/intl-pt/track/3n7ASTQanOp5milmESBqlt",
                   "https://open.spotify.com/intl-pt/track/1QjmBR1bqmh0fYrVnD9iU8",
                   "https://open.spotify.com/intl-pt/track/1BoMpKPeITtg3HN9Ursz5T",
                   "https://open.spotify.com/intl-pt/track/5cCwZJUf8QiCQGnyakhpmF",
                   "https://open.spotify.com/intl-pt/track/545IGh8s0x4tniaiBLHL6t",
                   "https://open.spotify.com/intl-pt/track/1EsgC6YzdQkKmPKB1QyEiE",
                   "https://open.spotify.com/intl-pt/track/76klxh7fnauuROKC2kDuHG",
                   "https://open.spotify.com/intl-pt/track/0cP0H3mezxubJHdDCUEMX4",
                   "https://open.spotify.com/intl-pt/track/5SO4R7IpqIBcm6LjUvKmlj",
                   "https://open.spotify.com/intl-pt/track/1KKnzHMySnYqkjwSHqgVVI",
                   "https://open.spotify.com/intl-pt/track/6iO7nBM2StwcPvuyblR0P4",
                   "https://open.spotify.com/intl-pt/track/152JuulFiSlmLQU1p3oM4b",
                   "https://open.spotify.com/intl-pt/track/1bQgCqHYpDvTs5QwEQX937",
                   "https://open.spotify.com/intl-pt/track/4Exjs0i5CFfKpIegAqcYOg",
                   "https://open.spotify.com/intl-pt/track/0J8LV0mKp1a2mBeiJTv1xZ",
                   "https://open.spotify.com/intl-pt/track/7DqtyR5w0QXD6BKnyawIm6",
                   "https://open.spotify.com/intl-pt/track/40JTPDvqaCP3hAKwczbshP",
                   "https://open.spotify.com/intl-pt/track/490GbBa2Apa3vNHcPkyJWO",
                   "https://open.spotify.com/intl-pt/track/1ltaaZhoXHHLQFYzyKSIGp",
                   "https://open.spotify.com/intl-pt/track/2oLCJDxRZYoEiLuSwanbjG",
                   "https://open.spotify.com/intl-pt/track/56xYjxmkJxnpBVQi6pLSiL",
                   "https://open.spotify.com/intl-pt/track/6rGOddAeZDBywYmeDYhJrQ",
                   "https://open.spotify.com/intl-pt/track/7eZCP5YHeqVsIGaPp8y9ac",
                   "https://open.spotify.com/intl-pt/track/7byTUdupcQ5dSRd3D9jAQo",
                   "https://open.spotify.com/intl-pt/track/0WYtu0wyQrJGlW1O8IYH1q",
                   "https://open.spotify.com/intl-pt/track/2HrjORyFBF3IFnXOAC3Rox",
                   "https://open.spotify.com/intl-pt/track/27iAEVwv6aMaICmXPkk50m",
                   "https://open.spotify.com/intl-pt/track/4BfppnNi6ZQTI8Ezo97zX6",
                   "https://open.spotify.com/intl-pt/track/0qzdA4ZdKqoTP4BEVpJdRu",
                   "https://open.spotify.com/intl-pt/track/5adH787aC7muiWC60s8Yvt",
                   "https://open.spotify.com/intl-pt/track/6jxE4XjFVSKF18kfo7FCl9",
                   "https://open.spotify.com/intl-pt/track/3QGxgNaqaFSpORp2OVLXHR",
                   "https://open.spotify.com/intl-pt/track/6CBdQXFI9nPUTVf51cWWxO",
                   "https://open.spotify.com/intl-pt/track/6jJiQk7l8SGVW2dfuG0IH2",
                   "https://open.spotify.com/intl-pt/track/2EQe3IsJqNfS8WACLeZnaY",
                   "https://open.spotify.com/intl-pt/track/6aqEqwMX0bnXO4pgEfXcPi",
                   "https://open.spotify.com/intl-pt/track/7xY5NUCid0WymfaXBZGhpW",
                   "https://open.spotify.com/intl-pt/track/0m5U5BkdjyDs0Fppkxvt2U",
                   "https://open.spotify.com/intl-pt/track/2VgNXyQcrsSyQdT4YyuFCu",
                   "https://open.spotify.com/intl-pt/track/7kOxU71fB54lrzu2GaZiNr",
                   "https://open.spotify.com/intl-pt/track/4sD1WFRLLoNMxgDHaTkF0I",
                   "https://open.spotify.com/intl-pt/track/5WSELUpi4GjDx3nRolKvSy",
                   "https://open.spotify.com/intl-pt/track/1IgyrKsjlZFo4EsQJtIbsa",
                   "https://open.spotify.com/intl-pt/track/06XgmjLenw60Y0VkCoxu8O",
                   "https://open.spotify.com/intl-pt/track/6EPTq7EQn8jrUPo3UoS61C",
                   "https://open.spotify.com/intl-pt/track/7IG7laqVpcvIIULrwWP5SA",
                   "https://open.spotify.com/intl-pt/track/3RuaQEnUtAYSblbk9K16u8",
                   "https://open.spotify.com/intl-pt/track/5Rm5tzLlpbBpUorSDETbjg",
                   "https://open.spotify.com/intl-pt/track/4VAo4FcgD6v9Ha9sRTn1Iv",
                   "https://open.spotify.com/intl-pt/track/3ZBRYFOmXvO0nQWbKWgIn3",
                   "https://open.spotify.com/intl-pt/track/68cPbG7hJnwDW9nPX1uQcX",
                   "https://open.spotify.com/intl-pt/track/2ye9BKhLI6xv7mOgXcq1PS",
                   "https://open.spotify.com/intl-pt/track/2YHdQVG5x6XI8HmdcqGJnn",
                   "https://open.spotify.com/intl-pt/track/4U8MZkasPn6VfwlwG3egGt",
                   "https://open.spotify.com/intl-pt/track/3suLdq5ZeXRrhpsYIMWrAQ",
                   "https://open.spotify.com/intl-pt/track/0rRuJdTpQFw5O5pcVytvwm",
                   "https://open.spotify.com/intl-pt/track/7p7ucw8UgzpwYnCfEhCxxn",
                   "https://open.spotify.com/intl-pt/track/5nIGVYXsdnS86hhbhIty2B",
                   "https://open.spotify.com/intl-pt/track/2I26XWAyR6vffAzwhAxdqO",
                   "https://open.spotify.com/intl-pt/track/32IGREEfY97uQ19npMKIlO",
                   "https://open.spotify.com/intl-pt/track/1BGHVKmt3Z2FArfkAvujcI",
                   "https://open.spotify.com/intl-pt/track/3PEecVkDpSSxey4mVssneS",
                   "https://open.spotify.com/intl-pt/track/7b8kjWj4TKWmWo2LX9Lkiz",
                   "https://open.spotify.com/intl-pt/track/1CBjYXLotHrkiykMbI7EaU"],
}

# Fetch and print the total play count for each artist's tracks
with open('playcount.csv', 'w', newline='') as csvfile:
    fieldnames = ['Artist', 'Total Play Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for artist, tracks in artist_tracks.items():
        total_play_count = fetch_play_count(artist, tracks)
        print(f"Total play count for {artist}: {total_play_count}")
        writer.writerow({'Artist': artist, 'Total Play Count': total_play_count})
