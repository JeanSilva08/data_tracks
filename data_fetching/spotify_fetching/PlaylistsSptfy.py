import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

client_id = ''
client_secret = ''


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
    playlist_ids = ["71Oc23mUiQmiM3SNYkmvV1",
                    "37i9dQZF1DXd2wJvXxyJb8",
                    "37i9dQZEVXbMXbN3EUUhlg",
                    "6GNmpxMYl4hD90GwGINyla",
                    "5DqR5bAbk7mTq5jnvJsjel",
                    "2KzqfWPN4UuS8Oxahfx4pU",
                    "4Zn9LFbwTguxz4XeAWTDi1",
                    "0X039tyQfxhPtVWoZUqqzX",
                    "5teJDcsrQJ9QZGYugoq2MB",
                    "1hCQkNupVD4HqfTS4GnMwC",
                    "49VFPROr6yhf8yB2J2wcNz",
                    "5MZvlLOt6b9JqbHOaEzJ5Z",
                    "1XwZaDHB3KOHfzpygfSfcR",
                    "4iXBmc9lmaFnjBKK9aCXg3",
                    "6pKvMoTAkiRhugrwibucHN",
                    "37i9dQZF1DX2L0iB23Enbq",
                    "527vAKGLtnxJefmY7QltHN",
                    "44HCx45fac9vrwqne4Sw41",
                    "3OXekjrqVhrdiZoZE5ZY9S",
                    "5mjOjSvZizVAUNjasnSy02",
                    "6dMJWeknEufFRxtTRB7Ufx",
                    "1yKMlyu7hirmy9fPxWcVnT",
                    "7hCUXE2FcQttBUJVz811BS",
                    "6VNAy0lActqHlZWbbpQcUW",
                    "37i9dQZF1DXdNL0ldoQCGi",
                    ]

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    playlist_tracks = {}
    playlist_names = []
    for playlist_id in playlist_ids:
        playlist_tracks[playlist_id] = fetch_playlist_tracks(playlist_id)
        playlist_name = fetch_playlist_name(sp, playlist_id)
        if playlist_name:
            playlist_names.append(playlist_name)

    artist_ids = [
        "25XJqeReVV38w0tR04GGBd",
        "3rfM2cGqF6DB0kUyytMkXx",
        "28ie4NNTa2VW2QV4Zray8M",
        "1WXbiUMl1AT9Inb619xPUg",
        "6jBww4kwlSrjaNYP7AQPtX",
        "68PYmgkbRP1qZnEWOry7sB",
        "4yGgbQJMq9orWypwqtdzYT",
        "2vWGxqWbGgmgxVDZ5CBvBP",
        "0oNOkdVXXFaWC9tPb7Ol10",
        "6J6U2JAv7LUF0cSQ98gpjM",
        "0BMccF4OSgl180EzdVFY9m",
        "0wopeyG3WHLoKcmrFD2jrY",
        "0xEdwBYYjxw6wk179Tq2sJ",
        "0y7B2G0jNMGWyQJsOoRMUt",
        "2NMYOlZHIEsSq7pp5jBjic",
        "7uskxjQtkzfiqHCNIIv3gD",
        "30Hiyu8fW3upjYdoXoXy8i",
        "1WQBwwssN6r8DSjUlkyUGW",
        "3Og0gjJyLFUdqIYzXxq6T6",
        "7KEZl3nvHOJaaLZUo1wLwc",
        "5XEiZVyQHpIDjhkIBbpf2G",
        "6RruMIOL9mfFjnNfZfsXhB",
        "3FVZlbowUWV4h0nKFKVb0a",
        "5OQwCMHaNZ6FtVcVNkkShY",
        "78TUxGXS6Jpos6nj2oEqSP",
        "7nhTCM7Tuu7NRQZsmpBIBg",
        "0bRPXWabRuRy4RqnycT5ne",
        "6Dzh6uXgA0QKVg1eIWxdDY",
        "3lrVtMWQakf49Evasc4FFW",
        "137b3EpKbbmxmY2dGgzx2Q",
        "2lTTvwwN7aNG21tKXHP8bU",
        "7rVT3dNwCamCtw5rC7salV",
        "65ZE0dYy4XIHtFBAGMKHhI",
        "3VI6PCewAVll6K4cYoNWt7",
        "6MWb3O5RfehDbCZsBfGrIG",
        "34dsFeNJO3am3bnNd9yxxd",
        "6obeWNZwOJv7P9EzIvu9zt",
        "6FruCl8GUxsP07s6LpsNKs"
    ]

    rows = []

    for artist_id in artist_ids:
        artist_name = fetch_artist_name(sp, artist_id)
        if artist_name:

            artist_row = [artist_name]

            for playlist_id in playlist_ids:

                track_names = []

                for track in playlist_tracks[playlist_id]:
                    track_details = track['track']
                    for track_artist in track_details['artists']:
                        if track_artist['id'] == artist_id or artist_id in [feat['id'] for feat in
                                                                            track_details['artists']]:
                            track_names.append(track_details['name'])
                            break

                track_names_str = ', '.join(track_names)
                artist_row.append(track_names_str)

            rows.append(artist_row)

    write_to_csv(rows, playlist_names)


if __name__ == "__main__":
    main()
