# CSCI-33a-Final_Project-MBTA
Final project for CS33a. 

# MBTA Arrival Times

Django App Name:
arrival_time

The project is located in the MBTA directory along with this README.md file. Inside the MBTA directory is a directory named "arrival_time". 
This is the name of the Django app for my final project. All the files related to the work I did for this project are located in there. 

# Background on Project
I wanted to build this project so I could quickly see when the next bus or train is coming at a stop. I want to be able to quickly open an app and know exactly
when it will be there. This app is intended for frequent riders of the MBTA who are familiar with station and bus stop names.

# Views.py
This file contains all the backend python code for allowing users to interact with the web app. Functions either load web pages with 
the proper information or save data submitted by a user to the database. 


# Models.py
This file contains the models to save information about stops, users, and comments on stops. 
It creates a relationship from users to stops so users can track their favorite stops. 

# script.js
This file contains functions that call the MBTA API and add that data to the html page. 
I had trouble with running MBTA Api querries. I got several to work which are included at the top of the file as example urls. 
These urls querry predicted times on the stops that are also saved in the database for the admin user. (password=123)


# HTML files
I created a separate html file for adding stops. This way it keeps the default view index.html clean and easy to see the important information. 

I created an html page for each stop. The comments for stops are also displayed here. This keeps the index.html page less busy. If users want to see comments on stops they can go to the specific stop page. 