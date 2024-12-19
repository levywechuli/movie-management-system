from models.movie import Movie
from models.genre import Genre
from models.base import Session

def movie_menu():
    session = Session()
    
    while True:
        print("\nMovie Management")
        print("1. Add a Movie")
        print("2. Delete a Movie")
        print("3. View All Movies")
        print("4. Find Movie by ID")
        print("5. View Movies by Genre")
        print("6. Back to Main Menu")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            add_movie(session)
        elif choice == "2":
            delete_movie(session)
        elif choice == "3":
            view_all_movies(session)
        elif choice == "4":
            find_movie_by_id(session)
        elif choice == "5":
            view_movies_by_genre(session)
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")

def add_movie(session):
    title = input("Enter movie title: ")
    release_year = int(input("Enter release year: "))
    director = input("Enter director: ")
    rating = float(input("Enter rating (1-10): "))
    genre_id = int(input("Enter genre ID: "))
    
    genre = session.query(Genre).get(genre_id)
    if genre:
        Movie.create(session, title, release_year, director, rating, genre)
        print(f"Movie '{title}' added successfully.")
    else:
        print("Invalid genre ID.")

def delete_movie(session):
    movie_id = int(input("Enter movie ID to delete: "))
    Movie.delete(session, movie_id)
    print("Movie deleted successfully.")

def view_all_movies(session):
    movies = Movie.get_all(session)
    for movie in movies:
        print(f"{movie.id}: {movie.title}, {movie.release_year}, {movie.rating}")

def find_movie_by_id(session):
    movie_id = int(input("Enter movie ID: "))
    movie = Movie.find_by_id(session, movie_id)
    if movie:
        print(f"{movie.id}: {movie.title}, {movie.release_year}, {movie.rating}")
    else:
        print("Movie not found.")

def view_movies_by_genre(session):
    genre_id = int(input("Enter genre ID: "))
    genre = session.query(Genre).get(genre_id)
    if genre:
        for movie in genre.movies:
            print(f"{movie.id}: {movie.title}, {movie.release_year}, {movie.rating}")
    else:
        print("Invalid genre ID.")