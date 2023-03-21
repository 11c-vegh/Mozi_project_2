from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import EditDataBase as Edb
from tkinter import messagebox
import math
import sqlite3
import ClassLibrary

#Oldal méretezése, Fontok megadása
def start(movies, movieid):
    #Kiválasztott székeket tartalmazó lista
    global tempseatids
    tempseatids = []


    reserve = Toplevel()
    reserve.title("Jegyfoglalás")
    style = ttk.Style("darkly")
    reserve.geometry("400x700")
    Font_tuple = ("Arial", 15, "bold")
    Font_tuples = ("Arial", 20, "bold")

    #Ikon megadása
    photo = PhotoImage(file = 'icons/icon.png')
    reserve.wm_iconphoto(False, photo)

    #Adatbázisból kinyert adatokat tároló változók
    moviename = movies[movieid].filmcim
    genre = movies[movieid].mufaj
    movielength = movies[movieid].idotartam
    fhely = movies[movieid].kapacitas
    roomnumber = movies[movieid].teremszam
    Seats = Edb.GetSeats(movies, movieid)
    #Megadott adatatok
    fname = ""
    lname = ""
    wanted = 0

    def SelectSeat():
        SeatPage = Toplevel()

        buttons = []

        #Gombokat generál, meghatározza, hogy a szék már foglalt-e vagy ki van e választva és az alapján adja meg, hogy milyen színű legyen
        for i in range(0, len(Seats)):
            buttons.append(Button(SeatPage, text=i+1, width=3, height=2, command=lambda c=i: AppendorDelete(c, Seats, buttons[c])))
            if(Seats[i] == 1):
                buttons[i].configure(bg="red")
                buttons[i].grid(row=(len(Seats))-math.floor(i/10), column=i%10, pady=10, padx=10)
                continue
            try:
                if(tempseatids[tempseatids.index(i)] == i):
                    buttons[i].configure(bg="orange")
            except ValueError as err:
                buttons[i].configure(bg="green")
            buttons[i].grid(row=(len(Seats))-math.floor(i/10), column=i%10, pady=10, padx=10)

    
    def AppendorDelete(c, Seats, btn):
        if(Seats[c] == 1):
            messagebox.showerror("Foglalt", "Kérem válasszon másik széket")
            return
        try:
            tempseatids.remove(c)
            btn.configure(bg="green")
        except ValueError:
            tempseatids.append(c)
            btn.configure(bg="orange")
        print(tempseatids)
    
        
    
    def reserved():
        reservedseats = 0
        for i in Seats:
            if(i == 1):
                reservedseats += 1

        #Label-el Főcím
        lbl0 = ttk.Label(reserve, text = "MoziTown | Jegyfoglalás", bootstyle="warning", )
        lbl0.grid(row = 0, column = 1, columnspan= 2, padx = 2, pady= 10)
        lbl0.configure(font = Font_tuple)
        
        #Separator az elválasztáshoz különböző adattípusok között
        separator1 = ttk.Separator(reserve, orient='horizontal')
        separator1.grid(row = 1, column=1, pady= 5, )
        

        #További label-ek Adatok kimutatásához
        lbl1 = ttk.Label(reserve, text = "Film neve:", bootstyle="warning", )
        lbl1.grid(row = 2, column = 1, padx = 2)
        lbl1.configure(font = Font_tuple)

        lbl1_2 = Label(reserve, width = 20 , text= moviename)
        lbl1_2.grid(row = 2, column = 2, padx = 2)

        lbl2 = Label(reserve, text = "Műfaj:")
        lbl2.grid(row = 3, column = 1, padx = 2)
        lbl2_2 = Label(reserve, width = 20 , text= genre)
        lbl2_2.grid(row = 3, column = 2, padx = 2)

        lbl3 = Label(reserve, text = "Játékidő:")
        lbl3.grid(row = 4, column = 1, padx = 2)
        lbl3_2 = Label(reserve, width = 20 , text= str(movielength) + ' perc')
        lbl3_2.grid(row = 4, column = 2, padx = 2)


        separator2 = ttk.Separator(reserve, orient='horizontal')
        separator2.grid(row = 6, column=1, pady= 5, )

        #Meter használata szabad helyek kimutatásához
        lbl5 = ttk.Label(reserve, text = "Szabad helyek:", bootstyle="success", font='Helvetica 18 bold')
        lbl5.grid(row = 7, column = 1, padx = 2)
        meter = ttk.Meter(reserve,
        metersize=200,
        padding=5,
        amountused= int(fhely) - reservedseats,
        bootstyle="success",
        metertype="semi",
        subtext="Férőhelyek",
        interactive=False,
        )
        meter.grid(row= 7 , column= 2 , padx=10, pady=10 )
        

        #Teremszám kimutatésa
        lbl5 = ttk.Label(reserve, text = "Teremszám:", bootstyle="info", font='Helvetica 12 bold')
        lbl5.grid(row = 8, column = 1, padx = 2)
        lbl5_2 = Label(reserve, width = 20 , text= roomnumber)
        lbl5_2.grid(row = 8, column = 2, padx = 2)

        separator2 = ttk.Separator(reserve, orient='horizontal', )
        separator2.grid(row = 9, column=1, pady= 5, )

        #Adatok megadásához használt kódrészlet, entry mezőbe való megadással

        lbl6 = ttk.Label(reserve, text = "Vezetéknév", font='Helvetica 12 bold')
        lbl6.grid(row = 10, column = 1, padx = 2, pady=5)
        lbl6_2 = ttk.Label(reserve , text= "Keresztnév", font='Helvetica 12 bold')
        lbl6_2.grid(row = 10, column = 2, padx = 2, pady= 5)


        e1 = ttk.Entry(reserve, style='info.TEntry')
        e1.grid(row = 11, column=1, padx= 2, pady= 10)

        e2 = ttk.Entry(reserve, style='info.TEntry')
        e2.grid(row = 11, column=2, padx= 2, pady= 10)

        lbl7 = ttk.Label(reserve, text = "Kívánt székek", font='Helvetica 12 bold')
        lbl7.grid(row = 12, column = 1, padx = 2, pady=5)
        bx = ttk.Button(reserve, text= "Kiválasztás", style='info.TButton', command=SelectSeat)
        bx.grid(row = 13, column=1, padx= 2)

        lbl7 = ttk.Label(reserve, text = "Jegytípus", font='Helvetica 12 bold')
        lbl7.grid(row = 12, column = 2, padx = 2, pady=5)
        mb = ttk.Menubutton(reserve, text='Válasszon jegytípust!', style='info.Outline.TMenubutton')
        menu = Menu(mb)
        option_var = StringVar()
        for option in ['Felnőtt', 'Diák', 'Nyugdíjas']:
            menu.add_radiobutton(label=option, value=option, variable=option_var)
        mb['menu'] = menu
        mb.grid(row = 13, column=2, padx= 2)
    

        #Foglaláshoz, vagy visszalépéshez használható gombok

        btn1 = ttk.Button(reserve, text= "Vissza", style='danger.TButton', command=lambda: reserve.destroy())
        btn1.grid(row = 14, column= 1, padx= 2, pady= 20)

        btn2 = ttk.Button(reserve, text= "Lefoglalás", style='success.TButton', command=lambda: confirm(e1.get(), e2.get()))
        btn2.grid(row = 14, column= 2, padx= 2,)
        
    reserved()



    #Lefoglalás gomb megnyomása után megnyitott megerősítő függvény
    def confirm(vezeteknev, keresztnev):

        if(fhely >= wanted ):   #Megnézi van-e elég férőhely

            #Ragasztószalagos megoldás az adatbázisba felvitelre
            for i in range(len(tempseatids)):
                print(i)
                Edb.Add_Reservation(tempseatids[i] ,movieid, keresztnev, vezeteknev)

            #Új ablak megnyitása, méretezése
            cf = Toplevel(reserve)
            cf.geometry("280x400")
            #Ikon megadása
            photo = PhotoImage(file = 'icons/icon2.png')
            cf.wm_iconphoto(False, photo)
            #Főcím
            l1 = ttk.Label(cf, text = "MoziTown | Jegyfoglalás", bootstyle="warning", )
            l1.grid(row = 0, column = 1, columnspan= 2, padx = 2, pady= 10)
            l1.configure(font = Font_tuple)

            l2 = ttk.Label(cf, text = "Sikeres Foglalás!", bootstyle="Success", )
            l2.grid(row = 1, column = 1, columnspan = 2, padx = 2, pady= 10)
            l2.configure(font = Font_tuple)

            separator3 = ttk.Separator(cf, orient='horizontal', )
            separator3.grid(row = 2, column=1, pady= 5, )

            #Adatok a lefoglalt jegyről
            l3 = ttk.Label(cf, text = "Teremszám:")
            l3.grid(row = 3, column = 1, padx = 2, pady= 10)
            l3_2 = Label(cf, width = 20 , text= str(movieid))
            l3_2.grid(row = 3, column = 2, padx = 2)

            #Stringbe átgenerálása a székeknek
            szekek = ""
            index = 0
            for i in tempseatids:
                if(index == 0):
                    szekek += str(i)
                else:
                    szekek += ", "+str(i)
                index += 1

            l4 = ttk.Label(cf, text = "Székszám(ok):")
            l4.grid(row = 4, column = 1, padx = 2, pady= 10)
            l4_2 = Label(cf, width = 20 , text= szekek)
            l4_2.grid(row = 4, column = 2, padx = 2)

            separator4 = ttk.Separator(cf, orient='horizontal', )
            separator4.grid(row = 5, column=1, pady= 5, )

            #Minden széknek külön foglalási száma van így ez nehezen megoldható

            l3 = ttk.Label(cf, text = "Foglalási szám", font='Helvetica 16 bold', bootstyle="Info")
            l3.grid(row = 6, column = 1, padx = 2, pady= 10)
            l3_2 = Label(cf, width = 20 , text= "x")
            l3_2.grid(row = 6, column = 2, padx = 2)

            
        #Amennyiben nincs annyi férőhely amennyit a felhasználó kért, hibaüzenetet ad vissza
        else:
            messagebox.showerror(title="Hiba", message="Nincs elég szabad férőhely a foglaláshoz!")

