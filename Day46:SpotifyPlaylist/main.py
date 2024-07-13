#IN PROGRESS
from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import json


SPOTIPY_CLIENT_ID='yours'
SPOTIPY_CLIENT_SECRET='yours'
SPOTIPY_REDIRECT_URI='http://localhost:8080/callback'


# user_ans = input("what year you would like to travel to in YYYY-MM-DD format.")
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_ans}/")
# data = response.text

# soup = BeautifulSoup(data, "html.parser")

# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]


# song_artist = soup.select("div ul li ul li span")
# song_art = [song.getText().strip()for song in song_artist]


# artist = []
# for i in range(len(song_art)):
#     if i%7 == 0:
#         artist.append(song_art[i])

# song_by_artist = []
# for j in range(len(artist)):
#     song_by_artist.append(f"{song_names[j]} {artist[j]}")

#example for data
song_by_artist = [
    "I'm Real Jennifer Lopez Featuring Ja Rule", "Fallin' Alicia Keys", 'Where The Party At Jagged Edge With Nelly', 
                  'Someone To Call My Lover Janet', "Hit 'Em Up Style (Oops!) Blu Cantrell", 'U Remind Me Usher', 
                  'Let Me Blow Ya Mind Eve Featuring Gwen Stefani', "It's Been Awhile Staind", 'Drops Of Jupiter (Tell Me) Train', 
                  'Hanging By A Moment Lifehouse', 'You Rock My World Michael Jackson', 'Family Affair Mary J. Blige', 'Izzo (H.O.V.A.) JAY-Z', 
                  'Peaches & Cream 112', 'Because I Got High Afroman', 'One Minute Man Missy "Misdemeanor" Elliott', 'Fill Me In Craig David', 
                  "When It's Over Sugar Ray", 'All Or Nothing O-Town', 'Drive Incubus', 'Austin Blake Shelton', 'Differences Ginuwine', 
                  "I'm A Thug Trick Daddy", 'The Space Between Dave Matthews Band', "I'm A Believer Smash Mouth",
                    'Contagious The Isley Brothers Featuring Ronald Isley', "I'm Just Talkin' About Tonight Toby Keith", 
                    'What Would You Do? City High', 'Area Codes Ludacris Featuring Nate Dogg', 'Only Time Enya', 
                    'What I Really Meant To Say Cyndi Thomson', 'Follow Me Uncle Kracker', 'Start The Commotion The Wiseguys', 
                    'I Wanna Be Bad Willa Ford', 'Bad Boy For Life P. Diddy, Black Rob & Mark Curry', "Can't Deny It Fabolous Featuring Nate Dogg",
                      'Where The Blacktop Ends Keith Urban', 'Angry All The Time Tim McGraw', 'Turn Off The Light Nelly Furtado', 
                      "Livin' It Up Ja Rule Featuring Case", 'Be Like That 3 Doors Down', 'Only In America Brooks & Dunn', 
                      'Everywhere Michelle Branch', 'Thank You Dido', 'Rock The Boat Aaliyah', "I Would've Loved You Anyway Trisha Yearwood", 
                      'Every Other Time LFO', "I'm Already There Lonestar", 'Where I Come From Alan Jackson', "Bootylicious Destiny's Child", 
                      "Here's To The Night Eve 6", 'Smooth Criminal Alien Ant Farm', 'Flavor Of The Weak American Hi-Fi', 'I Do!! Toya', 
                      'Ugly Bubba Sparxxx', "When I Think About Angels Jamie O'Neal", "Feelin' On Yo Booty R. Kelly", 
                      'Six-Pack Summer Phil Vassar', "Superman (It's Not Easy) Five For Fighting", 'Raise Up Petey Pablo', 
                      'Irresistible Jessica Simpson', 'Purple Hills D12', 'Clint Eastwood Gorillaz', 'How You Remind Me Nickelback', 
                      'So Complicated Carolyn Dawn Johnson', 'Lifetime Maxwell', 'Just In Case Jaheim', 'Bad Day Fuel',
                        "When God-Fearin' Women Get The Blues Martina McBride", 'Schism Tool', "There You'll Be Faith Hill", 
                        'On A Night Like This Trick Pony', 'Dance With Me 112', 'Love Of My Life Brian McKnight', 'Set It Off Juvenile', 
                        'Love Of A Woman Travis Tritt', 'Fat Lip Sum 41', "I'll Fly With You (L'amour Toujours) Gigi D'Agostino", 
                        'What It Is Violator Featuring Busta Rhymes', 'More Than That Backstreet Boys', "I'm A Survivor Reba", 
                        'Music Erick Sermon Featuring Marvin Gaye', 'The Way Jill Scott', 'Downtime Jo Dee Messina', 
                        'AM To PM Christina Milian', 'This Is Me Dream', 'Crawling Linkin Park', "She's All I Got Jimmy Cozier", 
                        'Loverboy Mariah Carey Featuring Cameo', 'Take You Out Luther Vandross', 'My Projects Coo Coo Cal', 
                        'Sandstorm Darude', 'Laredo Chris Cagle', 'Girl Next Door Musiq Soulchild Featuring Ayana', 
                        "Wait A Minute Ray J Featuring Lil' Kim", 'Castles In The Sky Ian Van Dahl Featuring Marsha', 
                        "Can't Believe Faith Evans Featuring Carl Thomas", 'While You Loved Me Rascal Flatts', 'Mad Season matchbox twenty', 
                        'The Rock Show blink-182'
                    ]

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)


