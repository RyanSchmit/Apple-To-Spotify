import spotipy
from spotipy.oauth2 import SpotifyOAuth

#authentication
scope = 'playlist-modify-public'
username = 'ryansrts'
token = SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)
 
#insert arrray of songs here  
countryPlaylist = ['Gods Country Blake Shelton', 'Chicken Fried Zac Brown Band', 'Ramblin Man The Allman Brothers Band', 'Rocky Mountain High John Denver', 'Sweet Home Alabama Lynyrd Skynyrd', 'Take Me Home, Country Roads... John Denver', 'Humble and Kind Tim McGraw', 'Undivided Tim McGraw & Tyler Hubbard', 'Gone Dierks Bentley', 'Buy Dirt', 'I Quit Drinking Kelsea Ballerini & LANY', 'We Didnt Have Much Justin Moore', 'Villain Lily Rose', 'Better Than Youre Used To Tyler Rich', 'Memory Kane Brown x blackbear', 'Nobodys More Country Blanco Brown', 'Truth About You Mitchell Tenpenny', 'Til You Cant Cody Johnson', 'Summer Job Money Chris Lane', 'Cold Beer Calling My Name Jameson Rodgers & Luke Combs', 'Same Boat Brown Band', 'half of my hometown (feat. Ke... Kelsea Ballerini', 'Hang On to That Charlie Worsham', 'Different Round Here Riley Green']
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