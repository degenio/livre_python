import tkinter as tk

def calculer():
    texto=txt_nom.get().upper()
    txt_nom.delete(0, tk.END)
    txt_nom.insert(0,texto)
    salaire = float(txt_salaire.get()) + 1000
    lbl_resultat.config(text=str(salaire))

#Creer la fenetre root
root = tk.Tk()
root.geometry('400x200')
root.title('Calculateur')
#ajout section du nom
lbl_nom = tk.Label(root, text='Nom:')
lbl_nom.grid(row=1, column=1, sticky='w', padx=5, pady=5)
txt_nom = tk.Entry(root)
txt_nom.grid(row=1, column=2, sticky='w', padx=5, pady=5)

#ajout section du salaire
lbl_salaire = tk.Label(root, text='Salaire:')
lbl_salaire.grid(row=2, column=1, sticky='w', padx=5, pady=5)
txt_salaire = tk.Entry(root, font=('arial', 14))
txt_salaire.grid(row=2, column=2, sticky='w', padx=5, pady=5)

#resultat
lbl_resultat = tk.Label(root, font=('arial', 14), fg='red')
lbl_resultat.grid(row=3, column=2, sticky='w', padx=5, pady=5)
#Ajout du bouton calculer
btn_calculer = tk.Button(root, text='Calculer', command=calculer)
btn_calculer.grid(row=4, column=2, sticky='w', padx=5, pady=5)
#Afficher la fenetre
root.mainloop()