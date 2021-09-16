import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_page = response.text
soup = bs(empire_page, "html.parser")

def movie_parser():
    movie_list = []
    movies = soup.find_all(class_="listicle-item")
    for movie in movies:
        movie_num = str(101 - int(movie.find(class_="listicle-item-count").getText().split()[0]))
        movie_name = movie.find("img")["alt"]
        movie_list.append(f"{movie_num}) {movie_name}")

    movie_list.reverse()

    with open("movies.txt", mode="w") as file:
        for movie in movie_list:
            file.write(f"{movie}\n")
            
    print("Movies parsed!")

movie_parser()