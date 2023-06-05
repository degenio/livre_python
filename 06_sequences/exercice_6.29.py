# version 1
listing = []
for i in range(0, 10):
    listing.append(float(input('Saisir une valeur réelle:')))

# Afficher les valeurs
print('Éléments dans la liste:{}'.format(listing))

# Moyenne
moyenne = sum(listing) / len(listing)
print('La moyenne des valeurs est:{:7.2f}'.format(moyenne))


# version avec fonction

def saisir_valeurs(nombre_valeurs, message):
    liste = []
    for i in range(0, nombre_valeurs):
        liste.append(float(input(message)))
    return liste


def calcul_moyenne(liste):
    return sum(liste) / len(liste)


def main():
    # Afficher les valeurs
    listing = saisir_valeurs(10, 'Saisir une valeur réelle:')
    print('Éléments dans la liste:{}'.format(listing))

    # Moyenne
    moyenne = calcul_moyenne(listing)
    print('La moyenne des valeurs est:{:7.2f}'.format(moyenne))


if __name__ == '__main__':
    main()
