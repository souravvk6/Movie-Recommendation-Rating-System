import movie_database

def movie_finder(search):
        if int(search)==1:
            for i in movie_database.movies:
                if "Action" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==2:
            for i in movie_database.movies:
                if "Romance" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==3:
            for i in movie_database.movies:
                if "Comedy" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==4:
            for i in movie_database.movies:
                if "Sci-Fi" in i["genre"]:
                    print(i["title"])


        elif int(search)==5:
            for i in movie_database.movies:
                if "Fantasy" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==6:
            for i in movie_database.movies:
                if "Thriller" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==7:
            for i in movie_database.movies:
                if "Horror" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==8:
            for i in movie_database.movies:
                if "Drama" in i["genre"]:
                    print(i["title"])
                
        elif int(search)==9:
            for i in movie_database.movies:
                if "Animation"in i["genre"]:
                    print(i["title"])
    
        elif int(search)==10:
            for i in movie_database.movies:
                if "Mystery"in i["genre"]:
                    print(i["title"])
    
        else:
            print("invalid choice, enter a number from 1-10")