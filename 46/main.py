import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

def time_machine():
    song_list = []
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    soup = bs(response.text, "html.parser")
    topSongs = soup.find_all(class_="chart-list__element")
    
    for song in topSongs:
        song_name = song.find(class_="chart-element__information__song").getText()
        song_artist = song.find(class_="chart-element__information__artist").getText()
        fullSong = f"'{song_name}'' by {song_artist}"
        song_list.append(fullSong)
    print(song_list)

# time_machine()
