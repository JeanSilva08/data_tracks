import csv
import os

# Define the base directory and file paths
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))
file1 = os.path.join(base_dir, 'playcount.csv')
file2 = os.path.join(base_dir, 'playcount_charts.csv')
output_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'rank_playcount.csv'))


# Function to read CSV and return a dictionary of artist and playcount
def read_csv(file_path):
    artist_playcount = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if len(row) == 2:  # Ensuring the row has exactly 2 elements
                artist, playcount = row
                playcount = int(playcount)
                artist_playcount[artist] = playcount
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

# Desired order of artists
desired_order = [
    "Mainstreet", "Orochi", "Poze", "Bin", "Borges", "Chefin", "Oruam", "Bielzin",
    "Dfideliz", "PL Quest", "Raffe", "Azevedo", "Leviano", "Ajaxx", "Kizzy",
    "jess beat", "RUXN", "MC Cabelinho", "Brutos", "A.R", "Vinicin", "Mano R7",
    "Amorim", "Budy", "MVK", "Pedrin", "Filhão", "Shenlong", "DEGE", "Hashi",
    "Benny", "Feek", "Oliveira", "Pior versão de mim", "Oreozin", "Peziinho",
    "Grone", "VT no Beat"
]

# Filter to include only artists from playcount.csv and maintain the desired order
filtered_ranked_artists = [(artist, rank) for artist in desired_order for rank, (a, playcount) in
                           enumerate(ranked_artists, start=1) if artist == a]

# Write the filtered ranked artists to a new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank'])
    for artist, rank in filtered_ranked_artists:
        writer.writerow([rank])

print(f"Output written to {output_file}")
