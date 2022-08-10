# Movie-Look-Up-Program

### Introduction:
The purpose of this assignment is to develop a program that is able to retrieve information about a movie given user input. The information retrieved about the movie includes the following information: movie title, year released, age rating, complete release date, runtime, genre, directors, actors, plot, blurred, language, country, awards, link to poster, ratings (metascore, imdb rating, rotten tomatoes), IMDB votes, IMDB ID, type (movie, series, etc), DVD information, box office, production and website address. The information is retrieved from the Open Movie Database (OMDB). The program makes use of the OMDB RESTful API web service in order to access the information.

RESTful API stands for Representational State Transfer Technology Application Programming Interface. RESTful API is a web service that utilises HTTP requests so that it can "retrieve a resource", "change" or "update" the state of the resource, "create" a new resource or "delete" an existing resource (SearchMicroservices, 2019). API, in terms of website usage, is code that allows for communication between two software applications (SearchMicroservices, 2019). The API showcases the appropriate way to communicate with the other application (SearchMicroservices, 2019). In this case the how the movie lookup program communicates with the Open Movie Database. 

### Code Explained:
    def check_store_values(dict):
        check_response = ""
        try:
            check_response = dict['response']
        except:
            print('')
    
    title = year = rated = released = runtime = genre = director = writer = actors = plot = language = country = awards = poster = ratings_Str = metascore = imdb_rating = imdb_votes = imdb_id = movie_type = dvd = box_office = production = website = ""
    
    if check_response == 'True':
        
        if 'title' in dict:
            title = ""
            title = dict['title']

        if 'year' in dict:
            year = ""
            year = dict['year']

        if 'rated' in dict:
            rated = ""
            rated = dict['rated']

        if 'released' in dict:
            released = ""
            released = dict['released']

        if 'runtime' in dict:
            runtime = ""
            runtime = dict['runtime']

        if 'genre' in dict:
            genre = ""
            genre = dict['genre']

        if 'director' in dict:
            director = ""
            director = dict['director']

        if 'writer' in dict:
            writer = ""
            writer = dict['writer']

        if 'actors' in dict:
            actors = ""
            actors = dict['actors']

        if 'plot' in dict:
            plot = ""
            plot = dict['plot']

        if 'language' in dict:
            language = ""
            language = dict['language']

        if 'country' in dict:
            country = ""
            country = dict['country']

        if 'awards' in dict:
            awards = ""
            awards = dict['awards']

        if 'poster' in dict:
            poster = ""
            poster = dict['poster']

        if 'ratings' in dict:
            ratings_Str = ""
            ratings_Str = str(list(dict['ratings']))

        if 'metascore' in dict:
            metascore = ""
            metascore = dict['metascore']

        if 'imdb_rating' in dict:
            imdb_rating = ""
            imdb_rating = dict['imdb_rating']

        if 'imdb_votes' in dict:
            imdb_votes = ""
            imdb_votes = dict['imdb_votes']

        if 'imdb_id' in dict:
            imdb_id = ""
            imdb_id = dict['imdb_id']

        if 'type' in dict:
            movie_type = ""
            movie_type = dict['type']

        if 'dvd' in dict:
            dvd = ""
            dvd = dict['dvd']

        if 'box_office' in dict:
            box_office = ""
            box_office = dict['box_office']

        if 'production' in dict:
            production = ""
            production = dict['production']

        if 'website' in dict:
            website  = ""
            website = dict['website']

        if 'response' in dict:
            response = ""
            response = dict['response']

        print("\nTitle: ", title + "\n" + "Year: ", year + "\n" + "Rated: ", rated
         + "\n" + "Released: ", released + "\n" + "Runtime: ", runtime + "\n" 
         + "Genre: ", genre + "\n" + "Director: ", director + "\n" + "Writer: ", writer
         + "\n" + "Actors: ", actors + "\n" + "Plot: ", plot + "\n" + "Language: ", language
         + "\n" + "Country: ", country + "\n" + "Awards: ", awards + "\n" + "Poster: ", poster
         + "\n" + "Ratings: " + ratings_Str + "\n" + "Metascore: ", metascore + "\n" + "imdb_rating: ", imdb_rating
         + "\n" + "imdb_votes: ", imdb_votes + "\n" + "imdb_id: ", imdb_id + "\n" + "Type: ", movie_type
         + "\n" + "DVD: ", dvd + "\n" + "box_office: ", box_office + "\n" + "Production: ", production
         + "\n" + "Website: ", website + "\n" + "Response: ", response + "\n")
        
        temp = ("\nTitle: " + title + "\n" + "Year: " + year + "\n" + "Rated: " + rated
         + "\n" + "Released: " + released + "\n" + "Runtime: "+ runtime + "\n" 
             + "Genre: "+ genre + "\n" + "Director: "+ director + "\n" + "Writer: "+ writer
            + "\n" + "Actors: " + actors + "\n" + "Plot: "+ plot + "\n" + "Language: "+ language
             + "\n" + "Country: " + country + "\n" + "Awards: " + awards + "\n" + "Poster: " + poster
            + "\n" + "Ratings: " + ratings_Str + "\n" + "Metascore: "+ metascore + "\n" + "imdb_rating: " + imdb_rating
             + "\n" + "imdb_votes: "+ imdb_votes + "\n" + "imdb_id: "+ imdb_id + "\n" + "Type: "+ movie_type
            + "\n" + "DVD: "+ dvd + "\n" + "box_office: "+ box_office + "\n" + "Production: "+ production
             + "\n" + "Website: "+ website + "\n" + "Response: "+ response + "\n")
        
        return temp
        
    else:
        print("\nThe movie you have searched does not exist inside the database or was incorrectly entered, please try again.")
        


