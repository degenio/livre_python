"""Mulitplication de deux nombres avec gestion d'exception et boucle
"""
flag = True
while flag:
    try:
        nombre_1 = float(input('Saisir nombre 1:'))
        nombre_2 = float(input('Saisir nombre 2:'))
    except ValueError as e:
        print('La valeur saisie n’est pas un nombre !')
    else:
        resultat = nombre_1 * nombre_2
        print('Le produit de {} par {} est:{}'.format(nombre_1, nombre_2, resultat))
        flag = False
