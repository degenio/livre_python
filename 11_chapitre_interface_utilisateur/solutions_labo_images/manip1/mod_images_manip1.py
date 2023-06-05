import tkinter as tk
import random

# Liste de fruits
fruits = ["pomme", "poire", "orange", "fraise", "citron", "cerise"]

# Fonction pour vérifier la réponse
def verifier_reponse():
    pass

# Fonction pour changer le fruit
def changer_fruit():
    global fruit_actuel
    global essais
    essais = 0
    fruit_actuel = random.choice(fruits)
    lbl_fruit.config(text=fruit_actuel)
    entry.delete(0, tk.END)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Devinez le fruit!")

# Création des widgets
lbl_fruit = tk.Label(root, text="", font=("Arial", 14))
lbl_fruit.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.grid(row=1, column=0, columnspan=2, padx=10)

btn_verifier = tk.Button(root, text="Vérifier!", command=verifier_reponse)
btn_verifier.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

lbl_resultat = tk.Label(root, text="")
lbl_resultat.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")

essais = 0
lbl_nb_essais = tk.Label(root, text="Nombre d'essais: " + str(essais))
lbl_nb_essais.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Lancement du jeu
changer_fruit()

# Boucle principale de la fenêtre
root.mainloop()
