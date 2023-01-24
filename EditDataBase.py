import sqlite3

def Test():
    conn = sqlite3.connect("sample_db.db")
    c = conn.cursor()
    cim = input("Cím")
    
    #A VALUES értékeinek meg kell egyezni a szótár kulcsaival!
    c.execute("INSERT INTO termek VALUES (:teremszam, :filmcim, :mufaj, :idotartam, :datum, :kapacitas)",
        {
            'teremszam':f_name.get(),
            'filmcim':l_name.get(),
            'mufaj':zipcode.get(),
            'idotartam':city.get(),
            'datum':street.get(),
            'kapacitas':street.get(),
        }
    )
    conn.commit()
    conn.close()