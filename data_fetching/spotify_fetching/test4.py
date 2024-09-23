import csv
import requests
from bs4 import BeautifulSoup
from constants import artists_charts


class MonthlyListeners:
    @staticmethod
    def fetch_and_write_monthly_listeners():
        with open('monthly_listeners_charts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Ouvintes Mensais"])

            for artist_url in artists_charts:
                artist_name, monthly_listeners = MonthlyListeners.get_monthly_listeners(artist_url)
                writer.writerow([monthly_listeners])

        print("Data exported to monthly_listeners_charts.csv")

    @staticmethod
    def get_monthly_listeners(artist_url):
        response = requests.get(artist_url)
        soup = BeautifulSoup(response.content, "html.parser")

        h1_tag = soup.find("h1", {"class": "Type__TypeElement-sc-goli3j-0", "data-encore-id": "type"})
        artist_name = h1_tag.text if h1_tag else "Unknown Artist"

        div_tag = soup.find("div", {"class": "Type__TypeElement-sc-goli3j-0", "data-encore-id": "type"})
        monthly_listeners = div_tag.text.strip().replace("monthly listeners", "") if div_tag else "Unknown Listeners"

        return artist_name, monthly_listeners


def main():
    MonthlyListeners.fetch_and_write_monthly_listeners()


if __name__ == "__main__":
    main()
