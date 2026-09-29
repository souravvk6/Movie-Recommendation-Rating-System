import movie_database
def movie_rating():
    
    print("\n---------MOVIE RATINGS---------")

    movname=input("\n\nEnter movie name:")

    for i in movie_database.movies:
        if movname.lower().strip()==i["title"].lower().strip():
            print("\nThe rating of this movie is:",i["rating"])
            return True
        


        
    





