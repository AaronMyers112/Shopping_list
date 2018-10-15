# Shopping_list
A basic shopping list application that holds the data of the list in a MySQL database.
# The Database
The data base is super simple and was created through the use of the [database_setup.sql](https://github.com/AaronMyers112/Shopping_list/blob/master/Database_setup.sql) file. Within the database there are two tables, fundementals and luxeries. Currently only the fundementals table is used as the luxeries table is for future implementation. 

## Dump files
The dump files for the program can be found in the dump folder. The most recent dump of the database is: 
https://github.com/AaronMyers112/Shopping_list/tree/master/dumps/15_10_2018
In these dumps are some test products that are used for testing purposes only. 

# Python
The python that has been implemented within this program is only as the graphical interface. The interface is created using Tkinter, a basic GUI module that comes base with python. Within the interface are three text fields, amount - product - cost. Along with this, the interface has three buttons and two labels. The label at the top shows the action that was just taken, whilst the label at the bottom shows the total cost of the shopping list. 

## The Buttons
The buttons that are currently implemented are insert, delete and print. the insert buttons adds the item that is added in the fields into the database. The delete deletes the specified item from the database, and the print button is still a work in progress but it creates a text file containing an array of all the items that are currently within the fundementals table. 

# Use
Currently, the python is setup to connect to a developer databse (MySQL server installed through the installer) and if you wish to use this program for yourself, you need to change the cnx connection at the top of each function (currently trying to make it into a function of its own but its not working).
