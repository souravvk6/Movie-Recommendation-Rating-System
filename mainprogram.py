
import movie_rating
import movie_similar
import movie_finder


while True:
    print("\n\n----MOVIE RECOMMENDATION PROGRAM----")
    
    
    print("1.Search movie list")
    print("2.Movie Rating")
    print("3.Recommend similar movies")
    print("4.Exit")

    choice=int(input("\nEnter your choice : "))

    if choice==1:
        print("\nMOVIE SEARCH")
        print("\n1.Action")
        print("2.Romance")
        print("3.Comedy")
        print("4.Sci-Fi")
        print("5.Fantasy")
        print("6.Thriller")
        print("7.Horror")
        print("8.Drama")
        print("9.Animation")
        print("10.Mystery")

        search=input("\n\nEnter (1-10):")
        print("\n")
        
        movie_finder.movie_finder(search)
            
        
        input("\nPress Enter To Reset Program...")

    elif choice==2:
    
        x=movie_rating.movie_rating()
    
        if x==True:
            True
        else:
            print("\nThe Movie is not in our database.")
        
            input("\nPress Enter To Reset Program...")
        
    elif choice==3:
        
        movie_similar.similar_movies()
        
        input("\nPress Enter To Reset Program...")
    
    elif choice==4:
        
        print("\nThank You for Using The Program!")
        
        break
    else:
        print("Invalid Choice!")
        input("\nPress Enter to Reset Program")