# Spotify Playlist Curation Manager

Simple Automatic Playlist Updater For Curating Big Playlists

This Python script allows you to manage your Spotify playlists by reading track links from a `song_links.txt` file, removing all existing songs in a specified playlist, and adding new songs from the list. Ideal for curating new weekly everchanging playlists based on simple text input.

## Features:
- Automatically removes all tracks from an existing playlist and replaces them with new ones.

**(Planning to add more features and make it a good curation tool in the future)**

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository
   ```bash
   git clone https://github.com/tabibyte/spotify-playlist-manager.git
   cd spotify-playlist-manager

2. Install dependencies
   ```bash
   pip install -r requirements.txt

3. Open the '.env' file and add the spotify credentials and playlist you want to work with
   ```bash
   SPOTIPY_CLIENT_ID=spotify_client_id
   SPOTIPY_CLIENT_SECRET=spotify_client_secret
   SPOTIPY_REDIRECT_URI=http://localhost:8888/callback/
   PLAYLIST_ID=your_playlist_id
 (You can change the redirect URI if you want to use custom port)

 (For playlist ID, copy the link of the playlist and get the bold part:
 <br> e.g: open.spotify.com/playlist/ **37i9dQZEVXbMDoHDwVN2tF** ?si=2edb3fc3215a4074 </br>
 
## Usage

1. Ensure you have added your Spotify credentials and playlist ID to the `.env` file and installed requirements correctly

2. Add Track links to 'track_links.txt'

3. Run
   ```bash
   python spotify_playlist_manager.py

The script will:

- Read the links from 'track_links.txt'.
- Extract the track IDs.
- Remove the existing tracks from the specified playlist.
- Add the new tracks to the playlist.

## Contributing

Contributions are always welcome:

1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
