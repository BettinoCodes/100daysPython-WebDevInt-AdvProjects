from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json
import time

#NOTES you must authenticate the scopes before using it with this API, this was a tough one whew, should recieve your token in a token.JSON file
#improve: make my searches better if song cant be found, BUT SO FAR IT WORKS!

SPOTIPY_CLIENT_ID='yourid'
SPOTIPY_CLIENT_SECRET='yoursecret'
SPOTIPY_REDIRECT_URI='yourcallback'


user_ans = input("what year you would like to travel to in YYYY-MM-DD format.")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_ans}/")
data = response.text

soup = BeautifulSoup(data, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]


song_artist = soup.select("div ul li ul li span")
song_art = [song.getText().strip()for song in song_artist]


artist = []
for i in range(len(song_art)):
    if i%7 == 0:
        artist.append(song_art[i])

song_by_artist = []
for j in range(len(artist)):
    song_by_artist.append(f"{song_names[j]} {artist[j]}")


list_of_uris = []
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, 
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

for search_song in song_by_artist:
    track_name = search_song
    results = sp.search(q=f'track:{track_name}', limit=1)

    # Extract track URI from the search results
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        print(f"Track URI: {track_uri}")
        list_of_uris.append(track_uri)
    else:
        print(f"No track found with the name '{track_name}'")


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public user-read-email user-read-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.json",
        username="yoursusername", 
    )
)

user_id = sp.current_user()["id"]
print(user_id)


with open('token.json', 'r') as file:
    data = json.load(file)

# Access the value associated with the key "accesstoken"
access_token = data.get("access_token")

print("Access Token:", access_token)


#Endpoint for creating a playlist
url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

# Header with the access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

id_of_playlist = input("What name for your playlist: ")

# Request body
data_playlist = {
    "name": id_of_playlist,
    "public": True,  # Set to False if you want it to be private
    "collaborative": False,  # Set to True if you want it to be collaborative
    "description": "A cool new playlist created via the Spotify API"
}

# Making the POST request
response = requests.post(url, headers=headers, data=json.dumps(data_playlist))

# Checking the response
if response.status_code == 201:
    print("Playlist created successfully!")
    print("Playlist details:", response.json())
else:
    print("Failed to create playlist.")
    print("Status code:", response.status_code)
    print("Response:", response.json())

# #--------------------------------------------------------------------------------------------------------------

playlists = sp.current_user_playlists()
# Print playlist names and IDs
playlist_id = ""

for playlist in playlists['items']:
    if playlist["name"] == id_of_playlist:
       print(f"Playlist ID: {playlist['id']}")
       playlist_id = playlist['id']

print(playlist_id)

url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

for tracks in list_of_uris:
  data_music = {
      "uris": [
          tracks
      ],
      "position": 0
  }

  response = requests.post(url, headers=headers, data=json.dumps(data_music))

  # Print the response from the server
  print(response.status_code)
  print(response.json())

