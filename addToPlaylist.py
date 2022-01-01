import spotipy
from spotipy.oauth2 import SpotifyOAuth

#authentication
scope = 'playlist-modify-public'
username = ''
token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)
 
#insert arrray of songs here  
countryPlaylist = []
list_of_songs = []

#looks for each song in the array
for x in countryPlaylist:
    result = spotifyObject.search(q=x)
    print(x)
    list_of_songs.append(result['tracks']['items'][0]['uri'])

#puts songs into the top playlist on your account
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)