import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyApi:

    os.environ["SPOTIPY_CLIENT_ID"] = ""
    os.environ["SPOTIPY_CLIENT_SECRET"] = ""
    os.environ["SPOTIPY_REDIRECT_URI"] = ""

    scope = "user-library-read"

    @classmethod
    def save_tracks_list(cls, playlist_url):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=cls.scope))
        track_names = []
        tracks_response = sp.playlist_items(playlist_url)
        for idx, item in enumerate(tracks_response['items']):
            track = item['track']
            track_names.append(track['artists'][0]['name'] + " " + track['name'])
        return track_names
