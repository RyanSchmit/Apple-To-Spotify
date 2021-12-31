import spotipy
from spotipy.oauth2 import SpotifyOAuth

#authenticates with spotify
scope = 'playlist-modify-public'
username = ''
token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)
 
 #get user input
playlistName = input("Playlist name: ")
playlistDescription = input("Playlist description: ")

#connects to api
spotifyObject.user_playlist_create(user=username,name=playlistName,public=True,description=playlistDescription)