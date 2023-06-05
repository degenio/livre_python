# class Voiture


class Voiture:
    """initialisateur"""

    def __init__(self, titre, distance, consommation, cout_essence):
        self.titre = titre
        self.distance = distance
        self.consommation = consommation
        self.cout_essence = cout_essence

    def __str__(self):
        return "titre:{:<10s} distance: {:7.2f}, consommation:{:7.2f}, " \
               "cout essence: {:7.2f}  " \
            .format(self.titre, self.distance, self.consommation, self.cout_essence)

    def calculer_cout_voyage(self):
        return self.distance * self.consommation * self.cout_essence / 100.0


def main():
    """instancier objet"""
    titre = input('Saisir le nom de la voiture:')
    distance = float(input('Saisir la distance:'))
    cout = float(input('Saisir le cout essence:'))
    consommation = float(input('Saisir la consommation de la voiture:'))

    obj1 = Voiture(titre=titre, distance=distance,
                   consommation=consommation, cout_essence=cout)
    print(obj1)
    # Calculer le cout du voyage
    cout_total = obj1.calculer_cout_voyage()
    print('Le cout total du voyage est:{}'.format(cout_total))


if __name__ == '__main__':
    main()
