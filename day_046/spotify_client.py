import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
USER_NAME = os.environ.get('SPOTIPY_USER_NAME')


class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="http://example.com",
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                show_dialog=True,
                cache_path="token.txt",
                username=USER_NAME
            )
        )

        self.user_id = self.sp.current_user()["id"]

    def create_playlist(self, song_names, date):
        song_uris = []
        year = date.split("-")[0]
        for song in song_names:
            result = self.sp.search(q=f"track:{song} year:{year}", type="track")
            print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")

        playlist = self.sp.user_playlist_create(user=self.user_id, name=f"{date} Billboard 100", public=False)

        self.sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

        return playlist["id"]
