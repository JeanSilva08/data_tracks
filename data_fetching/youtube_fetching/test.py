from googleapiclient.discovery import build
from time import sleep

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = ''

# Number of videos to request in each batch
BATCH_SIZE = 50

# Delay between API requests (in seconds)
REQUEST_DELAY = 1


class VideoManager:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_views(self, video_ids):
        video_info = {}
        batch_count = len(video_ids) // BATCH_SIZE + 1

        for i in range(batch_count):
            batch_ids = video_ids[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
            request = self.youtube.videos().list(
                part='snippet,statistics',  # Include 'snippet' to fetch video title
                id=','.join(batch_ids)
            )
            response = request.execute()

            for item in response.get('items', []):
                video_id = item['id']
                title = item['snippet']['title']
                view_count = int(item['statistics']['viewCount'])
                video_info[video_id] = {'title': title, 'views': view_count}

                # Print progress
                print(f"Fetched views for video '{title}': {view_count}")

            # Throttle requests to avoid rate limit
            sleep(REQUEST_DELAY)

        return video_info


def initialize_artist_videos():
    return {
        "Teste": ["EZZkjvaU_IQ"],

        "Borges": ["", ""],
        "Chefin": ["", ""],
        "Oruam": ["", ""],
        "Bielzin": ["", ""],
        "Dfideliz": ["", ""],
        "PL Quest": ["", ""],
        "Raffé": ["", ""],
        "Azevedo": ["", ""],
        "Leviano": ["", ""],
        "Ajaxx": ["", ""],
        "Kizzy": ["", ""],
        "jess beats": ["", ""],
        "RUXN": ["", ""],
        "MC Cabelinho": ["", ""],
        "Brutos": ["", ""],
        "A.R": ["", ""],
        "Vinicin": ["", ""],
        "MANO R7": ["", ""],
        "Amorim": ["", ""],
        "Buddy": ["", ""],
        "Mvk": ["", ""],
        "Pedrin": ["", ""],
        "Mc Filhão": ["", ""],
        "Shenlong": ["", ""],
        "DEGE": ["", ""],
        "Hashi": ["", ""],
        "Beny Free": ["", ""],
        "Feek": ["", ""],
        "Oliveira": ["", ""],
        "Pior Versão de Mim": ["", ""],
        "Oreozin": ["", ""],
        "Peziinho": ["", ""],
        "Grone": ["", ""],
        "Vt no beat": ["", ""]
    }


def calculate_total_views(video_manager, artist_videos):
    total_views = {}

    for artist, video_ids in artist_videos.items():
        print(f"\nCalculating total views for {artist}:")
        video_views = video_manager.get_video_views(video_ids)
        total_views[artist] = sum(video_info['views'] for video_info in video_views.values())

    return total_views


if __name__ == "__main__":
    artist_videos = initialize_artist_videos()

    video_manager = VideoManager(API_KEY)
    total_views = calculate_total_views(video_manager, artist_videos)

    if total_views:
        print("\nTotal views for each artist:")
        for artist, views in total_views.items():
            print(f"{artist}: {views}")
    else:
        print("No videos found.")
