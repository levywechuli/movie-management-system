from models.genre import Genre
from models.base import Session

def genre_menu():
    session = Session()
    
    while True:
        print("\nGenre Management")
        print("1. Add a Genre")
        print("2. Delete a Genre")
        print("3. View All Genres")
        print("4. Back to Main Menu")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            add_genre(session)
        elif choice == "2":
            delete_genre(session)
        elif choice == "3":
            view_all_genres(session)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def add_genre(session):
    name = input("Enter genre name: ")
    Genre.create(session, name)
    print(f"Genre '{name}' added successfully.")

def delete_genre(session):
    genre_id = int(input("Enter genre ID to delete: "))
    Genre.delete(session, genre_id)
    print("Genre deleted successfully.")

def view_all_genres(session):
    genres = Genre.get_all(session)
    for genre in genres:
        print(f"{genre.id}: {genre.name}")