import tkinter as tk
compteur = 0
def incrementer():
    global compteur
    compteur += 1
    label_compteur.config(text=str(compteur))
def decrementer():
    global compteur
    if compteur > 0:
        compteur -= 1
        label_compteur.config(text=str(compteur))
fenetre = tk.Tk()
fenetre.title("Application Compteur")
fenetre.geometry("300x200")
label_compteur = tk.Label(fenetre, text="0", font=("Arial", 20))
label_compteur.pack(pady=20)
btn_increment = tk.Button(fenetre, text="Incrémenter", command=incrementer)
btn_increment.pack(pady=5)
btn_decrement = tk.Button(fenetre, text="Décrémenter", command=decrementer)
btn_decrement.pack(pady=5)
fenetre.mainloop()