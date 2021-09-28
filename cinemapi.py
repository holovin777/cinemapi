import os
import json
import wikipedia

folder_path = input("Enter folder path (ex. /home/user/Cinema): ")
api_url = input("Enter api url (ex. https://api.example.org): ")
lang = input("Cinema language (ex. en, fr, it): ")

id = 0
movies = []
for file in os.walk(folder_path):
    items = file[2]
    for item in items:
        if item.endswith('.mp4'):
            name = file[0].replace(folder_path + "/", "")
            movie_path = file[0]+"/"+item
            movie_url = movie_path.replace(folder_path, api_url)
            wikipedia.set_lang(lang)
            summary = wikipedia.summary(name)
            page = wikipedia.page(name)
            plot = page.section("Trama")
            movie = { "id": id, "name": name, "movie_path": movie_path, "movie_url": movie_url, "summary": summary, "plot": plot }
            movies.append(movie)
            id = id+1
f = open(folder_path+"/"+"index.html", "w")
f.write(json.dumps(movies))
f.close()
