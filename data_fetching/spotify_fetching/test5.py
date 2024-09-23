import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_playlist_artists(playlist_url):
    # Substitua pelos seus Client ID e Client Secret
    client_id = 'fb5f08a6437c4e1dbcd18dc98475216b'
    client_secret = '6e9993758a7e4a08919de25cfa34bfc9'

    # Autenticação
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    # Extrair o ID da playlist da URL
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Obter os dados da playlist
    results = sp.playlist_tracks(playlist_id)

    artists = set()

    while results:
        for item in results['items']:
            track = item['track']
            for artist in track['artists']:
                artists.add((artist['name'], artist['id']))

        # Verificar se há mais páginas de resultados
        if results['next']:
            results = sp.next(results)
        else:
            results = None

    return artists


# Exemplo de uso
playlist_url = 'https://open.spotify.com/playlist/6pKvMoTAkiRhugrwibucHN'
artists = get_playlist_artists(playlist_url)

for artist_name, artist_id in artists:
    print(f"{artist_id}")