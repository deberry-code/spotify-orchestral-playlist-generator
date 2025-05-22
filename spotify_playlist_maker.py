import requests
import base64
import random
from dotenv import load_dotenv
import os

load_dotenv()

# Spotify API credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Encode client ID and secret
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Get access token
auth_url = "https://accounts.spotify.com/api/token"
auth_headers = {
    "Authorization": f"Basic {b64_auth_str}",
}
auth_data = {
    "grant_type": "client_credentials",
}

try:
    response = requests.post(auth_url, headers=auth_headers, data=auth_data)
    response_data = response.json()
    access_token = response_data.get("access_token")
    if not access_token:
        print("Failed to get access token. Response:", response_data)
        exit()
    print("Successfully obtained access token\n")
except Exception as e:
    print(f"Error parsing auth response: {e}")
    exit()

# Headers for subsequent API calls
api_headers = {
    "Authorization": f"Bearer {access_token}",
}

# Recommendation and audio analysis endpoints
api_url = 'https://api.spotify.com/v1/recommendations'
trackanalysis_url = 'https://api.spotify.com/v1/audio-features'

# Heroic tracks
heroic_songs = [
    '08QaHlMPWuO5PUxjl61bXn',  # Klaus Badelt - He's a Pirate
    '6N10tJfiQqm4wn6KM70aoT',  # Hans Zimmer - Up is Down
    '35gFlKdC4Pmo88Go1cVrae',  # Klaus Badelt - The Medallion Calls
    '775OxWq9wfVzmVDS0n3zff',  # Alexandre Desplat - Statues (HP 8)
    '4u4VElxO7JM4IR4jR4TL1s',  # Steve Jablonsky - Arrival to Earth
    '6hjSRFrfbq6XtHeQuW38qd',  # British Grenadiers
    '6xez71zpAqQ6N5i8E1jHlD',  # Carl Orff — O Fortuna
    '2JJNV1Kwrcj28NhYX69b46',  # Two Steps from Hell — Heart of Courage
    '518WEa0aINvgdjdLkMnnoh',  # Carl Orff — Fortune plango vulnera
    '3Od7kFjADlVPtvVqxASS5C'   # Berlioz - Rakoczy March
]

# Lively tracks
lively_songs = [
    '289nG8bnslnizI3aAa3npM',  # Tchaikovsky - La Fee (Sleeping Beauty)
    '6MzJZx1c74T5Vp6FE3ny0X',  # Tchaikovsky - Princess Florine
    '289nG8bnslnizI3aAa3npM',  # Tchaikovsky - Canari qui chante
    '7hTnnY0wysFgebsmF0FPvx',  # Tchaikovsky - Silver Fairy
    '4KLVPRo0f6XUJa4t4dnRW6',  # Mozart - Eine Kleine Nachtmusik
    '1I9MOstMVcWANW8Hj3JOQW',  # Hans Zimmer — Two Hornpipes (Tortuga!)
    '69f4oU2GWDWVNbLgd34xle',  # Fille Mal Gardee - Pas de March
    '33xx3BaaO1PZeASUDIbzys',  # Delibes — Sylvia Pizzicati
    '5rkLjDhH4dPV4gIABENKzm',  # Kitri's Wedding Variation
    '3m3sGx5h2FG461vLt0WYzV'   # Delibes — Coppelia Valse Lente
]

# Sentimental tracks
sentimental_songs = [
    '0Ee9oam0N0ZzxZSN9nogTQ',  # Ravel - Antar
    '07eYxFCtC3UzWA8XUD4XkZ',  # Tchaikovsky - Sugarplum Pas de Deux
    '2pCLg7o60iAnNEbYDW9Lhy',  # Bizet - Habanera (Instrumental)
    '775OxWq9wfVzmVDS0n3zff',  # Alexandre Desplat — Lily's Theme
    '582kxTHjj7jzMzsOxgrWfH',  # Delibes — Flower Duet (Instrumental)
    '1Ke4gVLpNH2FB8DoyfKU1D',  # Saint-Saëns — The Swan
    '0Z973O9nqc2I6G0mGB4bM7',  # Spartacus Adagio
    '6WbiLUdYqdtaRVskHDFLdp',  # Thaïs Meditation - Massenet
    '4AObypFcQnRns1AzgSOlOI',  # Nino Rota — Love Theme (Romeo & Juliet)
    '3Ii2KG3YLrC0KNbuJKAFj2'   # Love Theme from The Godfather
]

# Dark tracks
dark_songs = [
    '19fi3jLiGLhR6AbtfGwize',  # Lyubomudrov - The Spider Knows His Craft
    '1Aozvs1CIdllsgoCK5mrSC',  # Grieg - Anitra's Dance
    '1OuCn2F9BmyTAdM0Jylo9X',  # Wednesday Addams - Paint It Black
    '5cVHRNV1KfOkDP7Ql6nGXe',  # Adam Hurst - Dusk
    '6OIo4vJRXwIWyf41JDh1H3',  # Yoko Shimomura - Fragments of Sorrow
    '6E0AIIq5p8MZCrHf4w64ko',  # Hiroyuki Sawano - Vogel im Kafig
    '1lfKd4rk1FjLz0OE0NNKJv',  # Adam Hurst - Four Winds
    '6buHoQU9OTdbJrAuniVwGL',  # Hans Zimmer - Davy Jones
    '2LiWNkeUOAeibGxJKxmjsD'   # Prokofiev - Dance of the Knights
]


def makeplaylist(mood):
    params = {
        'limit': 100,
        'seed_genres': 'classical,soundtrack',
    }

    if mood == "heroic":
        seed = random.choice(heroic_songs)
        params.update({
            'min_tempo': 50,
            'seed_tracks': seed,
            'max_speechiness': 0.33,
        })
    elif mood == 'lively':
        seed = random.choice(lively_songs)
        params.update({
            'energy': 0.8,
            'min_tempo': 80,
            'valence': 0.8,
            'seed_tracks': seed,
            'target_mode': 0,
            'max_speechiness': 0.33,
        })
    elif mood == 'sentimental':
        seed = random.choice(sentimental_songs)
        params.update({
            'min_tempo': 60,
            'valence': 0.6,
            'max_speechiness': 0.33,
            'seed_tracks': seed,
        })
    elif mood == 'dark':
        seed = random.choice(dark_songs)
        params.update({
            'min_tempo': 50,
            'target_mode': 0,
            'seed_tracks': seed,
            'max_speechiness': 0.2,
        })
    else:
        print("Unknown mood:", mood)
        return

    print(f"Using seed track: https://open.spotify.com/track/{seed}\n")

    response = requests.get(api_url, headers=api_headers, params=params)
    data = response.json()

    if 'tracks' not in data:
        print("No tracks returned.")
        return

    tracks = data['tracks']
    sample = random.sample(tracks, min(15, len(tracks)))

    print(f"Generated {mood.capitalize()} Playlist:\n")
    for j, i in enumerate(sample, start=1):
        print(f"{j}. {i['name']} by {i['artists'][0]['name']}")
        print(i['external_urls']['spotify'])
        print()


def analyzetrack(track_id):
    analysis_response = requests.get(f'{trackanalysis_url}/{track_id}', headers=api_headers)
    print(analysis_response.json())


# Example usage
makeplaylist('heroic')