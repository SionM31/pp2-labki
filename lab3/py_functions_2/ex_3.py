# Write a function that takes a category name and returns just those movies under that category.
from mov_dict import movies

def categorizer(categorik):
    movie_list = []
    for movik in movies:
        if(movik["category"] == categorik):
            movie_list.append(movik["name"])
    
    return movie_list

print(categorizer("Romance"))
print(categorizer("Suspense"))