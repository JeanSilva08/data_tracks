import csv


class DataProcessor:
    @staticmethod
    def update_monthly_listeners():

        with open("data/monthly_listeners.csv", mode="r", encoding="utf-8") as monthly_file:
            reader = csv.DictReader(monthly_file)
            monthly_data = {row["Nome"]: row["Ouvintes Mensais"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        ouvintes_mensais_index = 4

        for row in rows[4:]:
            nome = row[0]
            if nome in monthly_data:
                row[ouvintes_mensais_index] = monthly_data[nome]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_total_followers_sptfy():

        with open("data/total_followers_sptfy.csv", mode="r", encoding="utf-8") as followers_file:
            reader = csv.DictReader(followers_file)
            followers_data = {row["Artist"]: row["Followers"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        seguidores_index = 5

        for i, row in enumerate(rows[2:]):
            artist_name = row[0]
            if artist_name in followers_data:
                row[seguidores_index] = followers_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_total_tracks():

        with open("data/total_tracks.csv", mode="r", encoding="utf-8") as tracks_file:
            reader = csv.DictReader(tracks_file)
            tracks_data = {row["Artist"]: row["Total Tracks"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        total_tracks_index = 3

        for i, row in enumerate(rows[1:]):
            artist_name = row[0]
            if artist_name in tracks_data:
                row[total_tracks_index] = tracks_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_sptfy_playcount():

        with open("data/playcount.csv", mode="r", encoding="utf-8") as playcount_file:
            reader = csv.DictReader(playcount_file)
            playcount_data = {row["Artist"]: row["Total Play Count"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        total_streams_index = 10

        for row in rows[1:]:
            artist_name = row[0]
            if artist_name in playcount_data:
                row[total_streams_index] = playcount_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_instagram_followers():

        with open("data/insta_followers.csv", mode="r", encoding="utf-8") as followers_file:
            reader = csv.reader(followers_file)
            next(reader)
            followers_data = {f"Artist{i + 1}": row[0] for i, row in enumerate(reader)}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        seguidores_index = 22

        for i, row in enumerate(rows[3:]):
            artist_name = f"Artist{i + 1}"
            if artist_name in followers_data:
                row[seguidores_index] = followers_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_youtube_views():

        with open("data/yt_total_views.csv", mode="r", encoding="utf-8") as views_file:
            reader = csv.DictReader(views_file)
            views_data = {row["Artist"]: row["Total Views"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        youtube_views_index = 15

        for row in rows[3:]:
            artist_name = row[0]
            if artist_name in views_data:
                row[youtube_views_index] = views_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_youtubemsc_views():

        with open("data/ytmsc_total_views.csv", mode="r", encoding="utf-8") as views_file:
            reader = csv.DictReader(views_file)
            views_data = {row["Artist"]: row["Total Views"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        youtube_views_index = 17

        for row in rows[3:]:
            artist_name = row[0]
            if artist_name in views_data:
                row[youtube_views_index] = views_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")

    @staticmethod
    def update_youtubefeat_views():

        with open("data/ytfeat_total_views.csv", mode="r", encoding="utf-8") as views_file:
            reader = csv.DictReader(views_file)
            views_data = {row["Artist"]: row["Total Views"] for row in reader}

        with open("data/Midia Kit Artistas_teste.csv", mode="r", encoding="utf-8") as final_file:
            reader = csv.reader(final_file)
            header = next(reader)
            rows = list(reader)

        youtube_views_index = 16

        for row in rows[3:]:
            artist_name = row[0]
            if artist_name in views_data:
                row[youtube_views_index] = views_data[artist_name]

        with open("data/Midia Kit Artistas_teste.csv", mode="w", newline="", encoding="utf-8") as updated_file:
            writer = csv.writer(updated_file)
            writer.writerow(header)
            writer.writerows(rows)

        print("Data exported to Midia Kit Artistas_teste.csv")
