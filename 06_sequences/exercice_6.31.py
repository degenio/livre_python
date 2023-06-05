def saisir_valeurs(nombre_valeurs, message):
    liste = []
    for i in range(0, nombre_valeurs):
        liste.append(int(input(message)))
    return liste


def determiner_consecutif(liste):
    # Vérifier consecutif
    if len(liste) == 0:
        print('Calcul impossible')
        return None
    else:
        for i in range(1, len(liste)):
            if liste[i] != liste[i - 1] + 1:
                return False
    return True


def main():
    liste_1 = saisir_valeurs(3, 'Saisir une valeur entiere:')
    print('Éléments dans la liste:{}'.format(liste_1))
    # Determine si consecutif
    flag = determiner_consecutif(liste_1)
    # Afficher le résultat
    print('Liste :{}'.format(flag))


if __name__ == '__main__':
    main()
 