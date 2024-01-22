# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
from mov_dict import movies

def abover(movie):
    for movik in movies:
        if(movik["name"] == movie and movik["imdb"] > 5.5):
            return True
    return False

print(abover("Hitman"))
print(abover("Bride Wars"))