# Write a function that takes a list of movies and computes the average IMDB score.
from mov_dict import movies

def categorizer(listik):
    suma = 0

    for movik in movies:
        if movik["name"] in listik:
            suma += movik["imdb"]
    
    return suma / len(listik)

print(categorizer(["Dark Knight", "Hitman"]))
print(categorizer(["The Help", "Love"]))