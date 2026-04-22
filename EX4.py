import tkinter as tk
def ajouter_tache():
    tache = entree.get()
    if tache != "":
        liste.insert(tk.END, tache)
        entree.delete(0, tk.END)
def marquer_terminee(event):
    selection = liste.curselection()
    if selection:
        index = selection[0]
        texte = liste.get(index)
        if not texte.startswith("✔ "):
            liste.delete(index)
            liste.insert(index, "✔ " + texte)
            liste.itemconfig(index, {'fg': 'gray'})  # changer couleur
def supprimer_tache():
    selection = liste.curselection()
    if selection:
        liste.delete(selection[0])
fenetre = tk.Tk()
fenetre.title("Liste de tâches")
fenetre.geometry("350x300")
entree = tk.Entry(fenetre, width=30)
entree.pack(pady=10)
btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_tache)
btn_ajouter.pack(pady=5)
liste = tk.Listbox(fenetre, width=40, height=10)
liste.pack(pady=10)
liste.bind("<<ListboxSelect>>", marquer_terminee)
btn_supprimer = tk.Button(fenetre, text="Supprimer", command=supprimer_tache)
btn_supprimer.pack(pady=5)
fenetre.mainloop()