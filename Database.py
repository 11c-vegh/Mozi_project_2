import sqlite3

def CreateDB():
    #Adatbázis létrehozása: egyszer kell lefuttatni!
    #1. lépés: kapcsolódás adatbázishoz (sqlite3)
    conn = sqlite3.connect("Movie_db.db")

    #2. lépés: Létrehozunk egy úgynevezett "kurzort". Ez a kurzor felelős azért, hogy a parancsainkat az sqlite feldolgozza és végrehajtsa
    c = conn.cursor()

    #3. lépés: végrehajtjuk a parancsot (itt tábla létrehozása először az attribútum nevével, majd a típusával)
    c.execute(""" CREATE TABLE termek (
        teremszam integer,
        filmcim text,
        mufaj text,
        idotartam integer,
        kapacitas integer,
        PRIMARY KEY(teremszam)
    )""")

    c.execute(""" CREATE TABLE foglalas (
        foglalassorszam INTEGER PRIMARY KEY AUTOINCREMENT,
        t_szam integer,
        szekszam integer,
        keresztnev text,
        vezeteknev text,
        FOREIGN KEY(t_szam) REFERENCES termek(teremszam)
    )""")

    #Filmek hozzáadása
    c.execute("""INSERT INTO termek VALUES (0, 'The Movie', 'Comedy', 200, 100), (1, 'The Movie Sequel', 'Comedy, Action', 150, 200)""")

    #4. lépés Kommitoljuk a lépést (alkalmazzuk)
    conn.commit()

    #5. lépés: lezárjuk a kapcsolatot
    conn.close()

CreateDB()