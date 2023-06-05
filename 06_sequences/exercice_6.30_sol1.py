# version 1

def saisir_valeurs(nombre_valeurs, message):
    liste = []
    for i in range(0, nombre_valeurs):
        liste.append(float(input(message)))
    return liste


def calculer_produit_liste(liste1, liste2):
    # Vérifier la longueur des 2 listes
    if len(liste1) != len(liste2) or liste1 == 0:
        print('Calcul impossible')
        return None
    else:
        resultat = []
        for i in range(0, len(liste1)):
            resultat.append(liste1[i] * liste2[i])
        return resultat


def calculer_somme_liste(liste1, liste2):
    # Vérifier la longueur des 2 listes
    if len(liste1) != len(liste2) or liste1 == 0:
        print('Calcul impossible')
        return None
    else:
        resultat = []
        for i in range(0, len(liste1)):
            resultat.append(liste1[i] + liste2[i])
        return resultat


def main():
    liste_1 = saisir_valeurs(5, 'Saisir une valeur réelle:')
    print('Éléments dans la liste:{}'.format(liste_1))
    liste_2 = saisir_valeurs(5, 'Saisir une valeur réelle:')
    print('Éléments dans la liste:{}'.format(liste_2))
    # Liste avec chaque élément la somme
    liste_somme = calculer_somme_liste(liste_1, liste_2)
    # Afficher le résultat
    print('Liste avec chaque élément la somme:{}'.format(liste_somme))
    # Liste avec chaque élément le produit
    liste_produit = calculer_produit_liste(liste_1, liste_2)
    # Afficher le résultat
    print('Liste avec chaque élément le produit:{}'.format(liste_produit))


if __name__ == '__main__':
    main()

 
