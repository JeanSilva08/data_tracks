import csv

# Define the file paths
file1 = 'monthly_listeners.csv'
file2 = 'monthly_listeners_charts.csv'
output_file = 'rank_monthly_listeners.csv'

# Function to read CSV and return a dictionary of artist and playcount
def read_csv(file_path):
    artist_playcount = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) >= 2:  # Ensuring the row has at least 2 elements
                artist = row[0].strip()
                playcount = row[2].strip().replace(',', '').replace('"', '')
                try:
                    playcount = int(playcount)
                    artist_playcount[artist] = playcount
                except ValueError:
                    continue  # Skip rows with invalid playcount
    return artist_playcount

# Read both CSV files
playcount_data = read_csv(file1)
playcount_charts_data = read_csv(file2)

# Combine the dictionaries
combined_data = {**playcount_data, **playcount_charts_data}

# Sort the artists by playcount in descending order
ranked_artists = sorted(combined_data.items(), key=lambda x: x[1], reverse=True)

# Print the full ranked list of artists
print("Full Ranked Artists List:")
for rank, (artist, playcount) in enumerate(ranked_artists, start=1):
    print(f"{rank}. {artist} - {playcount}")

# Filter to include only artists from playcount.csv for the CSV output, maintaining the original rank
filtered_ranked_artists = [(artist, rank) for rank, (artist, playcount) in enumerate(ranked_artists, start=1) if artist in playcount_data]

# Write the filtered ranked artists to a new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Artist', 'Rank'])
    for artist, rank in filtered_ranked_artists:
        writer.writerow([artist, rank])
