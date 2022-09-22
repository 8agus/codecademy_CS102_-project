import sqlite3

cur = sqlite3.connect("codecademy_project.db", check_same_thread=False)
db = cur.cursor()

s1 = db.execute("Select * FROM mov_rat WHERE movie_name like '%Carmencita%'")

movie_genre = ['Action', 'Adventure', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
               'Horror', 'Mystery', 'Music', 'Musical', 'Romance', 'Sport', 'Thriller']

genre_abreviation = {}
for genre in movie_genre:
    genre_abreviation[genre[0:3]] = genre


def print_result(lst):
    for ele in lst:

        print(f'''\n {str(lst.index(ele) + 1) + '.'}
        Movie name: {ele[1]}
        Year: {ele[2]}
        Genre: {ele[3]}
        Rating: {ele[4]}
        Number of votes: {ele[5]}''')


def look_for_movie():
    m1 = input("\nName of movie you are looking for rating: ")

    movie_list = list(db.execute("Select * FROM mov_rat WHERE movie_name like ?", ['%' + m1 + '%']))

    if len(movie_list) < 1:
        print("\nSorry was not able to locate movie with that name:-(")

    else:
        print("\n Here is a list of movies containing the name you are looking for.")
        print_result(movie_list)

    m2 = input('\nDo you want to search for another movie name? Reply Y for Yes and N for No. \n')
    while m2 not in ('y', 'Y', 'n', 'N'):
        print("Invalid selection. Try again.")
        m2 = input('\nDo you want to search for another movie name? Reply Y for Yes and N for N. \n')

    if m2 in ('y', 'Y'):
        look_for_movie()


def look_for_genre():
    print("\nHere are the options to choose from:\n")
    for abr, gen in genre_abreviation.items():
        print(f"Type {abr} for {gen}")

    g1 = input('\nWhich Genre have you selected?')

    if g1 not in genre_abreviation.keys():
        print("\nInvalid selection. Try again. ")
        look_for_genre()

    value = genre_abreviation[g1]

    genre_list = list(db.execute("SELECT * FROM mov_rat WHERE genre = ? "
                                 "AND numb_votes > 1000 "
                                 "ORDER BY rating DESC "
                                 "LIMIT 10", [value]))

    print("\nHere are the top 10 movies with more than 1000 votes")
    print_result(genre_list)

    g2 = input('\nDo you want to search for another genre? Reply Y for Yes and N for No. \n')
    while g2 not in ('y', 'Y', 'n', 'N'):
        print("Invalid selection. Try again.")
        g2 = input('\nDo you want to search for another genre? Reply Y for Yes and N for N. \n')

    if g2 in ('y', 'Y'):
        look_for_genre()


def movie_recommendation():
    q1 = input("\nDo you want a recommendation on movie name or Genre? Reply M for Movie and G for Genre. ")

    if q1 not in ('m', 'M', 'g', 'G'):
        print("\nInvalid selection. Try again. ")
        return movie_recommendation()

    elif q1 in ('m', 'M'):
        look_for_movie()

    else:
        look_for_genre()

    return "\nThank you for using Codecademy Movie Recommendation\n"


print(movie_recommendation())
