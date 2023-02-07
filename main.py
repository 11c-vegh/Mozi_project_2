import EditDataBase as Edb
import Database as DB
from pathlib import Path

path = Path('./Movie_db.db')

print(path.is_file())
#Edb.EditPage()