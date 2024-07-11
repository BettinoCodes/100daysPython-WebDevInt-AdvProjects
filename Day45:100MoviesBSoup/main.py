import requests
from bs4 import BeautifulSoup
from pprint import pprint
import codecs

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
data = response.text

#pprint(data)

soup = BeautifulSoup(data, "html.parser")
movies = soup.find_all(name="h3", class_="title")

with open("top100movies", mode="w") as file:
        for i in range(len(movies)-1, -1, -1):
            text_ = movies[i].getText()
            encoded_string = codecs.utf_8_encode(text_)[0]
            file.write(f"{encoded_string}\n")

movie_dictionary = []
for j in range(len(movies)-1, -1, -1):
    text_ = movies[j].getText()
    i = 0
    number = ""
    movie_name = ""
    while(text_[i] != ")" and text_[i] != ":"):
        number += text_[i]
        i += 1
    i += 2
    while(i < len(text_)):
        movie_name += text_[i]
        i += 1

    movie_dictionary.append({int(number), movie_name})

pprint(movie_dictionary)
