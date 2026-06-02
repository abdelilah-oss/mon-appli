import tkinter as tk
from tkinter import messagebox

def dire_bonjour():
    nom = entree.get()

    if nom:
        messagebox.showinfo("Bonjour", f"Bonjour {nom} !")
    else:
        messagebox.showwarning("Attention", "Entrez votre nom.")

fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("300x150")

label = tk.Label(fenetre, text="Votre nom :")
label.pack(pady=5)

entree = tk.Entry(fenetre)
entree.pack(pady=5)

bouton = tk.Button(
    fenetre,
    text="Valider",
    command=dire_bonjour
)
bouton.pack(pady=10)

fenetre.mainloop()
