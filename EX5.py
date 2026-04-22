import tkinter as tk
def click(val):
    entry.insert(tk.END, val)
def calculer():
    try:
        resultat = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultat))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")
def clear():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Calculatrice")
root.geometry("300x400")
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", padx=10, pady=10)
frame = tk.Frame(root)
frame.pack()
buttons = [
    ['1', '2', '3', '+'],
    ['4', '5', '6', '-'],
    ['7', '8', '9', '*'],
    ['0', 'C', '=', '/']
]
for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == "=":
            action = calculer
        elif btn == "C":
            action = clear
        else:
            action = lambda x=btn: click(x)
        tk.Button(frame, text=btn, width=5, height=2,
                  font=("Arial", 14),
                  command=action).grid(row=i, column=j, padx=5, pady=5)
root.mainloop()