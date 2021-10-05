import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import lxml

year = input("what year you would like to travel to in YYYY-MM-DD format: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
web_html = response.text
soup = BeautifulSoup(web_html, "lxml")
song_titles = []
titles = soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary")
for title in titles:
    song_titles.append(title.string)

song_uri = []


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="",
                                               client_secret="",
                                               redirect_uri="https://example.com/callback/",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path=".cache"
                                               ))

for song in song_titles:
    results = sp.search(q=f"track:{song}", type="track")
    try:
        song_uri.append(results["tracks"]["items"][0]["id"])
    except IndexError:
        pass

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100")
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uri)
