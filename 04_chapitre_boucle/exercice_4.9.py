####### Solution 1 #######
# Boucle sur 999
nombre = int(input('1. Saisir une valeur. Saisir 999 pour arreter:'))
somme = 0
compteur = 0
while nombre != 999:
    somme += nombre
    compteur += 1
    nombre = int(input('1. Saisir une valeur. Saisir 999 pour arreter:'))

print('Somme est:{} et la moyenne est:{}'.format(somme, somme / compteur))


####### Solution 2 avec arrondi sur 2 décimales #######
# Boucle sur 999
nombre = int(input('1. Saisir une valeur. Saisir 999 pour arreter:'))
somme = 0
compteur = 0
while nombre != 999:
    somme += nombre
    compteur += 1
    nombre = int(input('1. Saisir une valeur. Saisir 999 pour arreter:'))

print('Somme est:{} et la moyenne est:{}'.format(round(somme, 2), round(somme / compteur, 2)))


"""Solution 3 avec total de nombres positifs
et nombre de repétition du chiffre zéro
"""
# Boucle sur 999
nombre = int(input('1. Saisir une valeur. Saisir 999 pour arreter:'))
somme = 0
compteur = 0
somme_positifs = 0
nb_zeros = 0
while nombre != 999:
    somme += nombre
    compteur += 1
    if nombre == 0:
        nb_zeros += 1
    elif nombre > 0:
        somme_positifs += nombre

    nombre = int(input('1. Saisir une valeur. Saisir 999 pour arreter:'))

print('Somme est:{} et la moyenne est:{}'.format(round(somme, 2), round(somme / compteur, 2)))
print('Somme de nombres positifs:{}'.format(somme_positifs))
print('Nombre occurences de zéro:{}'.format(nb_zeros))
