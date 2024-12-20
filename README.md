# Movie-management-system  

#### 
An interactive CLI application built with Python, designed to help users organize and manage their movie collections. This project showcases the integration of Python fundamentals, SQLAlchemy ORM, and object-oriented programming techniques.  

#### By **Levy Wechuli**    

## Description   

The movie management system is a minimalist command-line interface application designed to catalog and manage movie collections. The app allows users to add, view, delete, and associate movies with genres, leveraging a SQLite database for persistent storage. It provides an engaging and functional interface to practice Python, database management, and software design concepts.  

## Screenshot  

![image alt](https://github.com/levywechuli/movie-management-system/blob/main/Screenshot%20from%202024-12-19%2023-45-48.png)  

## Features  

**Movie Management**:  
- Add new movies to the collection, providing details like title, release year, and genre.
- View all movies, including their associated details such as title, year, and genre.
- Search for a specific movie by its unique ID.
- Delete movies from the collection easily.

**Genre Management**:  
- Add new genres to categorize movies (e.g., "Action," "Comedy").
- View a list of all genres available in the collection.
- Search for specific genres using their unique IDs.
- View all movies associated with a specific genre to explore related titles.
- Delete a genre from the collection.

**User-Friendly CLI**:  
- Interactive menus guide the user through all available actions.
- Input validation ensures invalid or incomplete data is flagged with descriptive error messages.
- Continuous engagement allows users to perform multiple actions without restarting the application.
- Clear prompts make it easy to switch between managing movies and genres.

## How to Use   

**Requirements**  
- A PC or Mac.  
- Python 3.8 or higher.
- Pipenv for dependency management.

## Instructions  

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd movie-management-system
   ```
2. Install dependencies:
   ```bash
   pipenv install
   ```
3. Run the application:
   ```bash
   pipenv run python app.py
   ```
4. Example Workflow:
   * Start the application to access the main menu.
   * To add a new genre:
       - Navigate to "Manage Genres" and select "Add a Genre."
       - Enter a name for the new genre (e.g., "Action").
   * To add a movie:
       - Navigate to "Manage Movies" and select "Add a Movie."
       - Provide the movie title, release year, and select the newly added genre (e.g., "Action").
   * To view all movies:
       - Select "View All Movies" under "Manage Movies."
       - Review the list of stored movies with their details, including associated genres.
   * To delete a movie:
       - Select "Delete a Movie" under "Manage Movies."
       - Input the movie ID to remove it from the collection.
    * To delete a Genre:  
       - Navigate to the "Manage Genres" section.  
       - Select "Delete a Genre" and provide the genre ID.
             
5. Follow the on-screen menu to:  
  * Add, view, or delete movies.  
  * Add, view, or delete genres.  
  * Explore movies associated with specific genres.  
 
6. Exit the application by selecting the "Exit" option from the main menu.

## Technologies Used  

**Python:** Core programming language.    
**SQLAlchemy:** ORM for database interactions.    
**SQLite:** Lightweight database for data persistence.  
**Pipenv:** Dependency management tool.  

## Support and Contact Details  

If you have any questions, or suggestions, or need assistance, please contact:    

- Email: <levy.wechuli@student.moringaschool.com>

  ## License

  This project is licensed under the MIT License.

  Copyright &copy;2024. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  





   

   
         
      
   
   








  






















































































