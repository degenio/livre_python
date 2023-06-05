from tkinter import *

from mod_classes import Patient
from mod_fichiers import enregistrer_imc
from mod_fonctions import determiner_risque_classe, risque, classification

def quit():
    root.destroy()

def main_calcul():
    patient = Patient(nom.get(), int(age.get()), float(poids.get()), float(taille.get()))
    #Appel pour le calcul IMC
    imc = patient.calculer_imc()
    #Affciher IMC, risque et classification
    lbl_imc.config(text="{0:5.2f}".format(imc))
    indice = determiner_risque_classe(imc)
    lbl_risque.config(text=str(risque[indice]))
    lbl_classification.config(text=str(classification[indice]))

def enregistrer():
    personne = Patient(nom.get(), int(age.get()), float(poids.get()), float(taille.get()))
    #Sauvegarde csv
    enregistrer_imc("bmi_annuel.csv", personne)

#Creation de la fenetre princicpale
root = Tk()
root.title("Calcul de l'indice de masse corporelle")
root.geometry("380x400")

#Creation d'un frame pour le titre
frame_titre = Frame(root)
titre_font = ('arial', 20, 'bold')
label_titre = Label(frame_titre, text='Saisie des données Patient', font=titre_font)
label_titre.grid(row=1, column=1,   padx=5, pady=5 )

#Creation d'un frame pour les composants graphiques
frame_compo = Frame(root)
Label(frame_compo , text='Nom').grid(row=1, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Age').grid(row=2, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Poids').grid(row=3, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Taille').grid(row=4, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='IMC:').grid(row=5, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Risque de santé:').grid(row=6, column=1, sticky=E, padx=5, pady=5)
Label(frame_compo , text='Classification:').grid(row=7, column=1, sticky=E, padx=5, pady=5)

nom = Entry(frame_compo , width=40)
nom.grid(row=1, column=2, columnspan=4, sticky=W)
age = Entry(frame_compo , width=10)
age.grid(row=2, column=2, columnspan=4, sticky=W)
poids = Entry(frame_compo , width=20)
poids.grid(row=3, column=2, columnspan=4, sticky=W)
taille = Entry(frame_compo , width=20)
taille.grid(row=4, column=2, columnspan=4, sticky=W)
lbl_imc = Label(frame_compo  )
lbl_imc.grid(row=5, column=2,  sticky=W)
lbl_risque = Label(frame_compo )
lbl_risque.grid(row=6, column=2, sticky=W)
lbl_classification = Label(frame_compo )
lbl_classification.grid(row=7,  column=2, sticky=W)

#Creation d'un frame pour les boutons
frame_boutons = Frame(root)
btn_calculer = Button(frame_boutons, text='Calculer', width=15, command=main_calcul)
btn_calculer.grid(row=1, column=1, padx=5, pady=5)
btn_enregistrer = Button(frame_boutons, text='Enregistrer', width=15, command=enregistrer)
btn_enregistrer.grid(row=1, column=2, padx=5, pady=5)
btn_cancel = Button(frame_boutons, text='Quitter', width=15, command=quit)
btn_cancel.grid(row=1, column=3)
#Placement des frames
frame_titre.grid(row=1, column=1,columnspan=3,   padx=5, pady=5 )
frame_compo.grid(row=2, column=1,   padx=5, pady=5 )
frame_boutons.grid(row=3, column=1,  padx=5, pady=5 )

root.mainloop()
