import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from constants import client_id, client_secret, playlist_ids, artist_ids


def fetch_playlist_tracks(playlist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    playlist_tracks = []
    offset = 0
    while True:
        tracks = sp.playlist_tracks(playlist_id, offset=offset)
        playlist_tracks.extend(tracks['items'])
        if not tracks['next']:
            break
        offset += len(tracks['items'])
    return playlist_tracks


def fetch_artist_name(sp, artist_id):
    try:
        return sp.artist(artist_id)['name']
    except Exception as e:
        print(f"Unable to retrieve artist name for {artist_id}. Error: {e}")
        return None


def fetch_playlist_name(sp, playlist_id):
    try:
        return sp.playlist(playlist_id)['name']
    except Exception as e:
        print(f"Unable to retrieve playlist name for {playlist_id}. Error: {e}")
        return None


def write_to_csv(rows, playlist_names):
    filename = "playlist_tracks.csv"
    header = ['Artist Name']
    header.extend(playlist_names)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)
    print(f"The results have been saved to {filename}")


def main():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    playlist_tracks = {}
    playlist_names = []
    for playlist_id in playlist_ids:
        playlist_tracks[playlist_id] = fetch_playlist_tracks(playlist_id)
        playlist_name = fetch_playlist_name(sp, playlist_id)
        if playlist_name:
            playlist_names.append(playlist_name)

    rows = []

    for artist_id in artist_ids:
        artist_name = fetch_artist_name(sp, artist_id)
        if artist_name:
            artist_row = [artist_name]
            for playlist_id in playlist_ids:
                track_names = []
                for track in playlist_tracks[playlist_id]:
                    track_details = track.get('track')
                    if track_details:
                        for track_artist in track_details.get('artists', []):
                            if track_artist['id'] == artist_id or artist_id in [feat['id']
                                                                                for feat
                                                                                in track_details.get('artists', [])]:
                                track_names.append(track_details['name'])
                                break
                track_names_str = ', '.join(track_names)
                artist_row.append(track_names_str)
            rows.append(artist_row)

    write_to_csv(rows, playlist_names)


if __name__ == "__main__":
    main()
