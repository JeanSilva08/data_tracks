import csv
from collections import defaultdict

def get_top_five_tracks_per_artist(file_path):
    # Dictionary to store track information grouped by artist
    artist_tracks = defaultdict(list)

    # Read the CSV file
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            artist = row['Artist']
            track_name = row['Track Name']
            play_count = int(row['Play Count'])
            url = row['URL']

            # Append track information to the artist's list
            artist_tracks[artist].append({
                'Track Name': track_name,
                'Play Count': play_count,
                'URL': url
            })

    # Dictionary to store top five tracks per artist
    top_five_tracks = {}

    # Find top five tracks for each artist
    for artist, tracks in artist_tracks.items():
        # Sort the tracks by play count in descending order and get the top five
        top_tracks = sorted(tracks, key=lambda x: x['Play Count'], reverse=True)[:5]
        top_five_tracks[artist] = top_tracks

    return top_five_tracks

# Define the path to the CSV file
file_path = 'track_playcounts.csv'

# Get the top five tracks for each artist
top_five_tracks_per_artist = get_top_five_tracks_per_artist(file_path)

# Prepare data for export to CSV
export_data = []
for artist, tracks in top_five_tracks_per_artist.items():
    top_tracks = [track['Track Name'].split(' - ')[0] for track in tracks]
    top_tracks_str = ' - '.join(top_tracks)  # Join top tracks into a single string with ' - ' separator
    export_data.append({
        'Artist': artist,
        'Top 5 Tracks': top_tracks_str
    })

# Write the data to a new CSV file
output_file_path = 'artist_top_tracks.csv'
with open(output_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Artist', 'Top 5 Tracks']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in export_data:
        writer.writerow(row)

print(f"Data has been exported to {output_file_path}")
