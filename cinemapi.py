import os
import json

folder_path = input("Enter folder path (ex. /home/user/Cinema): ")
api_url = input("Enter api url (ex. https://api.example.org): ")
id = 0
movies = []
for file in os.walk(folder_path):
    items = file[2]
    for item in items:
        if item.endswith('.mp4'):
            movie_path = file[0]+"/"+item
            movie_url = movie_path.replace(folder_path, api_url)
            movie = {"id": id, "name": item, "movie_path": movie_path, "movie_url": movie_url}
            movies.append(movie)
            id = id+1
f = open(folder_path+"/"+"index.html", "w")
f.write(json.dumps(movies))
f.close()