### Check_store_values Function Explained:
The purpose of this function is to take the dictionary, containing the information about the movie being searched, as a parameter and then being used to find the necessary values to store in variables  by making use of the dictionary's keys. Firslty, the function checks to see if the dictionary key 'response' has a 'true' value and if it does it will check through a group of keys to see if there is information that can be stored in variables and once this is done it will print the informaton in a structured format to the console and this information will also being stored in a temporary variable that will be returned when the function is called. On the other hand if the value of 'response' is 'false' an error message saying that the movie could not be found in the database or was incorrectly entered will be printed to the console.


    if option == '1':
                try:
                    search_query = input("\nEnter in the title of the movie you would like to search: ")
                    
                    request_response = omdb.request(t=search_query, timeout=5)
                    response = request_response.status_code

                    if response == 200:
                        dict = omdb.title(search_query, timeout = 5)
                        check_store_values(dict)
                        string_dict = str(dict)
                        
                        try:
                            # The info about the movie title is stored in a text file as a string in a dictionary format
                            file_open = open("Previously Searched Titles.txt", "w")
                            file_open.write(string_dict);
                            file_open.close()
                        
                        except:
                            traceback.print_exc()
                        
                    else:
                        print("\nThe movie you have searched does not exist inside the database or was incorrectly entered, please try again.")
                except:
                    traceback.print_exc()


### Option One:
If the variable option has the value '1' then a try except block will execute. Within this block the user is prompted via the console to enter the tilte of the movie they wish to search. In order to determine if the movie is in the database, a request is sent to the omdb via the .request() method and then the .status_code method is used to determine is there is a true reponse from the omdb and if there is the status code will be '200'. If the status code is '200', then the .title() method is used to retrieve the movie information and it will be stored in a dictionary. The function described above previously is then called and executed. After that the the dictionary is then converted to a string and stored in a variable. Thereafter, a try except block is created. Within this block a text file is opened and the variable in which the dictioanry is stored is written to the text file and then it is closed. If the movie is not in the database or is incorrectly entered an error message will be printed to the console.


    elif option == '2':
                
                string_to_convert = ''
                
                with open("Previously Searched Titles.txt", "r") as s:
                    for string_to_convert in s:
                        dict_read_In = ast.literal_eval(string_to_convert.strip())
                        check_store_values(dict_read_In)


### Option Two:
If the value of option is '2' then code within the elif block will be executed. A temporary variable is given the value of an empty string. As per convention in pyhton if ast.literal_eval() is to be used to evaluate a string variable from a text file in order to convert it to a dictionary it makes use of the with statement in order open the text file, process the content of the text file and then close it. Within the with statement there is a for loop that loops through the strings in text file which is then converted to a dictionary and stored in a variable. Thereafter, the check_store_values() method is executed.


    elif option == '3':    
                search_title = input("Enter movie title: ")
                search_year = input("Enter moive title's year: ")

                res = omdb.get(title = search_title, year = search_year, fullplot = True, tomatoes = True, timeout = 5)
                check_store_values(res)


