from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from tkinter import messagebox
#Oldal méretezése, Fontok megadása
root = Tk()
root.title("Jegyfoglalás")
style = ttk.Style("darkly")
root.geometry("400x700")
Font_tuple = ("Arial", 15, "bold")
Font_tuples = ("Arial", 20, "bold")

#Ikon megadása
photo = PhotoImage(file = 'icons/icon.png')
root.wm_iconphoto(False, photo)

#Adatbázisból kinyert adatokat tároló változók
moviename = ""
genre = ""
movielength = ""
releasedate = ""
fhely = 0
roomnumber = 0

#Megadott adatatok
fname = ""
lname = ""
wanted = 0

def reserve():

    #Label-el Főcím
    lbl0 = ttk.Label(root, text = "MoziTown | Jegyfoglalás", bootstyle="warning", )
    lbl0.grid(row = 0, column = 1, columnspan= 2, padx = 2, pady= 10)
    lbl0.configure(font = Font_tuple)
    
    #Separator az elválasztáshoz különböző adattípusok között
    separator1 = ttk.Separator(root, orient='horizontal')
    separator1.grid(row = 1, column=1, pady= 5, )
    

    #További label-ek Adatok kimutatásához
    lbl1 = ttk.Label(root, text = "Film neve:", bootstyle="warning", )
    lbl1.grid(row = 2, column = 1, padx = 2)
    lbl1.configure(font = Font_tuple)

    lbl1_2 = Label(root, width = 20 , text= moviename)
    lbl1_2.grid(row = 2, column = 2, padx = 2)

    lbl2 = Label(root, text = "Műfaj:")
    lbl2.grid(row = 3, column = 1, padx = 2)
    lbl2_2 = Label(root, width = 20 , text= genre)
    lbl2_2.grid(row = 3, column = 2, padx = 2)

    lbl3 = Label(root, text = "Játékidő:")
    lbl3.grid(row = 4, column = 1, padx = 2)
    lbl3_2 = Label(root, width = 20 , text= movielength)
    lbl3_2.grid(row = 4, column = 2, padx = 2)

    lbl4 = Label(root, text = "Kiadás éve:")
    lbl4.grid(row = 5, column = 1, padx = 2)
    lbl4_2 = Label(root, width = 20 , text= releasedate)
    lbl4_2.grid(row = 5, column = 2, padx = 2)

    separator2 = ttk.Separator(root, orient='horizontal')
    separator2.grid(row = 6, column=1, pady= 5, )

    #Meter használata szabad helyek kimutatásához
    lbl5 = ttk.Label(root, text = "Szabad helyek:", bootstyle="success", font='Helvetica 18 bold')
    lbl5.grid(row = 7, column = 1, padx = 2)
    meter = ttk.Meter(
    metersize=200,
    padding=5,
    amountused=fhely,
    bootstyle="success",
    metertype="semi",
    subtext="Férőhelyek",
    interactive=False,
    )
    meter.grid(row= 7 , column= 2 , padx=10, pady=10 )
    

    #Teremszám kimutatésa
    lbl5 = ttk.Label(root, text = "Teremszám:", bootstyle="info", font='Helvetica 12 bold')
    lbl5.grid(row = 8, column = 1, padx = 2)
    lbl5_2 = Label(root, width = 20 , text= roomnumber)
    lbl5_2.grid(row = 8, column = 2, padx = 2)

    separator2 = ttk.Separator(root, orient='horizontal', )
    separator2.grid(row = 9, column=1, pady= 5, )

    #Adatok megadásához használt kódrészlet, entry mezőbe való megadással

    lbl6 = ttk.Label(root, text = "Vezetéknév", font='Helvetica 12 bold')
    lbl6.grid(row = 10, column = 1, padx = 2, pady=5)
    lbl6_2 = ttk.Label(root , text= "Keresztnév", font='Helvetica 12 bold')
    lbl6_2.grid(row = 10, column = 2, padx = 2, pady= 5)


    e1 = ttk.Entry(root, style='info.TEntry')
    e1.grid(row = 11, column=1, padx= 2, pady= 10)

    e2 = ttk.Entry(root, style='info.TEntry')
    e2.grid(row = 11, column=2, padx= 2, pady= 10)

    lbl7 = ttk.Label(root, text = "Kívánt székek", font='Helvetica 12 bold')
    lbl7.grid(row = 12, column = 1, padx = 2, pady=5)
    e3 = ttk.Entry(root, style='info.TEntry')
    e3.grid(row = 13, column=1, padx= 2)

    lbl7 = ttk.Label(root, text = "Jegytípus", font='Helvetica 12 bold')
    lbl7.grid(row = 12, column = 2, padx = 2, pady=5)
    mb = ttk.Menubutton(root, text='Válasszon jegytípust!', style='info.Outline.TMenubutton')
    menu = Menu(mb)
    option_var = StringVar()
    for option in ['Felnőtt', 'Diák', 'Nyugdíjas']:
        menu.add_radiobutton(label=option, value=option, variable=option_var)
    mb['menu'] = menu
    mb.grid(row = 13, column=2, padx= 2)
   
   

    #Foglaláshoz, vagy visszalépéshez használható gombok

    btn1 = ttk.Button(root, text= "Vissza", style='danger.TButton', command=lambda: root.quit())
    btn1.grid(row = 14, column= 1, padx= 2, pady= 20)

    btn2 = ttk.Button(root, text= "Lefoglalás", style='success.TButton', command=lambda: confirm())
    btn2.grid(row = 14, column= 2, padx= 2,)
    

reserve()


#Lefoglalás gomb megnyomása után megnyitott megerősítő függvény
def confirm():

    if(fhely >= wanted ):   #Megnézi van-e elég férőhely

        #Új ablak megnyitása, méretezése
        cf = Toplevel(root)
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
        l3 = ttk.Label(cf, text = "Teremszám:" )
        l3.grid(row = 3, column = 1, padx = 2, pady= 10)
        l3_2 = Label(cf, width = 20 , text= "x")
        l3_2.grid(row = 3, column = 2, padx = 2)

        l4 = ttk.Label(cf, text = "Székszám(ok):" )
        l4.grid(row = 4, column = 1, padx = 2, pady= 10)
        l4_2 = Label(cf, width = 20 , text= "x")
        l4_2.grid(row = 4, column = 2, padx = 2)

        separator4 = ttk.Separator(cf, orient='horizontal', )
        separator4.grid(row = 5, column=1, pady= 5, )


        l3 = ttk.Label(cf, text = "Foglalási szám", font='Helvetica 16 bold', bootstyle="Info")
        l3.grid(row = 6, column = 1, padx = 2, pady= 10)
        l3_2 = Label(cf, width = 20 , text= "x")
        l3_2.grid(row = 6, column = 2, padx = 2)

        
    #Amennyiben nincs annyi férőhely amennyit a felhasználó kért, hibaüzenetet ad vissza
    else:
        messagebox.showerror(title="Hiba", message="Nincs elég szabad férőhely a foglaláshoz!")


root.mainloop()