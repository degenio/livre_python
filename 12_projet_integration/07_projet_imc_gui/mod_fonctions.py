#Projet intégration IMC
from mod_classes import Patient
from mod_fichiers import enregistrer_imc

risque = ["Accru",
"Moindre","Accru","Élevé","Très élevé","Extrêmement élevé"]
classification = ["Poids insuffisant",
"Poids normal","Excès de poids","Obésité  classe I","Obésité  classe II","Obésité classe III"
]

def saisir_valeur(msg, msg_erreur):
    '''
    Saisir d'une valeur pour les besoins IMC
    :param msg: Message pour la saisie d'une valeur
    :param msg_erreur: Message en cas d'erreur de saisie
    :return: La valeur saisie
    '''
    data = float(input(msg))
    while data <= 0:
        data = float(input(msg_erreur))
    return data

def calculer_imc(patient):
    return patient.poids / patient.taille ** 2

def afficher_imc(imc):
    print("Votre IMC est: {0:5.2f}".format(imc))

def determiner_risque_classe(imc):
    if imc < 18.5:
        indice = 0
    elif imc < 25:
        indice = 1
    elif imc < 30:
        indice = 2
    elif imc < 35:
        indice = 3
    elif imc < 40:
        indice = 4
    else:
        indice = 5

    return indice

def afficher_risque_classe(indice):
    print("Classification:{0:20s}".format(classification[indice]))
    print("Risque:{0:20s}".format(risque[indice]))

def main():
    poids = saisir_valeur("S.V.P, votre poids:","S.V.P, votre poids en numérique   sup à 0:")
    taille = saisir_valeur("S.V.P, votre taille:", "S.V.P, votre taille en numérique  sup à 0:")
    nom = input("S.V.P, votre nom:")
    age = int(input("S.V.P, votre age:"))

    #Creer un objet de type Patient
    patient = Patient(nom ,age , poids , taille )
    # calculer imc
    imc = patient.calculer_imc()
     # afficher imc
    afficher_imc(imc)
    # determiner indice
    indice = determiner_risque_classe(imc)
    # afficher risque et classification
    afficher_risque_classe(indice)
    #Sauvegarder dans un fichier
    enregistrer_imc("sortie_imc.csv",patient)

if __name__ == '__main__':
    main()