# Problem Statement

Movie enthusiasts who want to find a film to watch have three questions: what is available in the genre I feel like watching today? Is the movie well rated? What are other movies like that one? Major players in the streaming space address these with complex account-bound systems which have opaque recommendation algorithms. For CS and AI students the value in building a recommendation engine lies in exposing the features and the algorithm used to recommend similar items.

This project is a lightweight self-contained movie recommendation engine that does not require a login or internet connection. It demonstrates the foundational concept of a content-based recommendation engine: representing items by their features and comparing the similarity of these representations.

## Scope
This project includes:

• A console-based application
• A small static in-memory dataset of 50 items
• Three modules implementing genre search, rating lookup, and similar movies recommendation, plus a menu controller
• Case-insensitive title matching with tolerance for extra spaces
This project deliberately excludes:

• Personalization or user accounts
• Production-grade data layer or API
• Graphical or web interface
• Persistent storage
• Trained ML models (recommendations are based on keyword overlap; the ML pipeline is not implemented)
## Who Cares?
Who would benefit from this project?

• Movie lovers who want a light utility to discover movies in a particular genre and get similar movies recommendations
• CS/ML students who want to see an example of a content-based recommendation engine implemented in a clean maintainable way

## Key Features
Features associated with the public MVP:

• Search by the 10+ genres
• Look up ratings of any movie in the database
• Get recommendations for similar movies
• Resilience to invalid inputs and unknown titles
• Modular design with clear separation of concerns for easy extensibility