import sqlite3

def CreateDB():
    #Adatbázis létrehozása: egyszer kell lefuttatni!
    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()

    #Táblák létrehozása
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
    c.execute("""INSERT INTO termek VALUES
    (0, 'A csodálatos pókember', 'Akció/Kaland/Sci-fi', 136, 100), (1, 'Avatar: A víz útja', 'Sci-fi/Akció', 192, 140), (2, 'Uncharted', 'Sci-fi/Akció', 116, 150),
    (3, 'Bosszúállók: Végjáték', 'Akció/Sci-fi', 182, 120), (4, 'Bosszúállók', 'Kaland/Akció', 143, 130), (5, 'Banános Joe', 'Filmvígjáték', 92, 90),
    (6, 'Kincs, ami nincs', 'Akció/Kaland', 102, 100), (7, 'A Keresztapa', 'Krimi', 175, 130), (8, 'Csillagok között', 'Sci-fi', 110, 100), (9, 'A sötét lovag', 'Szuperhős film', 152, 80) """)
    
    conn.commit()
    conn.close()

