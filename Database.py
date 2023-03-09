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
    #Megadtam az adatokat, de nem tetszik ez a nulladik terem, de felrobban a kód ha átírom, úgyhogy majd + 1 et kell sztem adni mindegyikhez - Milán 
    c.execute("""INSERT INTO termek VALUES
    (0, 'A csodálatos pókember', 'Akció/Kaland/Sci-fi', 136, 100), (1, 'Avatar: A víz útja', 'Sci-fi/Akció', 192, 140), (2, 'Uncharted', 'Sci-fi/Akció', 116, 150),
    (3, 'Bosszúállók: Végjáték', 'Akció/Sci-fi', 182, 120), (4, 'Bosszúállók', 'Kaland/Akció', 143, 130), (5, 'Banános Joe', 'Filmvígjáték', 92, 90),
    (6, 'Kincs, ami nincs', 'Akció/Kaland', 102, 100), (7, 'A Keresztapa', 'Krimi', 175, 130), (8, 'Csillagok között', 'Sci-fi', 110, 100), (9, 'A sötét lovag', 'Szuperhős film', 152, 80) """)
    


    #4. lépés Kommitoljuk a lépést (alkalmazzuk)
    conn.commit()

    #5. lépés: lezárjuk a kapcsolatot
    conn.close()

