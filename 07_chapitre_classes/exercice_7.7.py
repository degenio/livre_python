# class Ventialteur et manipulation

FAIBLE_VITESSE = 1
MOYENNE_VITESSE = 2
HAUTE_VITESSE = 3
class Ventilateur:
    """initialisateur"""
    def __init__(self, vitesse=FAIBLE_VITESSE, enmarche=False, rayon=5,
                 couleur='bleu'):
        self.vitesse = vitesse
        self.enmarche = enmarche
        self.rayon = rayon
        self.couleur = couleur


    def __str__(self):
        statut = "en marche" if self.enmarche else "à l'arret"
        return "Vitesse:{:2d} rayon: {:2d} " \
               "statut: {:<10} couleur: {:<10s} " \
               .format(self.vitesse, self.rayon, statut, self.couleur)


def main():
    """instancier objet"""
    obj1 = Ventilateur(vitesse= HAUTE_VITESSE, couleur='jaune', rayon=10,
                       enmarche=True)
    print(obj1)
    obj2 = Ventilateur(vitesse= MOYENNE_VITESSE)
    print(obj2)
    # afficher le pourcentage de changement


if __name__ == '__main__':
    main()
