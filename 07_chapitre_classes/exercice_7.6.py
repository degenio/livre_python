# class Action et manipulation
class Action:
    """initialisateur"""
    def __init__(self, symbole, titre, prix_cloture, prix_courant):
        self.symbole = symbole
        self.titre = titre
        self.prix_cloture = prix_cloture
        self.prix_courant = prix_courant


    def __str__(self):
        return "Action  symbole:{:<5} titre: {:<20} " \
               "prix cloture: {:7.2f} prix courant: {:7.2f} " \
               .format(self.symbole, self.titre, self.prix_cloture, self.prix_courant)

    def changement_pourcentage(self):
        return (self.prix_courant / self.prix_cloture - 1) * 100

def main():
    """instancier objet"""
    obj1 = Action(titre="Microsoft", symbole="MSFT", prix_cloture=123.24, prix_courant=127.04)
    print(obj1)
    # afficher le pourcentage de changement
    pourcentage = obj1.changement_pourcentage()
    print('Pourcentage de changement est:{:7.3f}'.format(pourcentage))

if __name__ == '__main__':
    main()
