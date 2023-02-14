import sqlite3
import EditDataBase as Edb
import Database as DB
import ClassLibrary as CL
import Fooldal as Mp
from pathlib import Path

path = Path('./Movie_db.db')

movies = []

if(path.is_file() == False):
    DB.CreateDB()

def GetMovies():
    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()

    c.execute("SELECT * FROM termek")
    records = c.fetchall()

    for record in records:
        #print(record[0])
        movies.append(CL.Film(record[0], record[1], record[2], record[3], record[4]))

    conn.commit()
    conn.close()


GetMovies()
Mp.fooldal(movies)
#Edb.EditPage()