import sqlite3
from tkinter import *
import EditDataBase as Edb
import Database as DB
import ClassLibrary as CL
import Fooldal as Mp
from pathlib import Path
import ttkbootstrap as ttk
import reservation as res

root = Tk()
path = Path('Movie_db.db')
print(path)

movies = []

if(path.is_file() == False):
    DB.CreateDB() 

#Edb.Delete_Reservation("x", "y", 0, 1)
movies = Edb.GetMovies()

#print(Edb.GetSeats(movies, 0))
Mp.fooldal(movies)
#Edb.EditPage()
#res.start(movies,0)
root.mainloop()