# scope = 'user-read-private user-read-email'


# sp_oauth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="http://localhost:8080/callback", scope=scope)
# auth_url = sp_oauth.get_authorize_url()
# print(auth_url)

# url = "https://accounts.spotify.com/api/token"

# # Headers for the request
# headers_token = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# # Data for the request
# data = {
#     "grant_type": "client_credentials",
#     "client_id": SPOTIPY_CLIENT_ID,
#     "client_secret": SPOTIPY_CLIENT_SECRET
# }

# # Making the POST request
# response = requests.post(url, headers=headers_token, data=data)


# token_info = response.json()
# access_token = token_info['access_token']
# print(access_token)

# #------------------------------------------playlist------------------------------------------------------------------

# url = 'https://api.spotify.com/v1/users/{user_id}/playlists'

# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json'
# }

# data = {
#     "name": "New Playlist Time",
#     "description": "New playlist description",
#     "public": False
# }

# response = requests.post(url, headers=headers, data=json.dumps(data))

# # Print the response from the server
# print(response.status_code)
# print(response.json())

#----------------------------------------------------------------------------------------------------------------------

# client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, 
#                                                       client_secret=SPOTIPY_CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# for search_song in song_by_artist:
#     track_name = search_song
#     results = sp.search(q=f'track:{track_name}', limit=1)

#     # Extract track URL from the search results
#     if results['tracks']['items']:
#         track_url = results['tracks']['items'][0]['external_urls']['spotify']
#         print(f"Track URL: {track_url}")
#         url_playlist = 'https://api.spotify.com/v1/playlists/NewPlaylist/tracks'
#         headers = {
#             'Authorization': f'Bearer {access_token}',
#             'Content-Type': 'application/json'
#         }

#         data = {
#             "uris": [
#                 "string"  # Replace "string" with actual track URI(s)
#             ],
#             "position": 0
#         }

#         response = requests.post(url, headers=headers, data=json.dumps(data))

#         # Print the response from the server
#         print(response.status_code)
#         print(response.json())
#     else:
#         print(f"No track found with the name '{track_name}'")
#------------------------------USER ID---------------------------------------------------------------------------------
#getting the id for the playlist
# headers_user_id = {
#     'Authorization': f'Bearer {access_token}'
# }

# response = requests.get('https://api.spotify.com/v1/me', headers=headers_user_id)


# if response.status_code == 200:
#     user_data = response.json()
#     print(f"user data: {user_data}")
# else:
#     print(f"Request failed with status code {response.status_code}: {response.text}")



