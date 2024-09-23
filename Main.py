import threading
from data_fetching.spotify_fetching.MonthlyListeners import MonthlyListeners
from data_fetching.youtube_fetching.YoutubeFeatFetcher import YoutubeFeatFetcher, initialize_artist_videosytfeat, \
    calculate_total_viewsytfeat, export_to_csvytfeat
from data_fetching.youtube_fetching.YoutubeFetcher import YoutubeFetcher, API_KEY, initialize_artist_videos, \
    calculate_total_views, export_to_csv
from data_fetching.youtube_fetching.YoutubeMscFetcher import YoutubeMscFetcher, initialize_artist_videosytmsc, \
    calculate_total_viewsytmsc, export_to_csvytmsc
from data_processing.DataProcessor import DataProcessor
from sheets_automation.UpdateSheets import UpdateSheets
from data_fetching.spotify_fetching.SptfyFollowers import PopularityFollowers
from data_fetching.spotify_fetching.TotalTracks import TotalTracks


class Main:
    @staticmethod
    def run():

        data_processed_event = threading.Event()

        fetch_thread = threading.Thread(target=MonthlyListeners.fetch_and_write_monthly_listeners)
        fetch_thread.start()

        fetch_thread.join()

        youtube_msc_fetcher = YoutubeMscFetcher(API_KEY)
        artist_videos = initialize_artist_videosytmsc()

        total_views = calculate_total_viewsytmsc(youtube_msc_fetcher, artist_videos)

        if total_views:
            print("\nTotal views for each artist:")
            for artist, views in total_views.items():
                print(f"{artist}: {views}")
            export_to_csvytmsc(total_views)
            print("Data exported to 'ytmsc_total_views.csv'")
        else:
            print("No videos found.")

        youtube_fetcher = YoutubeFetcher(API_KEY)

        artist_videos = initialize_artist_videos()
        total_views = calculate_total_views(youtube_fetcher,
                                            artist_videos)
        if total_views:
            print("\nTotal views for each artist:")
            for artist, views in total_views.items():
                print(f"{artist}: {views}")
            export_to_csv(total_views)
            print("Data exported to 'yt_total_views.csv'")
        else:
            print("No videos found.")

        youtube_feat_fetcher = YoutubeFeatFetcher(API_KEY)

        artist_videos = initialize_artist_videosytfeat()
        total_views = calculate_total_viewsytfeat(youtube_feat_fetcher,
                                                  artist_videos)

        if total_views:
            print("\nTotal views for each artist:")
            for artist, views in total_views.items():
                print(f"{artist}: {views}")
            export_to_csvytfeat(total_views)
            print("Data exported to 'ytfeat_total_views.csv'")

        else:
            print("No videos found.")

        popularity_followers = PopularityFollowers(client_id='fb5f08a6437c4e1dbcd18dc98475216b',
                                                   client_secret='6e9993758a7e4a08919de25cfa34bfc9')
        artist_followers = {}
        for artist_name in artist_names:
            _, followers = popularity_followers.get_followers(artist_name)
            artist_followers[artist_name] = followers
        file_path = 'data/total_followers_sptfy.csv'  # Specify the file path
        popularity_followers.export_followers_to_csv(artist_followers, file_path)

        DataProcessor.update_total_followers_sptfy()
        DataProcessor.update_monthly_listeners()
        DataProcessor.update_instagram_followers()
        DataProcessor.update_sptfy_playcount()
        DataProcessor.update_youtube_views()
        DataProcessor.update_youtubemsc_views()
        DataProcessor.update_youtubefeat_views()

        sheet_update_thread = threading.Thread(target=UpdateSheets.update_google_sheets, args=(data_processed_event,))
        sheet_update_thread.start()

        sheet_update_thread.join()


