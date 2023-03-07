from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.font as font
import reservation as res

def fooldalstart():
    fooldal1 = Toplevel()
    fooldal1.geometry('1180x750')
    fooldal1.title("Főoldal")
    fooldal1.configure(bg='black')
    hatter = ttk.Style('darkly')

    ttk.Label(fooldal1, text = 'Filmek', font =('Verdana', 15)).grid(row=1, column=3, pady=(10,10))

    pokember_image = ttk.PhotoImage(file = "Images/a_csodalatos_pokember_4.png")
    avatar_image = ttk.PhotoImage(file = "Images/avatar_a_viz_utja_2.png")
    uncharted_image = ttk.PhotoImage(file = "Images/uncharted_2.png")
    bosszuallok_vegjatek_image = ttk.PhotoImage(file = "Images/bosszallok_vegjatek_2.png")
    bosszuallok_image = ttk.PhotoImage(file = "Images/bosszuallok_2.png")
    bananos_joe_image = ttk.PhotoImage(file = "Images/bananos_joe_2.png")
    kincs_ami_nincs_image = ttk.PhotoImage(file = "Images/kincs_ami_nincs_2.png")
    a_keresztapa_image = ttk.PhotoImage(file = "Images/a_keresztapa_2.png")
    csillagok_kozott_image = ttk.PhotoImage(file = "Images/csillagok_kozott_2.png")
    a_sotet_lovag_image = ttk.PhotoImage(file = "Images/a_sotet_lovag_2.png")

    #photoimage = photo.subsample(3,3)
    #200*250-es ek legyenek a képek
    #https://www.simpleimageresizer.com/upload
    #photo = Label(fooldal, image=photo, height=500, width=300)
    pokember_cim = """
    Csodálatos pókember
    """
    avatar_cim = """
    Avatar: A víz útja
    """
    uncharted_cim = """
    Uncharted
    """
    bosszuallok_vegjatek_cim = """
    Bosszúállók végjáték
    """
    bosszuallok_cim = """
    Bosszúállók
    """
    bananos_joe_cim = """
    Banános Joe
    """
    kincs_ami_nincs_cim = """
    Kincs ami nincs
    """
    a_keresztapa_cim = """
    A keresztapa
    """
    csillagok_kozott_cim = """
    Csillagok között
    """
    a_sotet_lovag_cim = """
    A sötét lovag
    """

    def fooldal(movie):
        #ttk.Style.configure('custom.TButton', foreground='white', font=('Helvetica', 24))
        btn_pokember = ttk.Button(fooldal1, text=pokember_cim,image=pokember_image, compound=BOTTOM, bootstyle="light-outline")
        btn_pokember.grid(row=2, column=1, padx=(10,5))
        btn_avatar = ttk.Button(fooldal1, text=avatar_cim,image=avatar_image,compound=BOTTOM, bootstyle="light-outline", command= res.start()).grid(row=2, column=2, padx=(5,5))
        btn_uncharted = ttk.Button(fooldal1, text=uncharted_cim,image=uncharted_image,compound=BOTTOM, bootstyle="light-outline").grid(row=2, column=3, padx=(5,5))
        btn_bosszuallok_vegjatek = ttk.Button(fooldal1, text=bosszuallok_vegjatek_cim,image=bosszuallok_vegjatek_image,compound=BOTTOM, bootstyle="light-outline").grid(row=2, column=4, padx=(5,5))
        btn_bosszuallok = ttk.Button(fooldal1, text=bosszuallok_cim,image=bosszuallok_image,compound=BOTTOM, bootstyle="light-outline").grid(row=2, column=5, padx=(5,5))
        btn_bananos_joe = ttk.Button(fooldal1, text=bananos_joe_cim,image=bananos_joe_image,compound=BOTTOM, bootstyle="light-outline").grid(row=3, column=1, pady=25, padx=(10,5))
        btn_kincs_ami_nincs = ttk.Button(fooldal1, text=kincs_ami_nincs_cim,image=kincs_ami_nincs_image,compound=BOTTOM, bootstyle="light-outline").grid(row=3, column=2, pady=25, padx=(5,5))
        btn_a_kersztapa = ttk.Button(fooldal1, text=a_keresztapa_cim,image=a_keresztapa_image,compound=BOTTOM, bootstyle="light-outline").grid(row=3, column=3, pady=25, padx=(5,5))
        btn_csillagok_kozott = ttk.Button(fooldal1, text=csillagok_kozott_cim,image=csillagok_kozott_image,compound=BOTTOM, bootstyle="light-outline").grid(row=3, column=4, pady=25, padx=(5,5))
        btn_a_sotet_lovag = ttk.Button(fooldal1, text=a_sotet_lovag_cim,image=a_sotet_lovag_image,compound=BOTTOM, bootstyle="light-outline").grid(row=3, column=5, pady=25, padx=(5,5))


