from cli.movie_menu import movie_menu
from cli.genre_menu import genre_menu

def main_menu():
    while True:
        print("Welcome to the Movie Collection Manager")
        print("1. Manage Movies")
        print("2. Manage Genres")
        print("3. Exit")
        choice = input("Please select an option: ")

        if choice == "1":
            movie_menu()
        elif choice == "2":
            genre_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")