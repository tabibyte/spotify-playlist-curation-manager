import os
import re
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Loading enviromental variables
load_dotenv()

CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

SCOPE = "playlist-modify-public playlist-modify-private"

# Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Loading track links from song_links.txt
def get_track_ids_from_file(filename):
    track_ids = []
    with open(filename, 'r') as file:
        for line in file:
            track_url = line.strip()
            match = re.search(r"track/([a-zA-Z0-9]+)", track_url)
            if match:
                track_ids.append(match.group(1))
    return track_ids

file_path = 'spotify_playlist_updater\song_links.txt'

new_tracks = get_track_ids_from_file(file_path)

# Getting the ID from track links
track_uris = [f'spotify:track:{track_id}' for track_id in new_tracks]

playlist_id = os.getenv('PLAYLIST_ID')

# Removing old tracks
current_tracks = sp.playlist_tracks(playlist_id)
track_uris_to_remove = [item['track']['uri'] for item in current_tracks['items']]

if track_uris_to_remove:
    sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris_to_remove)
    print(f"Removed {len(track_uris_to_remove)} tracks from the playlist.")

# Adding new ones
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
    print(f"Added {len(track_uris)} new tracks to the playlist.")
