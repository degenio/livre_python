def convertir_secondes(secondes):
    '''
    Calcul le nombre d'heures, minutes et secondes

    :param secondes: Le nombre de secondes à convertir
    :return: Le tuple comprenant les nombres d'heures, minutes
    et secondes
    '''
    nb_heures = secondes // 3600
    nb_minutes = (secondes % 3600) // 60
    nb_secondes = ((secondes % 3600) % 60)
    return nb_heures, nb_minutes, nb_secondes

#Appel de la fonction
resultat = convertir_secondes(89568578)
print('Heures: {0}, Minutes: {1}, Secondes:{2}'.format(
    resultat[0], resultat[1], resultat[2]))


