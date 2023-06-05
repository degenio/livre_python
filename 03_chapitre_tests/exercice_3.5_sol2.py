#conversion de mètres vers pieds et pied en metres
distance = float(input('Saisir la distance à convertir:'))
option = int(input('Saisir option 1 ou 2 \n1. Convertir metres en pieds\n2. Convertir pieds en metres\n'))
if option == 1:
    distance_convertie = distance /.3048
    print('La distance en pieds est:{0:7.2f}'.format(distance_convertie))
elif option == 2:
    distance_convertie = distance * .3048
    print('La distance en metres est:{0:7.2f}'.format(distance_convertie))
else:
    print('Option choisie est invalide')

