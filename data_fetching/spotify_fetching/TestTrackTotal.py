import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

def get_all_songs(artist_id):
    client_id = 'fb5f08a6437c4e1dbcd18dc98475216b'
    client_secret = '6e9993758a7e4a08919de25cfa34bfc9'

    # Authentication
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    # Initialize empty lists to store song information
    solo_songs = []
    single_songs = []
    feat_songs = []
    all_song_urls = set()  # To ensure no duplicates

    # Get artist albums
    albums = sp.artist_albums(artist_id, album_type='album', limit=50)
    for album in albums['items']:
        album_tracks = sp.album_tracks(album['id'])
        for track in album_tracks['items']:
            if track['external_urls']['spotify'] not in all_song_urls:
                solo_songs.append({'name': track['name'], 'url': track['external_urls']['spotify']})
                all_song_urls.add(track['external_urls']['spotify'])

    # Get artist singles
    singles = sp.artist_albums(artist_id, album_type='single', limit=50)
    for single in singles['items']:
        single_tracks = sp.album_tracks(single['id'])
        for track in single_tracks['items']:
            if track['external_urls']['spotify'] not in all_song_urls:
                single_songs.append({'name': track['name'], 'url': track['external_urls']['spotify']})
                all_song_urls.add(track['external_urls']['spotify'])

    # Get artist's top tracks (for features)
    top_tracks = sp.artist_top_tracks(artist_id)
    for track in top_tracks['tracks']:
        if track['external_urls']['spotify'] not in all_song_urls:
            feat_songs.append({'name': track['name'], 'url': track['external_urls']['spotify']})
            all_song_urls.add(track['external_urls']['spotify'])

    # Total number of unique songs
    total_songs = len(all_song_urls)

    return {
        'solo_songs': solo_songs,
        'single_songs': single_songs,
        'feat_songs': feat_songs,
        'total_songs': total_songs
    }

if __name__ == "__main__":
    artist_id = '28ie4NNTa2VW2QV4Zray8M'
    songs = get_all_songs(artist_id)
    print("Solo Songs:")
    for song in songs['solo_songs']:
        print(f"{song['name']} - {song['url']}")
    print("\nSingle Songs:")
    for song in songs['single_songs']:
        print(f"{song['name']} - {song['url']}")
    print("\nFeatured Songs:")
    for song in songs['feat_songs']:
        print(f"{song['name']} - {song['url']}")
    print(f"\nTotal Number of Songs: {songs['total_songs']}")
