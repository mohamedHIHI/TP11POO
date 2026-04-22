import tkinter as tk
def calculer_carre():
    try:
        nombre = float(entree_nombre.get())
        carre = nombre ** 2
        resultat.config(text=f"Résultat : {carre}")
    except ValueError:
        resultat.config(text="Entrée invalide")
fenetre = tk.Tk()
fenetre.title("Calcul du carré")
fenetre.geometry("300x200")
label = tk.Label(fenetre, text="Entrez un nombre :")
label.pack(pady=5)
entree_nombre = tk.Entry(fenetre)
entree_nombre.pack(pady=5)
bouton = tk.Button(fenetre, text="Calculer le carré", command=calculer_carre)
bouton.pack(pady=10)
resultat = tk.Label(fenetre, text="Résultat :")
resultat.pack(pady=10)
fenetre.mainloop()