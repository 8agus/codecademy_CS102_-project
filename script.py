import sqlite3

# Connecting database to sqlite
# The database I used is more than 1GB and due to gitHub size constraints not able to upload database here
# Database can be downloaded from link:
# https://drive.google.com/file/d/1Xgd3N8zozrSUfjUBRvLpjBOptb19KNvS/view?usp=sharing
cur = sqlite3.connect("codecademy_project.db", check_same_thread=False)
db = cur.cursor()

# List created to give genre option to users
movie_genre = ['Action', 'Adventure', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
               'Horror', 'Mystery', 'Music', 'Musical', 'Romance', 'Sport', 'Thriller']

# Implemented a Dict list for user to type first 3 letters
# instead of the whole word when selecting genre
genre_abreviation = {}
for genre in movie_genre:
    genre_abreviation[genre[0:3]] = genre


# Function used to print the movie results
def print_result(lst):
    # Uses a for loop to access the lists of movies that are recommended based on users choices
    for ele in lst:
        print(f'''\n {str(lst.index(ele) + 1) + '.'}
        Movie name: {ele[1]}
        Year: {ele[2]}
        Genre: {ele[3]}
        Rating: {ele[4]}
        Number of votes: {ele[5]}''')


# Function searches for a name in the database and return lists of matches
def look_for_movie():
    m1 = input("\nName of movie you are looking for rating: ")

    # List that saves the matches found from search done on database using sqlite3
    movie_list = list(db.execute("Select * FROM mov_rat WHERE movie_name like ?", ['%' + m1 + '%']))

    # If no matches
    if len(movie_list) < 1:
        print("\nSorry was not able to locate movie with that name:-(")

    # Calls the print function on list with matches found in database
    else:
        print("\n Here is a list of movies containing the name you are looking for.")
        print_result(movie_list)

    # Checks if user wants to search for another movie
    m2 = input('\nDo you want to search for another movie name? Reply Y for Yes and N for No. \n')
    while m2 not in ('y', 'Y', 'n', 'N'):
        print("Invalid selection. Try again.")
        m2 = input('\nDo you want to search for another movie name? Reply Y for Yes and N for N. \n')

    # If user does want to search for another movie the function calls itself
    if m2 in ('y', 'Y'):
        look_for_movie()


# Function searches for movie genre and returns top 10 matches with more than 1000 votes
def look_for_genre():
    # Prints list with first 3 letters of genre's name and full name of genre
    print("\nHere are the options to choose from:\n")
    for abr, gen in genre_abreviation.items():
        print(f"Type {abr} for {gen}")

    # First 3 letters of user selection is saved in this variable
    g1 = input('\nWhich Genre have you selected?')

    # removes black spaces and makes sure first letter is capital
    g1_clean = g1.title().strip(" ")

    # Checks valid selection has been entered by the user
    # Message inform if invalid option is selected and function calls itself
    if g1_clean not in genre_abreviation.keys():
        print("\nInvalid selection. Try again. ")
        look_for_genre()

    # Using key the full name of genre is saved to variable
    value = genre_abreviation[g1_clean]

    # List that saves the matches found from search done on database using sqlite3
    genre_list = list(db.execute("SELECT * FROM mov_rat WHERE genre = ? "
                                 "AND numb_votes > 1000 "
                                 "ORDER BY rating DESC "
                                 "LIMIT 10", [value]))

    # Calls the print function on list with matches found in database
    print("\nHere are the top 10 movies with more than 1000 votes")
    print_result(genre_list)

    # Checks if user wants to search for another movie
    g2 = input('\nDo you want to search for another genre? Reply Y for Yes and N for No. \n')
    while g2 not in ('y', 'Y', 'n', 'N'):
        print("Invalid selection. Try again.")
        g2 = input('\nDo you want to search for another genre? Reply Y for Yes and N for N. \n')

    # If user does want to search for another movie the function calls itself
    if g2 in ('y', 'Y'):
        look_for_genre()


def main():
    # Ask user if recommendation should be done on movie name or genre
    q1 = input("\nDo you want a recommendation on movie name or Genre? Reply M for Movie and G for Genre. ")

    # Checks valid selection has been entered by the user
    # Message inform if invalid option is selected and function calls itself
    if q1 not in ('m', 'M', 'g', 'G'):
        print("\nInvalid selection. Try again. ")
        return main()

    # Calls movie function if user made this selection
    elif q1 in ('m', 'M'):
        look_for_movie()

    # Calls genre function if user made this selection
    else:
        look_for_genre()

    # If there were no more searches the user wanted to perform the script ends with below message
    return "\nThank you for using Codecademy Movie Recommendation\n"


print(main())
