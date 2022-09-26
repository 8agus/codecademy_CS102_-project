# Codecademy CS102 Project

### Project assignement 

"In this portfolio project, you will research, brainstorm, and build a basic recommendation program for a topic of your choice. 
By entering letters or words into the terminal, the program will suggest a specific category for the user to explore. 
If the user is interested in the category, the program will provide a variety of related recommendations to the user. 
After you finish building the program, you will create a blog post to share the program on a publication of your choice"


​The project I decided on making, is a movie recommendation program. I used title.rating and name.basics database that can be downloaded from IMDb (https://datasets.imdbws.com/)
to create a new database. The new database was created using sqlite3. Due to size limitations on GitHub, the databases could not be uploaded and available
on the below link. 

https://drive.google.com/file/d/1Xgd3N8zozrSUfjUBRvLpjBOptb19KNvS/view?usp=sharing

The 'main()' function controls the flow of the program, by asking the user to enter 'M' to search by movie name or 'G' to search by Genre. Based on user 
selection the user will be directed to a function 'look_for_moview()' or 'look_for_genre()'. 

The 'look_for_moview()' function asks the user to type the movie name and the user reply is saved in variable 'm1'. Using sqlite3 syntax the database 'mov-rat' 
is search for matches to the value saved in 'm1'. If no match is found, a message is returned informing the same and the function will call itself 
to search for another name. If a match was found then the 'print_result()' function will be called to print information. The user is thereafter given an 
option to search for another movie name. If 'Y' is selected, the function will call itself. If 'N' is selected then the user will be directed to 'main()' 
 and a message will appear that thanks the user for using the program. 

The 'look_for_genre()' function asks the user to type the first 3 letters of a genre's name which is saved in variable 'g1'. Using sqlite3 syntax the database 
'mov_rat' is searched for the top 10 movies with more than 1000 votes and printed using the 'print_result()' function. The user is thereafter given an 
option to search for another genre. If 'Y' is selected, the function will call itself. If 'N' is selected then user will be directed to 'main()' 
 and a message will appear that thanks the user for using the program.  

Requirements

* sqlite3 
