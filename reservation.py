from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from tkinter import messagebox
root = Tk()
root.title("Jegyfoglalás")
style = ttk.Style("darkly")
root.geometry("400x700")
Font_tuple = ("Arial", 15, "bold")
Font_tuples = ("Arial", 20, "bold")
photo = PhotoImage(file = 'Mozi_project_2/icon.png')
root.wm_iconphoto(False, photo)

fhely = 0
wanted = 0

def reserve():

    lbl0 = ttk.Label(root, text = "MoziTown | Jegyfoglalás", bootstyle="warning", )
    lbl0.grid(row = 0, column = 1, columnspan= 2, padx = 2, pady= 10)
    lbl0.configure(font = Font_tuple)
    

    separator1 = ttk.Separator(root, orient='horizontal')
    separator1.grid(row = 1, column=1, pady= 5, )
    


    lbl1 = ttk.Label(root, text = "Film neve:", bootstyle="warning", )
    lbl1.grid(row = 2, column = 1, padx = 2)
    lbl1.configure(font = Font_tuple)

    lbl1_2 = Label(root, width = 20 , text= "x")
    lbl1_2.grid(row = 2, column = 2, padx = 2)

    lbl2 = Label(root, text = "Műfaj:")
    lbl2.grid(row = 3, column = 1, padx = 2)
    lbl2_2 = Label(root, width = 20 , text= "x")
    lbl2_2.grid(row = 3, column = 2, padx = 2)

    lbl3 = Label(root, text = "Játékidő:")
    lbl3.grid(row = 4, column = 1, padx = 2)
    lbl3_2 = Label(root, width = 20 , text= "x")
    lbl3_2.grid(row = 4, column = 2, padx = 2)

    lbl4 = Label(root, text = "Kiadás éve:")
    lbl4.grid(row = 5, column = 1, padx = 2)
    lbl4_2 = Label(root, width = 20 , text= "x")
    lbl4_2.grid(row = 5, column = 2, padx = 2)

    separator2 = ttk.Separator(root, orient='horizontal')
    separator2.grid(row = 6, column=1, pady= 5, )

    
    lbl5 = ttk.Label(root, text = "Szabad helyek:", bootstyle="success", font='Helvetica 18 bold')
    lbl5.grid(row = 7, column = 1, padx = 2)
    meter = ttk.Meter(
    metersize=200,
    padding=5,
    amountused=100,
    bootstyle="success",
    metertype="semi",
    subtext="Férőhelyek",
    interactive=False,
    )
    meter.grid(row= 7 , column= 2 , padx=10, pady=10 )
    
    lbl5 = ttk.Label(root, text = "Teremszám:", bootstyle="info", font='Helvetica 12 bold')
    lbl5.grid(row = 8, column = 1, padx = 2)
    lbl5_2 = Label(root, width = 20 , text= "x")
    lbl5_2.grid(row = 8, column = 2, padx = 2)

    separator2 = ttk.Separator(root, orient='horizontal', )
    separator2.grid(row = 9, column=1, pady= 5, )

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
   

    btn1 = ttk.Button(root, text= "Vissza", style='danger.TButton', command=lambda: root.quit())
    btn1.grid(row = 14, column= 1, padx= 2, pady= 20)

    btn2 = ttk.Button(root, text= "Lefoglalás", style='success.TButton', command=lambda: confirm())
    btn2.grid(row = 14, column= 2, padx= 2,)
    
    

reserve()

def confirm():
    if(fhely >= wanted ):
        cf = Toplevel(root)
        cf.geometry("280x400")
        photo = PhotoImage(file = 'Mozi_project_2/icon2.png')
        cf.wm_iconphoto(False, photo)
        l1 = ttk.Label(cf, text = "MoziTown | Jegyfoglalás", bootstyle="warning", )
        l1.grid(row = 0, column = 1, columnspan= 2, padx = 2, pady= 10)
        l1.configure(font = Font_tuple)

        l2 = ttk.Label(cf, text = "Sikeres Foglalás!", bootstyle="Success", )
        l2.grid(row = 1, column = 1, columnspan = 2, padx = 2, pady= 10)
        l2.configure(font = Font_tuple)

        separator3 = ttk.Separator(cf, orient='horizontal', )
        separator3.grid(row = 2, column=1, pady= 5, )


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

        
        
    else:
        messagebox.showerror(title="Hiba", message="Nincs elég szabad férőhely a foglaláshoz!")

root.mainloop()