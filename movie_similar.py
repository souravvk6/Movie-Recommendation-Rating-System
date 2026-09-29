import movie_database


def similar_movies():
    def keyword_movie():
        print("\n-------SIMILAR MOVIE FINDER--------")
        mov = input("\nEnter a movie:").lower().strip()

        for movie in movie_database.movies:
            if movie["title"].lower().strip() == mov:
                print("\nMovies similar to", movie["title"], "are:\n")
                return movie["keywords"], movie["title"]

        print("Movie not found in database.")
        return None, None

    def similar_movie_finder(keywords, title):
        found_any = False
        for movie in movie_database.movies:
            if movie["title"].lower().strip() == title.lower().strip():
                continue  
            for keyword in movie["keywords"]:
                if keyword in keywords:
                    print(movie["title"])
                    found_any = True
                    break

        if not found_any:
            print("No similar movies found.")

    keywords, title = keyword_movie()

    if keywords is None:
        return  

    similar_movie_finder(keywords, title)
   








