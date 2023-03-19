from tkinter import *
from tkinter import messagebox
import ClassLibrary as CL
import sqlite3

def Kiindulo():
    root = Tk()
    try:
        conn = sqlite3.connect("Movie_db.db")
        c = conn.cursor()

        c.execute("SELECT teremszam FROM termek")
        records = c.fetchall()

        buttons = []
    
        for i in range(0, len(records)):
            buttons.append(Button(root, text=i, command=lambda c=i: EditPage(buttons[c].cget("text"))))
            buttons[i].pack()

        conn.commit()
        conn.close()
    except sqlite3.Error:
        messagebox.showerror("Database error", "Hiba az adat lekérésekor")

def GetMovies():
    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()

    c.execute("SELECT * FROM termek")
    records = c.fetchall()

    templist = []

    for record in records:
        templist.append(CL.Film(record[0], record[1], record[2], record[3], record[4]))

    conn.commit()
    conn.close()
    return templist

def GetSeats(movies, t_szam):
    #a székek 10-esével vannak sorba rendezve(itt még nincs bent)
    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()

    c.execute("SELECT szekszam FROM foglalas WHERE t_szam="+str(t_szam))
    records = c.fetchall()

    templist = []

    i = 0
    for i in range(0, movies[t_szam].kapacitas):
        isSeat = False
        for record in records:
            if(i == record[0]):
                isSeat = True
                templist.append(1)
        if(isSeat == False):
            templist.append(0)
        

    conn.commit()
    conn.close()
    return templist

def Update_movie(teremszam_entry, filmcim_entry, mufaj_entry, idotartam_entry, kapacitas_entry):
    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()
    try:
        #A VALUES értékeinek meg kell egyezni a szótár kulcsaival!
        c.execute("""UPDATE termek SET
		teremszam = :teremszam,
		filmcim = :filmcim,
		mufaj = :mufaj,
		idotartam = :idotartam,
		kapacitas = :kapacitas 
		WHERE teremszam = :teremszam""",
		{
		'teremszam': teremszam_entry,
		'filmcim': filmcim_entry,		
		'mufaj': mufaj_entry,
		'idotartam': idotartam_entry,
        'kapacitas': kapacitas_entry,
		})
    except sqlite3.IntegrityError:
        messagebox.showerror("Egyező Elsődleges Kulcs", "A teremhez már van megadva film")
    except sqlite3.Error:
        messagebox.showerror("Database operation error", "Hiba az adat felvitelekor")
    conn.commit()
    conn.close()

def Add_movie(teremszam_entry, filmcim_entry, mufaj_entry, idotartam_entry, kapacitas_entry):
    try:
        conn = sqlite3.connect("Movie_db.db")
        c = conn.cursor()
        #A VALUES értékeinek meg kell egyezni a szótár kulcsaival!
        c.execute("INSERT INTO termek VALUES (:teremszam, :filmcim, :mufaj, :idotartam, :kapacitas)",
            {
                'teremszam':teremszam_entry.get(),
                'filmcim':filmcim_entry.get(),
                'mufaj':mufaj_entry.get(),
                'idotartam':idotartam_entry.get(),
                'kapacitas':kapacitas_entry.get(),
            }
        )
    except sqlite3.IntegrityError:
        messagebox.showerror("Egyező Elsődleges Kulcs", "A teremhez már van megadva film")
    except sqlite3.Error:
        messagebox.showerror("Database operation error", "Hiba az adat felvitelekor")
    conn.commit()
    conn.close()

def Add_Reservation(szekszam_in, t_szam_in, keresztnev_in, vezeteknev_in):
    try:
        conn = sqlite3.connect("Movie_db.db")
        c = conn.cursor()
        c.execute("begin")
        #A VALUES értékeinek meg kell egyezni a szótár kulcsaival!
        c.execute("INSERT INTO foglalas VALUES (NULL, :t_szam, :szekszam, :keresztnev, :vezeteknev)",
            {
                't_szam':t_szam_in,
                'szekszam':szekszam_in,
                'keresztnev': keresztnev_in,
                'vezeteknev': vezeteknev_in,
            }
        )
    except sqlite3.Error as err:
        messagebox.showerror("Database operation error", "Hiba az adat felvitelekor")
    conn.commit()
    conn.close()

def Delete_Reservation(foglalasid):
    print(foglalasid)
    try:
        conn = sqlite3.connect("Movie_db.db")
        c = conn.cursor()
        c.execute("DELETE FROM foglalas WHERE foglalassorszam = "+str(foglalasid))
    except sqlite3.Error as err:
        messagebox.showerror("Database operation error", "Hiba az adat felvitelekor")
    conn.commit()
    conn.close()

def EditPage(teremszam):
    print(teremszam)
    edit = Toplevel() 

    teremszam_entry = Entry(edit, width=30)
    teremszam_entry.grid(row=0, column=1, padx=20)

    filmcim_entry = Entry(edit, width=30)
    filmcim_entry.grid(row=1, column=1, padx=20)

    mufaj_entry = Entry(edit, width=30)
    mufaj_entry.grid(row=2, column=1, padx=20)

    idotartam_entry = Entry(edit, width=30)
    idotartam_entry.grid(row=3, column=1, padx=20)

    kapacitas_entry = Entry(edit, width=30)
    kapacitas_entry.grid(row=4, column=1, padx=20)

    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()

    c.execute("SELECT * FROM termek WHERE teremszam="+str(teremszam))
    records = c.fetchall()

    for record in records:
        teremszam_entry.insert(0, record[0])
        filmcim_entry.insert(0, record[1])
        mufaj_entry.insert(0, record[2])
        idotartam_entry.insert(0, record[3])
        kapacitas_entry.insert(0, record[4])

    conn.commit()
    conn.close()

    edit_btn = Button(edit, text="Mentés", command=lambda: [Update_movie(teremszam_entry.get(), filmcim_entry.get(), mufaj_entry.get(), idotartam_entry.get(), kapacitas_entry.get())])
    edit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

#ReservationPage()
#Kiindulo()

#root.mainloop()