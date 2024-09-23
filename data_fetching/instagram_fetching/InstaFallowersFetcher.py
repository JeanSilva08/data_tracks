import instaloader
import csv


def fetch_instagram_followers(artist_usernames):
    loader = instaloader.Instaloader()

    loader.load_session_from_file('avlis_seraos')
    if not loader.context.is_logged_in:
        loader.context.login('avlis_seraos', 'swordfish08')

    data = []

    for username in artist_usernames:
        try:

            profile = instaloader.Profile.from_username(loader.context, username)

            followers_count = profile.followers

            data.append([followers_count])
        except Exception as e:

            print(f"Error fetching followers for {username}: {e}")

    return data


artist_usernames = [
    'mainstreet',
    'orochi',
    'pozevidalouca',
    'souobin',
    'borges.clout',
    'chefinoficial',
    'oruam',
    'bielzin',
    'dfideliz',
    'plquest_',
    'raffe.og',
    'azevedo',
    'levianinn',
    'ajaxxprod',
    'kaiquekizzy',
    'jessbeats',
    'beatdoruxn',
    'mccabelinho',
    'brutosb13',
    'a.rb13',
    'vinicinb.13',
    'maano_r7',
    'amorimb13',
    'buddy021_',
    'mvkoficiaal',
    'vzpedrin',
    'filhaof2',
    'shenlongmc',
    'degenog',
    'hashibxd',
    'benyfreee',
    'feek7._',
    'oliveira09ne',
    'piorversaodemim',
    'oreozin7',
    'peziinho_',
    'grone.40',
    'vtnobeat'
]

followers_data = fetch_instagram_followers(artist_usernames)

with open('insta_followers.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Followers Count'])
    csv_writer.writerows(followers_data)

print("Data has been written to insta_followers.csv file.")
