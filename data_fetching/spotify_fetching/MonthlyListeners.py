import csv
import requests
from bs4 import BeautifulSoup


class MonthlyListeners:
    @staticmethod
    def fetch_and_write_monthly_listeners():
        artists = [
            "https://open.spotify.com/intl-pt/artist/25XJqeReVV38w0tR04GGBd",
            "https://open.spotify.com/intl-pt/artist/3rfM2cGqF6DB0kUyytMkXx",
            "https://open.spotify.com/intl-pt/artist/28ie4NNTa2VW2QV4Zray8M",
            "https://open.spotify.com/intl-pt/artist/1WXbiUMl1AT9Inb619xPUg",
            "https://open.spotify.com/intl-pt/artist/6jBww4kwlSrjaNYP7AQPtX",
            "https://open.spotify.com/intl-pt/artist/68PYmgkbRP1qZnEWOry7sB",
            "https://open.spotify.com/intl-pt/artist/4yGgbQJMq9orWypwqtdzYT",
            "https://open.spotify.com/intl-pt/artist/2vWGxqWbGgmgxVDZ5CBvBP",
            "https://open.spotify.com/intl-pt/artist/0oNOkdVXXFaWC9tPb7Ol10",
            "https://open.spotify.com/intl-pt/artist/6J6U2JAv7LUF0cSQ98gpjM",
            "https://open.spotify.com/intl-pt/artist/0BMccF4OSgl180EzdVFY9m",
            "https://open.spotify.com/intl-pt/artist/0wopeyG3WHLoKcmrFD2jrY",
            "https://open.spotify.com/intl-pt/artist/0xEdwBYYjxw6wk179Tq2sJ",
            "https://open.spotify.com/intl-pt/artist/0y7B2G0jNMGWyQJsOoRMUt",
            "https://open.spotify.com/intl-pt/artist/2NMYOlZHIEsSq7pp5jBjic",
            "https://open.spotify.com/intl-pt/artist/7uskxjQtkzfiqHCNIIv3gD",
            "https://open.spotify.com/intl-pt/artist/30Hiyu8fW3upjYdoXoXy8i",
            "https://open.spotify.com/intl-pt/artist/1WQBwwssN6r8DSjUlkyUGW",
            "https://open.spotify.com/intl-pt/artist/3Og0gjJyLFUdqIYzXxq6T6",
            "https://open.spotify.com/intl-pt/artist/7KEZl3nvHOJaaLZUo1wLwc",
            "https://open.spotify.com/intl-pt/artist/5XEiZVyQHpIDjhkIBbpf2G",
            "https://open.spotify.com/intl-pt/artist/6RruMIOL9mfFjnNfZfsXhB",
            "https://open.spotify.com/intl-pt/artist/3FVZlbowUWV4h0nKFKVb0a",
            "https://open.spotify.com/artist/5OQwCMHaNZ6FtVcVNkkShY",
            "https://open.spotify.com/artist/78TUxGXS6Jpos6nj2oEqSP",
            "https://open.spotify.com/intl-pt/artist/7nhTCM7Tuu7NRQZsmpBIBg",
            "https://open.spotify.com/intl-pt/artist/0bRPXWabRuRy4RqnycT5ne",
            "https://open.spotify.com/artist/6Dzh6uXgA0QKVg1eIWxdDY",
            "https://open.spotify.com/intl-pt/artist/3lrVtMWQakf49Evasc4FFW",
            "https://open.spotify.com/artist/137b3EpKbbmxmY2dGgzx2Q",
            "https://open.spotify.com/intl-pt/artist/2lTTvwwN7aNG21tKXHP8bU",
            "https://open.spotify.com/artist/7rVT3dNwCamCtw5rC7salV",
            "https://open.spotify.com/intl-pt/artist/65ZE0dYy4XIHtFBAGMKHhI",
            "https://open.spotify.com/artist/3VI6PCewAVll6K4cYoNWt7",
            "https://open.spotify.com/artist/6MWb3O5RfehDbCZsBfGrIG",
            "https://open.spotify.com/intl-pt/artist/34dsFeNJO3am3bnNd9yxxd",
            "https://open.spotify.com/intl-pt/artist/6obeWNZwOJv7P9EzIvu9zt",
            "https://open.spotify.com/intl-pt/artist/6FruCl8GUxsP07s6LpsNKs"
        ]

        with open('data/monthly_listeners.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nome", "", "Ouvintes Mensais"])

            for artist_url in artists:
                artist_name, monthly_listeners = MonthlyListeners.get_monthly_listeners(artist_url)
                writer.writerow([artist_name, "", monthly_listeners])

        print("Data exported to monthly_listeners.csv")

    @staticmethod
    def get_monthly_listeners(artist_url):
        response = requests.get(artist_url)
        soup = BeautifulSoup(response.content, "html.parser")

        h1_tag = soup.find("h1", {"class": "Type__TypeElement-sc-goli3j-0", "data-encore-id": "type"})

        artist_name = h1_tag.text

        div_tag = soup.find("div", {"class": "Type__TypeElement-sc-goli3j-0", "data-encore-id": "type"})

        monthly_listeners = div_tag.text.strip().replace("monthly listeners", "") if div_tag else ""

        return artist_name, monthly_listeners
