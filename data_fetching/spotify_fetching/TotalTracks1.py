# count_tracks.py

from constants import artist_tracks

# Create a dictionary to store the count of tracks for each artist
artist_track_count = {}

# Iterate over the artist_tracks dictionary
for artist, tracks in artist_tracks.items():
    # Count the number of tracks for each artist
    track_count = len(tracks)
    # Store the count in the artist_track_count dictionary
    artist_track_count[artist] = track_count

# Print the count of tracks for each artist
for artist, count in artist_track_count.items():
    print(f"{count}")
