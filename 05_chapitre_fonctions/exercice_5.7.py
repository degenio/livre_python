def saisir_valeur(message):
    '''
    Retourne une valeur saisie par l'usager
    
    :param message: Le message à afficher à l'usager
    :return: La valeur saisie par l'usager
    '''
    return input(message)

#Appel de la fonction
resultat = saisir_valeur("Saisir une valeur:")
print(resultat)