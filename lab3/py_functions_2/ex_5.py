# Write a function that takes a category and computes the average IMDB score.
from mov_dict import movies

def categorizer(categorik):
    suma, counter = 0, 0

    for movik in movies:
        if movik["category"] == categorik:
            suma += movik["imdb"]
            counter += 1
    
    return suma / counter

print(categorizer("Romance"))
print(categorizer("Drama"))