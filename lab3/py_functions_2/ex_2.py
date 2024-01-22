# Write a function that returns a sublist of movies with an IMDB score above 5.5.
from mov_dict import movies

def l_abover():
    movie_list = []
    for movik in movies:
        if(movik["imdb"] > 5.5):
            movie_list.append(movik["name"])
    
    return movie_list

[print(movik) for movik in l_abover()]