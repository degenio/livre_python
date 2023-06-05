# Générer un nombre aléatoire
import random
inconnu = random.randint(1, 100)
print(inconnu)
# Trouver le nombre
essai = 1
nombre = int(input('Deviner le nombre:'))
while nombre != inconnu:
    if nombre > inconnu:
        print('votre nombre est plus grand!')
    else:
        print('votre nombre est plus petit!')
    essai += 1
    nombre = int(input('Deviner le nombre:'))

print('Vous avez reussi à trouver le nombre {} en {} fois'.format(inconnu, essai))
