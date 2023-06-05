#Afficher le mois en toute lettre
#Il y'a d'autres solutions plus élégantes que celle-ci
option = int(input('Saisir le mois désiré 1-12:'))
if option == 1:
    mois = 'Janvier'
elif option ==2:
    mois = 'Fevrier'
elif option == 3:
    mois = 'Mars'
elif option == 4:
    mois = 'Avril'
elif option == 5:
    mois = 'Mai'
elif option == 6:
    mois = 'Juin'
elif option == 7:
    mois = 'Juillet'
elif option == 8:
    mois = 'Aout'
elif option == 9:
    mois = 'Septembre'
elif option == 10:
    mois = 'Octobre'
elif option == 11:
    mois = 'Novembre'
elif option == 12:
    mois = 'Decembre'
else:
    mois = 'invalide'

print('Le mois choisi est:{}'.format(mois))