def getitem(a):
    global selected_id
    listselection = listBox.selection()[0]
    selected_id = listBox.item(listselection)["values"][0]
    print(selected_id)

def DeleteReservaton(vezeteknev, keresztnev):
    selected_id = 0
    deletePage = Toplevel()
    global listBox
    conn = sqlite3.connect("Movie_db.db")
    c = conn.cursor()
    c.execute("Select vezeteknev, keresztnev FROM foglalas")
    records = c.fetchall()
    conn.close()
    try:
        conn = sqlite3.connect("Movie_db.db")
        c = conn.cursor()
        c.execute("Select foglalassorszam, t_szam, szekszam FROM foglalas WHERE keresztnev = '"+keresztnev+"' AND vezeteknev = '"+vezeteknev+"'")
        records = c.fetchall()
        cols = ('Foglalási_Szám', 'teremszám', 'székszám')
        listBox = ttk.Treeview(deletePage, columns=cols, show='headings', selectmode=BROWSE)
        #Treeview insert
        for record in records:
            listBox.insert("", "end", values=(record[0], record[1] ,record[2]))
        for col in cols:
            listBox.heading(col, text=col)
        conn.close()
    except sqlite3.Error as err:
        messagebox.showerror("Database operation error", err)#"Hiba az adat felvitelekor")
    except:
        messagebox.showerror("Something is wrong", "Basic error")
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.bind("<<TreeviewSelect>>", getitem)
    btn1 = ttk.Button(deletePage, text= "Foglalás törlése", style='danger.TButton', command=lambda: [CheckId(), deletePage.destroy()]).grid(row=5, column=5, pady=25)

def CheckId():
    if(selected_id != 0):
        Edb.Delete_Reservation(selected_id)