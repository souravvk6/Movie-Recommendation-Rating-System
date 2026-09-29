

\# Movie Recommendation Program



A modular, menu-driven console-based Python application for genre search, movie rating, and content-based similar movie recommendation.



\## Description



Choosing what to watch is a hard task, especially when numerous streaming services offer thousands of movies and television shows. While modern platforms utilize sophisticated recommender systems to suggest the most relevant content to the user, such systems remain proprietary and complex. This project contains an implementation of a simplified movie recommendation system that runs locally in the console and has no internet connection. The user can search for movies by genre, find the rating of a particular movie, and request similar movies based on thematic keywords. The code is organized into separate modules for each part of the system, and all data is contained within a preloaded dataset of 50 movies.



\## Features



\### Core Features



\- 10 genres search: Action, Romance, Comedy, Sci-Fi, Fantasy, Thriller, Horror, Drama, Animation, Mystery



\- Movie rating lookup by title: Case-insensitive and whitespace-insensitive



\- Similar movies recommendation based on thematic tags: No similar movie includes the input one



\- Customized error messages: No errors raised if not found or if wrong menu option chosen



\- Modular structure: Every major part of the program is separated into individual modules and files



\### Technologies / Tools



\- Python 3: Only the standard library is used; no external packages are included



\- Git: Version control system



\## How the Program is Structured



movie-recommendation-program/



├── mainprogram.py # Main module with the menu and core logic



├── movie\_database.py # Movie database with 50 entries for test purposes



├── movie\_finder.py # Module 1: Movie finder by genre



├── movie\_rating.py # Module 2: Movie rating lookup



├── movie\_similar.py # Module 3: Similar movie recommender



├── README.md



└── statement.md



\## How to Set Up



These instructions describe how to set up and run the program on a local machine.



\### Prerequisites



Make sure that Python 3 is installed on your system:



&#x09;python3 --version



\### Installation



Install the program by cloning the repository:



&#x09;git clone <https://github.com/souravvk6/Movie-Recommendation-Rating-System>



&#x09;cd movie-recommendation-program



Then, run the following command:



&#x09;python3 mainprogram.py



Once the program starts, follow the on-screen prompts to select an option and run the program.



\## How to Test



This program can be tested by running it in a local Python environment. The following steps describe how to perform basic tests:



1\. Run the program by typing python3 mainprogram.py in the terminal



2\. Test genre finder: type 1 and press Enter, then type a number 1–10 and press Enter again to see the movies in the selected genre



3\. Test movie rating: type 2 and press Enter, then type the name of the movie and press Enter again to see its rating



4\. Test similar movie recommender: type 3 and press Enter, then type the name of the movie and press Enter again to see similar movies



5\. Test invalid input: at the main menu, type a number 1–4 to select an option, then type any input other than numbers 1–4 to see the error message.



6\. Test exit: type 4 and press Enter to exit the program



If all tests are successful, the program will print a message saying Thank You for using the Movie Recommender System!





