import requests
from bs4 import BeautifulSoup as bs

def time_machine():
    song_list = []
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
    spotify_page = response.text
    soup = bs(spotify_page, "html.parser")
    topSongs = soup.find_all(class_="chart-list__element")
    for song in topSongs:
        song_name = song.find(class_="chart-element__information__song").getText()
        song_artist = song.find(class_="chart-element__information__artist").getText()
        fullSong = f"'{song_name}'' by {song_artist}"
        song_list.append(fullSong)
    print(song_list)


time_machine()