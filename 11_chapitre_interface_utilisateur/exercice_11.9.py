import tkinter as tk


def show_taille():
    lbl_resultat.config(text=txt_produit.get() +':'+ v.get(), font=('arial', 16))


# Creer la fenetre root
root = tk.Tk()
root.geometry('300x150')
root.title('Choix Taille')

v = tk.StringVar()
v.set(1)  # init

tailles = [("Large", 'large'),
           ("Medium", 'medium'),
           ("Small", 'small')]
# ajout section du produit
lbl_produit = tk.Label(root, text='Produit:')
lbl_produit.grid(row=1, column=1, sticky='w', padx=5, pady=5)
txt_produit = tk.Entry(root)
txt_produit.grid(row=1, column=2, sticky='w', padx=5, pady=5)

# ajout section Taille
frame = tk.Frame(root)
frame.grid(row=2, column=2, sticky='w', padx=3, pady=5)
i = 2
for taille, val in tailles:
    tk.Radiobutton(frame,
                   text=taille,
                   padx=5,
                   variable=v,
                   command=show_taille,
                   value=val).grid(row=2, column=i, sticky='w', padx=5, pady=5)
    i += 1

lbl_resultat = tk.Label(root)
lbl_resultat.grid(row=3, column=2, sticky='w', padx=5, pady=5)

# Afficher la fenetre
root.mainloop()