if __name__ == "__main__":
    artist_names = [
        "Mainstreet", "Orochi", "Mc Poze do Rodo", "BIN", "Borges", "Chefin", "Oruam", "Bielzin", "Dfideliz",
        "PL Quest", "Raffé", "Azevedo", "Leviano", "Ajaxx", "Kizzy", "jess beats", "RUXN", "MC Cabelinho",
        "Brutos", "A.R", "Vinicin", "MANO R7", "Amorim", "Buddy", "Mvk", "Pedrin", "Mc Filhão", "Shenlong",
        "DEGE", "Hashi", "Beny Free", "Feek", "Oliveira", "Pior Versão de Mim", "Oreozin", "Peziinho", "Grone",
        "Vt no beat"
    ]
    artist_urls = [
        "https://open.spotify.com/intl-pt/artist/25XJqeReVV38w0tR04GGBd",
        "https://open.spotify.com/intl-pt/artist/3rfM2cGqF6DB0kUyytMkXx",
        "https://open.spotify.com/intl-pt/artist/28ie4NNTa2VW2QV4Zray8M",
        "https://open.spotify.com/intl-pt/artist/1WXbiUMl1AT9Inb619xPUg",
        "https://open.spotify.com/intl-pt/artist/6jBww4kwlSrjaNYP7AQPtX",
        "https://open.spotify.com/intl-pt/artist/68PYmgkbRP1qZnEWOry7sB",
        "https://open.spotify.com/intl-pt/artist/4yGgbQJMq9orWypwqtdzYT",
        "https://open.spotify.com/intl-pt/artist/2vWGxqWbGgmgxVDZ5CBvBP",
        "https://open.spotify.com/intl-pt/artist/0oNOkdVXXFaWC9tPb7Ol10",
        "https://open.spotify.com/intl-pt/artist/6J6U2JAv7LUF0cSQ98gpjM",
        "https://open.spotify.com/intl-pt/artist/0BMccF4OSgl180EzdVFY9m",
        "https://open.spotify.com/intl-pt/artist/0wopeyG3WHLoKcmrFD2jrY",
        "https://open.spotify.com/intl-pt/artist/0xEdwBYYjxw6wk179Tq2sJ",
        "https://open.spotify.com/intl-pt/artist/0y7B2G0jNMGWyQJsOoRMUt",
        "https://open.spotify.com/intl-pt/artist/2NMYOlZHIEsSq7pp5jBjic",
        "https://open.spotify.com/intl-pt/artist/7uskxjQtkzfiqHCNIIv3gD",
        "https://open.spotify.com/intl-pt/artist/30Hiyu8fW3upjYdoXoXy8i",
        "https://open.spotify.com/intl-pt/artist/1WQBwwssN6r8DSjUlkyUGW",
        "https://open.spotify.com/intl-pt/artist/3Og0gjJyLFUdqIYzXxq6T6",
        "https://open.spotify.com/intl-pt/artist/7KEZl3nvHOJaaLZUo1wLwc",
        "https://open.spotify.com/intl-pt/artist/5XEiZVyQHpIDjhkIBbpf2G",
        "https://open.spotify.com/intl-pt/artist/6RruMIOL9mfFjnNfZfsXhB",
        "https://open.spotify.com/intl-pt/artist/3FVZlbowUWV4h0nKFKVb0a",
        "https://open.spotify.com/artist/5OQwCMHaNZ6FtVcVNkkShY",
        "https://open.spotify.com/artist/78TUxGXS6Jpos6nj2oEqSP",
        "https://open.spotify.com/intl-pt/artist/7nhTCM7Tuu7NRQZsmpBIBg",
        "https://open.spotify.com/intl-pt/artist/0bRPXWabRuRy4RqnycT5ne",
        "https://open.spotify.com/artist/6Dzh6uXgA0QKVg1eIWxdDY",
        "https://open.spotify.com/intl-pt/artist/3lrVtMWQakf49Evasc4FFW",
        "https://open.spotify.com/artist/137b3EpKbbmxmY2dGgzx2Q",
        "https://open.spotify.com/intl-pt/artist/2lTTvwwN7aNG21tKXHP8bU",
        "https://open.spotify.com/artist/7rVT3dNwCamCtw5rC7salV",
        "https://open.spotify.com/intl-pt/artist/65ZE0dYy4XIHtFBAGMKHhI",
        "https://open.spotify.com/artist/3VI6PCewAVll6K4cYoNWt7",
        "https://open.spotify.com/artist/6MWb3O5RfehDbCZsBfGrIG",
        "https://open.spotify.com/intl-pt/artist/34dsFeNJO3am3bnNd9yxxd",
        "https://open.spotify.com/intl-pt/artist/6obeWNZwOJv7P9EzIvu9zt",
        "https://open.spotify.com/intl-pt/artist/6FruCl8GUxsP07s6LpsNKs"

    ]

    Main.run()
