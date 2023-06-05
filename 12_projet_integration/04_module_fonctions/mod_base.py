# Calcul IMC
classification=["Poids insuffisant",
"Poids normal","Excès de poids",
"Obésité, classe I","Obésité, classe II","Obésité, classe III"]
risque=["Accru","Moindre",
"Accru","Élevé","Très élevé","Extrêmement élevé"]

def saisir_valeur(msg, msg_error ):
    valeur = float(input(msg))
    while valeur <= 0:
        valeur = float(input(msg_error))
    return valeur
    
def calculer_imc(poids, taille):
    return poids / (taille ** 2)

def afficher_imc(valeur):
    print("Votre imc est :{0:7.2f}".format(valeur))
    
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
    #saisir le poids
    poids = saisir_valeur("Saisir le poids:", "Saisir le poids > 0:")
    #saisie la taille
    taille = saisir_valeur("Saisir la taille:", "Saisir la taille > 0:")
    #calculer imc
    imc = calculer_imc(poids, taille)
    #afficher imc
    afficher_imc(imc)
    #determiner indice
    indice = determiner_risque_classe(imc)
    #afficher risque et classification
    afficher_risque_classe(indice)

if __name__ == '__main__':
    main()