### Option Three:
Option three is used when the user wishes to search for a movie that may have the same name as other movies in which case this option is used as it aids the user by allowing for a more specific search. The user is asked to input the title of the movie as well as the year the movie was released. The input is then used as parameters in the .get() method from the omdb API. In this case the user will recieve a full plot of the movie as well as ratings by rotten tomatoes. The information is retrieved and stored as a dictionary thereafter the check_store_values() method is called.


    def search_by_title():
            
            # this function is the operation code for the search button.
            def search():
                search_entry = search_box.get()
                temp_output = ""

                try:
                    request_response = omdb.request(t=search_entry, timeout=5)
                    response = request_response.status_code

                    if response == 200:
                        dict = omdb.title(search_entry, timeout = 5)
                        temp_output = check_store_values(dict)
                        string_dict = str(dict)
                        text_output = search_by_title_window_canvas.create_text(0, 400, anchor=W, font="none 12 bold",text = temp_output)
                        
                        # this function merely clears the displayed output
                        def clear_text_output():
                            search_by_title_window_canvas.delete(text_output)
                            
                        clear_btn = tkinter.Button(search_by_title_window, text = 'CLEAR',bg = 'purple',fg = 'cyan' , command = clear_text_output)
                        search_by_title_window_canvas.create_window(200, 100, window = clear_btn)
                            
                        try:
                            file_open = open("Previously Searched Titles.txt", "w")
                            file_open.write(string_dict);
                            file_open.close()
                            
                            file_open1 = open("Movie_Search_History.txt", "a")
                            file_open1.write(search_entry + ", ")
                            file_open1.close()

                        except:
                            traceback.print_exc()

                    else:
                        temp_ouput = ("\nThe movie you have searched does not exist inside the database or was incorrectly entered, please try again.")
                except:
                    traceback.print_exc()


### Search_by_title Function:
When the Search By Title button is clicked on the main menu in the GUI mode this function will be executed. Within this function is another function called search. The search function will be called when the search button in the Search by Title window is clicked. This will take the input which the user entered in the entry box and then run simlarly to how Option one in console mode is executed. The differences are that it will be displayed on the canvas of the Search by title window, there is anoother function called clear_text_output() that is called when the clear button is clicked which is also created via the Button() function from the tkinter librabry which is used to create the GUI, and another text file is opened as well in order to store the search queries of the user.


    def prev_search():
            prev_search_window = tkinter.Tk()
            prev_search_window.title("Previously Searched Title")
            
            prev_search_window_canvas = tkinter.Canvas(prev_search_window, width = 1000, height = 700)
            prev_search_window_canvas.configure(background = 'cyan')
            prev_search_window_canvas.pack()
            
            back_btn2 = tkinter.Button (prev_search_window_canvas, text = 'BACK',bg = 'purple',fg = 'cyan' , command = prev_search_window.destroy)
            prev_search_window_canvas.create_window(500, 50, window = back_btn2)
            
            string_to_convert = ''
            text_display = ''
            
            with open("Previously Searched Titles.txt", "r") as s:
                for string_to_convert in s:
                    dict_read_In = ast.literal_eval(string_to_convert.strip())
                    text_display = check_store_values(dict_read_In)
            
            prev_search_window_canvas.create_text(0, 400, anchor=W, font="none 12 bold",text = text_display)


### Prev_search Function:
This function is called when the previously searched title button in the main menu of the GUI mode is clicked. It then creates a new window called previously searched title. A canvas is then created with a cyan coloured background. A back button is created which will close the current window. Thereafter the same code as option two from the console mode is executed and displayed on the current window.


    def history():
            history_window = tkinter.Tk()
            history_window.title("History")
            
            history_window_canvas = tkinter.Canvas(history_window, width = 1000, height = 700)
            history_window_canvas.configure(background = 'cyan')
            history_window_canvas.pack()
            
            back_btn3 = tkinter.Button(history_window_canvas, text = 'BACK',bg = 'purple',fg = 'cyan' , command = history_window.destroy)
            history_window_canvas.create_window(500, 50, window = back_btn3)
            
            text_display2 = ''
            
            with open("Movie_Search_History.txt", "r") as s:
                for string in s:
                    text_display2 = string
            
            history_window_canvas.create_text(500, 400, anchor=W, font="none 12 bold",text = text_display2)


