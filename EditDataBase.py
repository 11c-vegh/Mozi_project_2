from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

def Kiindulo():

    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()

    c.execute("SELECT teremszam FROM termek")
    records = c.fetchall()

    buttons = []
    
    for i in range(0, len(records)):
        print(i)
        buttons.append(Button(root, text=i, command=lambda c=i: EditPage(buttons[c].cget("text"))))
        buttons[i].pack()

    conn.commit()
    conn.close()

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
        #A VALUES értékeinek meg kell egyezni a szótár kulcsaival!
        c.execute("INSERT INTO foglalas VALUES (NULL, :t_szam, :szekszam, :keresztnev, :vezeteknev)",
            {
                't_szam':t_szam_in.get(),
                'szekszam':szekszam_in.get(),
                'keresztnev': keresztnev_in.get(),
                'vezeteknev': vezeteknev_in.get(),
            }
        )
    except sqlite3.Error as err:
        messagebox.showerror("Database operation error", "Hiba az adat felvitelekor")
    conn.commit()
    conn.close()

def Delete_Reservation(foglalasid):
    try:
        conn = sqlite3.connect("Movie_db.db")
        c = conn.cursor()
        c.execute("""DELETE FROM foglalas WHERE foglalassorszam = ?""", foglalasid)
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

def ReservationPage():
    reservepage = Toplevel()
    #Entryk létrehozása adatbevitelhez
    foglalassorszam_entry = Entry(reservepage, width=30)
    foglalassorszam_entry.grid(row=0, column=1, padx=20)

    szekszam_entry = Entry(reservepage, width=30)
    szekszam_entry.grid(row=1, column=1, padx=20)

    tszam_entry = Entry(reservepage, width=30)
    tszam_entry.grid(row=2, column=1, padx=20)

    keresztnev_entry = Entry(reservepage, width=30)
    keresztnev_entry.grid(row=3, column=1, padx=20)

    vezeteknev_entry = Entry(reservepage, width=30)
    vezeteknev_entry.grid(row=4, column=1, padx=20)

    # Címkék az entrykhez
    foglalassorszam_lbl = Label(reservepage, text="Foglalássorszám")
    foglalassorszam_lbl.grid(row=0, column=0)

    szekszam_lbl = Label(reservepage, text="Székszám")
    szekszam_lbl.grid(row=1, column=0)

    tszam_lbl = Label(reservepage, text="Teremszám")
    tszam_lbl.grid(row=2, column=0)

    keresztnev_lbl = Label(reservepage, text="Keresztnév")
    keresztnev_lbl.grid(row=3, column=0)

    vezeteknev_lbl = Label(reservepage, text="Vezetéknév")
    vezeteknev_lbl.grid(row=4, column=0)

    add_btn = Button(reservepage, text="Mentés", command=lambda: [Add_Reservation(szekszam_entry, tszam_entry, keresztnev_entry, vezeteknev_entry)])
    add_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)
  

def AddPage():
    addpage = Toplevel()
    #Entryk létrehozása adatbevitelhez
    teremszam_entry = Entry(addpage, width=30)
    teremszam_entry.grid(row=0, column=1, padx=20)

    filmcim_entry = Entry(addpage, width=30)
    filmcim_entry.grid(row=1, column=1, padx=20)

    mufaj_entry = Entry(addpage, width=30)
    mufaj_entry.grid(row=2, column=1, padx=20)

    idotartam_entry = Entry(addpage, width=30)
    idotartam_entry.grid(row=3, column=1, padx=20)

    kapacitas_entry = Entry(addpage, width=30)
    kapacitas_entry.grid(row=4, column=1, padx=20)

    # Címkék az entrykhez
    teremszam_lbl = Label(addpage, text="Teremszám")
    teremszam_lbl.grid(row=0, column=0)

    filmcim_lbl = Label(addpage, text="Film Címe")
    filmcim_lbl.grid(row=1, column=0)

    mufaj_lbl = Label(addpage, text="Műfaja")
    mufaj_lbl.grid(row=2, column=0)

    idotartam_lbl = Label(addpage, text="Időtartama")
    idotartam_lbl.grid(row=3, column=0)

    kapacitas_lbl = Label(addpage, text="Kapacitás")
    kapacitas_lbl.grid(row=4, column=0)

    edit_btn = Button(addpage, text="Mentés", command=lambda: [Add_movie(teremszam_entry, filmcim_entry, mufaj_entry, idotartam_entry, kapacitas_entry)])
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

#AddPage()
#ReservationPage()
#Kiindulo()

root.mainloop()