import sqlite3
from tkinter import *
import EditDataBase as Edb
import Database as DB
import ClassLibrary as CL
import Fooldal as Mp
from pathlib import Path

root = Tk()
path = Path('./Movie_db.db')

if(path.is_file() == False):
    DB.CreateDB() 


movies = Edb.GetMovies()
Mp.fooldal(movies)
#Edb.EditPage()

root.mainloop()