# class Employe

HEURES_SUP = 35
TAUX_SUP = 1.5


class Employe:
    """initialisateur"""

    def __init__(self, nom, prenom, code, statut, salaire):
        self.nom = nom
        self.prenom = prenom
        self.code = code
        self.statut = statut
        self.salaire = salaire

    def __str__(self):
        return "nom:{:<10s} prenom: {:<10s} " \
               "code: {:<10s} statut: {:<15s}, salaire:{:7.2f} " \
            .format(self.nom, self.prenom, self.code, self.statut, self.salaire)


def main():
    """instancier objet"""
    nom = input('Saisir le nom:')
    prenom = input('Saisir le prenom:')
    code = input('Saisir le code:')
    statut = int(input('Saisir le statut en choisissant 1 ou 2\n1. Temps plein\n2. Temps partiel:\n'))
    # Saisir les autres données selon le statut
    if statut == 1:
        salaire = float(input('Saisir le salaire:'))
    else:
        heures = float(input("Saisir le nombre d'heures:"))
        taux = float(input("Saisir le taux horaire:"))
        # Calculer le salaire selon le statut
        if heures <= HEURES_SUP:
            salaire = heures * taux
        else:
            salaire = (heures - HEURES_SUP) * TAUX_SUP * taux + HEURES_SUP * taux

    obj1 = Employe(nom=nom, prenom=prenom, code=code, salaire=salaire,
                   statut='TEMPS PLEIN' if statut == 1 else 'TEMPS PARTIEL')
    print(obj1)


if __name__ == '__main__':
    main()