### History Function:
This function is called when the history button is clicked. It creates a new window called History. It also creates a new canvas with a cyan background for the current window, a back button and opens a text file contained the previously searched titles names which is them stored in a string variable that is later displayed on a text canvas.

## Retrospective:
The first major problem I encountered was trying to read in a string from the previously searched titles text file. The string was in the format of a dictionary and needed to be converted to a dictionary and then parsed as a parameter to the check_store_values() function. After quite a lengthy period of reseacrh and trial and error, I mamaged to solve the problem by making use of the with statement and the .literal_eval() function from the ast library. 

The second major problem was with the enhanced search option in the console mode. I used the .request() function from the omdb API and ended up with a different dictionary format that is not compatible with the check_store_values() function. After trying to adapt the program to no avail I went back to the omdb API and eventualy managed to solve the problem by making use of the .get() function. 

The third major problem was with the GUI mode and the tkinter library. I spent quite some time on trying to use both buttons and text output on the same window in the correct positions. The mistake I made was trying to use grids instead of canvases. After some considerable research on the tkinter library I learnt how to make use of canvas, button, entry box and text widgets. 

Improvements that can be made are using a better background image instead of just a solid colour, adding a enhanced search option to the GUI mode and a drop down menu that includes a help option and link to the omdb website. 

I have learnt more about the omdb API and the tkinter library. In future, I intend to spend more time on researching the APIs and libraries I intend to use in my programs as it will save me plenty of time. 

## Help:
Run the code underneath the Final Code heading and not under code explained.

On start up, the user will be prompted with a message on the console asking the user which mode the user would like to use. The modes are 0) Console mode and 1) GUI mode. It also gives the option to choose 2) Exit to quit the program. The user must enter 0, 1 or 2 (as numbers not text).

If the user chooses 0 then the user will be prompted with an option selection menu prompt. Here the user can choose the options: 1) Search Movie Title, 2) View Previously Searched Movie Title, 3) Enhanced Search, 4) Back. If the user types in option 1 then the user will be asked to enter the title of the movie the user wishes to search. If the user enters a valid search the user will be given the information about the movie else the user will recieve an error message after which the user will be taken back to option selection. If the user chooses option two the user will be displayed the previously search movie title's information and then prompted again with the option slection. If the user chooses 3, the user will be prompted to input the movie title and then input the movie year and if valid it will display the movie information else an error message will be displayed, thereafter it will prompt the user with option selection again. If the user chooses 4, then the user will be prompted with mode selection. 

If the user chooses 1 for mode selection, then a main menu window will open with four buttons to click.Do not close the main menu window when other windows open. If the first button(Search By Title) is clicked, a new window will open that will have a search button, text entry box and a back button. If the user enters a valid movie title and clicks the search button then the movie information will be displayed on the current window. A new button called clear will appear which if clicked will clear the movie information displayed in order for new movie information to be displayed. If the back button is clicked it will close the current window. In the main menu, if the second button(Previously Searched Movie Title) is clicked it will open a new window that will display the information of the last movie searched and has a back button that will close the current window. If the user clicks on the third button(History) it will open a new window that will display the search history of the user and a back button to return to main menu. If the user clicks on the last button(Exit) it will close the GUI mode and the user will be prompted to select a mode in the console. 

## References:
- SearchMicroservices. (2019). What is RESTful API? - Definition from WhatIs.com. [online] Available at: https://searchmicroservices.techtarget.com/definition/RESTful-API [Accessed 10 May 2019].

- PyPI. (2019). omdb. [online] Available at: https://pypi.org/project/omdb/ [Accessed 10 May 2019].

- Omdbapi.com. (2019). OMDb API - The Open Movie Database. [online] Available at: http://www.omdbapi.com/ [Accessed 10 May 2019].

- Datacamp.com. (2019). [online] Available at: https://www.datacamp.com/ [Accessed 10 May 2019].
