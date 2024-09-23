import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from requests.exceptions import ReadTimeout, ConnectionError


def retry_request(func, *args, retries=5, delay=1, backoff=2, **kwargs):
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except (spotipy.exceptions.SpotifyException, ReadTimeout, ConnectionError) as e:
            if attempt < retries - 1:
                print(f"Request failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
                delay *= backoff
            else:
                raise
    return None


def get_all_items(func, *args, **kwargs):
    items = []
    offset = 0
    limit = 50
    while True:
        kwargs.update({'limit': limit, 'offset': offset})
        response = retry_request(func, *args, **kwargs)
        if not response or not response['items']:
            break
        items.extend(response['items'])
        offset += limit
    return items


def get_artist_tracks(artist_id):
    try:
        # Authenticate with Spotify API
        auth_manager = SpotifyClientCredentials(client_id='161a8e2ab6104bb29940b2681262813e',
                                                client_secret='dadbe18c00b94c13b14df6d67f797573')
        sp = spotipy.Spotify(auth_manager=auth_manager)

        # Get artist details
        artist = retry_request(sp.artist, artist_id)
        if not artist:
            print(f"No artist found with the ID {artist_id}")
            return [], 0

        print(f"Found artist {artist['name']} with ID {artist_id}")

        # Get all albums where the artist is a primary artist or featured
        albums = get_all_items(sp.artist_albums, artist_id, album_type='album,single,appears_on')

        # Extract Spotify URLs and names of all tracks where the artist is a primary artist or featured
        tracks_info = {}
        for album in albums:
            tracks = get_all_items(sp.album_tracks, album['id'])
            for track in tracks:
                if any(artist['id'] == artist_id for artist in track['artists']):
                    if 'spotify' in track['external_urls']:
                        track_name = track['name']
                        track_url = track['external_urls']['spotify']
                        # Add the track to the dictionary if it's not already present
                        if track_name not in tracks_info:
                            tracks_info[track_name] = track_url

        return list(tracks_info.values()), len(tracks_info)

    except Exception as e:
        print(f"Error fetching tracks for artist ID {artist_id}: {e}")
        return [], 0


# Prompt user to input artist ID
artist_id = input("Enter the ID of the artist: ")

# Get Spotify URLs and names of all songs for the specified artist
artist_tracks, total_tracks = get_artist_tracks(artist_id)

# Print the total number of tracks and the song names with Spotify URLs
if artist_tracks:
    print(f"Total number of tracks by artist with ID '{artist_id}': {total_tracks}")
    print(f"Songs by artist with ID '{artist_id}':")
    for track_url in artist_tracks:
        print(f'"{track_url}",')
else:
    print(f"No songs found for artist with ID '{artist_id}'")
