#conversion de kilogramme vers livre et livre vers kilogramme
poids = float(input('Saisir le poids à convertir:'))
option = int(input('Saisir option 1 ou 2 \n1. Convertir kilogramme en livre\n2. Convertir livre en kilogramme\n'))
if option == 1:
    poids_converti = poids * 2.2
    print('Le poids en livre est:{0:7.2f}'.format(poids_converti ))
elif option == 2:
    poids_converti = poids /2.2
    print('Le poids en kilo est:{0:7.2f}'.format(poids_converti))
else:
    print('Option choisie est invalide')
