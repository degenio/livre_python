import tkinter as tk
from tkinter import ttk

def afficher():
    produit = txt_produit.get()
    qte = float(txt_qte.get())
    taille = tailleC.get()
    resultat = 'Produit:{}, taille:{}, qte:{}'.format(produit, taille, qte)
    lbl_resultat.config(text=resultat)

#Creer la fenetre root
root = tk.Tk()
root.geometry('400x200')
root.title('Choix de chandail')
#ajout section du produit
lbl_produit = tk.Label(root, text='Produit:')
lbl_produit.grid(row=1, column=1, sticky='w', padx=5, pady=5)
txt_produit = tk.Entry(root)
txt_produit.grid(row=1, column=2, sticky='w', padx=5, pady=5)

#ajout section taille
lbl_taille = tk.Label(root, text='Taille:')
lbl_taille.grid(row=2, column=1, sticky='w', padx=5, pady=5)
# Combobox creation
n = tk.StringVar()
tailleC = ttk.Combobox(root, width=10, textvariable=n)
#  valeurs
tailleC['values'] = (' Large',
                          ' Medium',
                          ' Small')

tailleC.current(1)
tailleC.grid(row=2, column=2, sticky='w', padx=5, pady=5)

#ajout section qte
lbl_qte = tk.Label(root, text='Quantité:')
lbl_qte.grid(row=3, column=1, sticky='w', padx=5, pady=5)
txt_qte = tk.Entry(root)
txt_qte.grid(row=3, column=2, sticky='w', padx=5, pady=5)

#resultat
lbl_resultat = tk.Label(root, font=('arial', 14), fg='red')
lbl_resultat.grid(row=4, column=2, sticky='w', padx=5, pady=5)
#Ajout du bouton calculer
btn_calculer = tk.Button(root, text='Afficher', command=afficher)
btn_calculer.grid(row=5, column=2, sticky='w', padx=5, pady=5)
#Afficher la fenetre
root.mainloop()