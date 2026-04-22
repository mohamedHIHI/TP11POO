import tkinter as tk
def convertir():
    try:
        celsius = float(entree_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        resultat.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        resultat.config(text="Entrée invalide")
fenetre = tk.Tk()
fenetre.title("Conversion Celsius → Fahrenheit")
fenetre.geometry("300x200")
label_celsius = tk.Label(fenetre, text="Température en Celsius :")
label_celsius.pack(pady=5)
entree_celsius = tk.Entry(fenetre)
entree_celsius.pack(pady=5)
bouton = tk.Button(fenetre, text="Convertir", command=convertir)
bouton.pack(pady=10)
resultat = tk.Label(fenetre, text="Résultat en Fahrenheit")
resultat.pack(pady=10)
fenetre.mainloop()