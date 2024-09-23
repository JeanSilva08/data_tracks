import csv
import requests
from bs4 import BeautifulSoup
from .constants import artists


class MonthlyListeners:
    @staticmethod
    def fetch_and_write_monthly_listeners():
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
