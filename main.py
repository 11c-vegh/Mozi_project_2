import EditDataBase as Edb
import Database as DB
from pathlib import Path

path = Path('./Movie_db.db')

if(path.is_file() == False):
    DB.CreateDB()

#Edb.EditPage()