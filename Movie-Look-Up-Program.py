#!/usr/bin/env python
# coding: utf-8

#    # ISM 224 Project:                                        Gilliam Van Der Merwe

# ## Introduction:
# The purpose of this assignment is to develop a program that is able to retrieve information about a movie given user input. The information retrieved about the movie includes the following information: movie title, year released, age rating, complete release date, runtime, genre, directors, actors, plot, blurred, language, country, awards, link to poster, ratings (metascore, imdb rating, rotten tomatoes), IMDB votes, IMDB ID, type (movie, series, etc), DVD information, box office, production and website address. The information is retrieved from the Open Movie Database (OMDB). The program makes use of the OMDB RESTful API web service in order to access the information.
# 
# RESTful API stands for Representational State Transfer Technology Application Programming Interface. RESTful API is a web service that utilises HTTP requests so that it can "retrieve a resource", "change" or "update" the state of the resource, "create" a new resource or "delete" an existing resource (SearchMicroservices, 2019). API, in terms of website usage, is code that allows for communication between two software applications (SearchMicroservices, 2019). The API showcases the appropriate way to communicate with the other application (SearchMicroservices, 2019). In this case the how the movie lookup program communicates with the Open Movie Database. 

# ## Final Code:

# In[ ]:


import sys
get_ipython().system('{sys.executable} -m pip install omdb')


# In[16]:


# api key = b94319ef
import omdb
import traceback
import sys
import os
import ast
import tkinter
from tkinter import *

API_KEY = 'b94319ef'
omdb.set_default('apikey', API_KEY)

# This function takes in the movie info as a dictionary and stores the values in seperate var and prints the
# output as well as returning the info as a string in a structured format.
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

        
# This while loop acts as the main functionality of the program, includes mode selection as well as operational
# code for both the console mode and GUI mode.
while True:
    print("Select the number of the mode you would like to run.")
    mode = input("\n0) Console mode\n1) GUI mode\n2) Exit\n")

    if mode == '0':
        print("\n1) Search Movie Title\n2) View Previously Searched Movie Title\n3) Enhanced Search\n4) Back\n")
        option = input("\nEnter the number of the option you would like to choose: ")

        while True:
            # option one is the basic search option where the user inputs movie title name and calls method
            # to display the info about the movie.
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

            # option two reads in the stored info about the previously searched movie title from a text file.
            elif option == '2':
                
                string_to_convert = ''
                
                with open("Previously Searched Titles.txt", "r") as s:
                    for string_to_convert in s:
                        dict_read_In = ast.literal_eval(string_to_convert.strip())
                        check_store_values(dict_read_In)
                        
            # option three is for a more specific search that includes both the movie title and year in order to get
            # a more specific result.
            elif option == '3':    
                search_title = input("Enter movie title: ")
                search_year = input("Enter moive title's year: ")

                res = omdb.get(title = search_title, year = search_year, fullplot = True, tomatoes = True, timeout = 5)
                check_store_values(res)
                
            # option four merely acts as a 'back button' in order to exit option selection loop and back into mode
            # selection loop.
            elif option == '4':
                print("\nReturn to mode selection.\n")
                break
                
            # in the event that the user enters any input that does not match the required input this message will
            # be displayed to the user and the user will need to try again.
            else:
                print("\nINVALID: Please try again.")

            print("\n1) Search Movie Title\n2) View Previously Searched Movie Title\n3) Enhanced Search\n4) Back\n")
            option = input("\nEnter the number of the option you would like to choose.\n")
            
    # mode one is the GUI mode of the program.        
    elif mode == '1':
        
        main_menu = tkinter.Tk()
        main_menu.title("Movie Lookup Program")
        
        main_menu_canvas = tkinter.Canvas(main_menu, width = 1000, height = 700)
        main_menu_canvas.configure(background = 'cyan')
        main_menu_canvas.pack()
        
        # this function is for the search by title window in the GUI. Will be explained later in the project.
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
            
            search_by_title_window = tkinter.Tk()
            search_by_title_window.title("Search By Title")
            
            search_by_title_window_canvas = tkinter.Canvas(search_by_title_window, width = 1000, height = 700)
            search_by_title_window_canvas.configure(background = 'cyan')
            search_by_title_window_canvas.pack()
            
            search_box = Entry(search_by_title_window)
            search_by_title_window_canvas.create_window(400, 50, window = search_box)
            
            search_btn = tkinter.Button(search_by_title_window, text = 'SEARCH',bg = 'purple',fg = 'cyan' ,command = search)
            search_by_title_window_canvas.create_window(200, 50, window = search_by_title_btn)
            
            back_btn = tkinter.Button(search_by_title_window, text = 'BACK',bg = 'purple',fg = 'cyan' , command = search_by_title_window.destroy)
            search_by_title_window_canvas.create_window(500, 50, window = back_btn)
            
            search_by_title_window.mainloop()
        # this function is the operational code for the prev search button in the main menu.
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
            
        # this function is the operational code for the history button in the main menu.
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
        
        search_by_title_btn = tkinter.Button(main_menu, text = 'SEARCH BY TITLE',bg = 'purple',fg = 'cyan' , command = search_by_title)
        main_menu_canvas.create_window(500, 200, window = search_by_title_btn)
        
        
        prev_search_btn = tkinter.Button(main_menu, text = 'PREVIOUSLY SEARCHED TITLE',bg = 'purple',fg = 'cyan' , command = prev_search)
        main_menu_canvas.create_window(500, 300, window = prev_search_btn)
        
        history_btn = tkinter.Button(main_menu, text = 'HISTORY',bg = 'purple',fg = 'cyan' , command = history)
        main_menu_canvas.create_window(500, 400, window = history_btn)
         
        exit_btn = tkinter.Button(main_menu, text = 'EXIT',bg = 'purple',fg = 'cyan' , command = main_menu.destroy)
        main_menu_canvas.create_window(500, 500, window = exit_btn)

        main_menu.mainloop()
    
    # mode two is used to quit the program
    elif mode == '2':
        print("\nProgram Quit")
        break
    # if any invalid input is used the program will output this error message and the user will have to try again.
    else:
        print("\nINVALID: Please try again.")
