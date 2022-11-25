from spotifyapi.SpotifyApiMethods import SpotifyApi
from ytapi.YoutubeApiMethods import YoutubeApiMethods


class Run:

    @staticmethod
    def download_tracks_from_spotify_playlist(playlist_url):
        track_list = SpotifyApi.save_tracks_list(playlist_url)
        for track in track_list:
            YoutubeApiMethods.download_music(track)
