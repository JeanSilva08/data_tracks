import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv


class TotalTracks:
    def __init__(self, artist_urls, client_id, client_secret):
        self.artist_urls = artist_urls
        self.client_id = client_id
        self.client_secret = client_secret

    def get_total_tracks(self):

        auth_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        total_tracks_data = {}

        for artist_url in self.artist_urls:

            artist_id = artist_url.split("/")[-1]


            albums = sp.artist_albums(artist_id, album_type='album')
            total_album_tracks = 0


            for album in albums['items']:
                total_album_tracks += album['total_tracks']


            singles = sp.artist_albums(artist_id, album_type='single')
            eps = sp.artist_albums(artist_id, album_type='album', limit=50)  # Assuming EPs are also albums

            total_singles_tracks = sum(single['total_tracks'] for single in singles['items'])
            total_eps_tracks = sum(ep['total_tracks'] for ep in eps['items'])


            total_tracks = total_album_tracks + total_singles_tracks + total_eps_tracks


            artist_info = sp.artist(artist_id)
            artist_name = artist_info.get("name", "Unknown Artist")


            total_tracks_data[artist_name] = total_tracks

        return total_tracks_data

    def export_to_csv(self, filename):

        total_tracks_data = self.get_total_tracks()


        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Artist', 'Total Tracks'])
            for artist, total_tracks in total_tracks_data.items():
                writer.writerow([artist, total_tracks])

        print(f"The results have been saved to {filename}")

