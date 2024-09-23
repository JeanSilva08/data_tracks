from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with your own API key
API_KEY = 'AIzaSyD74qS0b9EHk5P-wWMOXXqWk4HTe7Fas04'
# Replace with the channel IDs of the artists
CHANNEL_IDS = {
    "Mainstreet": "UCDiQ-LZ8dfc3cmoGBxMDS7Q",
    "Orochi": "UCQSDP7H4BINtrZ0bJc_FNIA",
    "Poze": "UCsyd_nnNNDxlOs9TYrDvCoQ",
    "Bin": "UCP0TWIE6oz5raG3FB8tTDmw",
    "Borges": "UCBRWI1h-efdTbVZK6RQdGqA",
    "Chefin": "x",
    "Oruam": "x",
    "Bielzin": "x",
    "Dfideliz": "UC0oTDMKxiVS5Kj3CnYnEISg",
    "PL Quest": "UC-9-kyTW8ZkZNDHQJ6FgpwQ",
    "Raffe": "x",
    "Azevedo": "UC4R8DWoMoI7CAwX8_LjQHig",
    "Leviano": "UCYfdidRxbB8Qhf0Nx7ioOYw",
    "Ajaxx": "x",
    "Kizzy": "x",
    "jess beat": "UCEgdi0XIXXZ-qJOFPf4JSKw",
    "RUXN": "UCfM3zsQsOnfWNUppiycmBuw",
    "MC Cabelinho": "UCjhZqfzCp1aDE0GeugC0GXw",
    "Brutos": "x",
    "A.R": "x",
    "Vinicin": "UCfM3zsQsOnfWNUppiycmBuw",
    "Mano R7": "UCwllLf7J2DmBmxSe_MCHgYQ",
    "Amorim": "x",
    "Budy": "UC9uU78JQnuF0PYvvCe9OCJw",
    "MVK": "UC-9oGMUxHsIhpTPwOQkdb1w",
    "Pedrin": "UCkcrPDvxYDAdjksVT1ShAMQ",
    "Filhão": "x",
    "Shenlong": "x",
    "DEGE": "UCUYq4-ru4v9iAs79_0fhLhA",
    "Hashi": "x",
    "Benny": "UC682IefNWj1TAg6mcywYUkA",
    "Feek": "UCm5_57oRHlI2KQHOIMsaxmQ",
    "Oliveira": "x",
    "Pior versão de mim": "UCRPmcZiyYKBffAgbE15TCYA",
    "Oreozin": "UCTbh9go3nR1mQpImzeyThYQ",
    "Peziinho": "x",
    "Grone": "UCmTOP3EH8agqTaQgJuCjw3A",
    "VT no Beat": "UC3sU0AcRwUEnEW277gKRAng"
}


def get_top_videos(api_key, channel_id, max_results=5):
    if channel_id == "x":
        return None

    try:
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Fetch the uploads playlist ID
        request = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        )
        response = request.execute()

        if 'items' not in response or not response['items']:
            print(f"No items found for channel ID: {channel_id}")
            return []

        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Fetch the top videos from the uploads playlist
        request = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=max_results
        )
        response = request.execute()

        videos = []
        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            videos.append({'title': title, 'video_id': video_id})

        return videos

    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
        return []
    except KeyError as e:
        print(f"A KeyError occurred: {e}")
        return []


if __name__ == '__main__':
    results = {}
    for artist, channel_id in CHANNEL_IDS.items():
        print(f"Fetching top videos for {artist} (Channel ID: {channel_id})")
        top_videos = get_top_videos(API_KEY, channel_id)
        results[artist] = top_videos
        if top_videos is not None:
            for idx, video in enumerate(top_videos, start=1):
                print(f"{idx}. {video['title']} (https://www.youtube.com/watch?v={video['video_id']})")
        else:
            print(f"No videos found for {artist}.")
        print("\n")

    print("Results:", results)
