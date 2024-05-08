import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class PopularityFollowers:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    def get_followers(self, artist_name):
        results = self.sp.search(q=artist_name, type='artist')
        if len(results['artists']['items']) == 0:
            return artist_name, None

        artist_id = results['artists']['items'][0]['id']
        num_followers = self.sp.artist(artist_id)['followers']['total']
        return artist_name, num_followers

    @staticmethod
    def export_followers_to_csv(artist_data, file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Artist', 'Followers'])
            for artist, followers in artist_data.items():
                writer.writerow([artist, followers])
        print(f'Data exported to total_followers_sptfy.csv')
