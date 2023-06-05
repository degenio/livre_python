HEURES_SUP = 35
TAUX_SUP = 1.5
TAUX_IMPOSITION = .20


class Employe:
    """initialisateur"""

    def __init__(self, nom, prenom, code):
        self.nom = nom
        self.prenom = prenom
        self.code = code

    def __str__(self):
        return "nom:{:<10s} prenom: {:<10s} " \
               "code: {:<10s}" \
            .format(self.nom, self.prenom, self.code)


class EmpTempsPartiel(Employe):
    def __init__(self, nom, prenom, code, heures, taux):
        super().__init__(nom, prenom, code)
        self.heures = heures
        self.taux = taux

    def __str__(self):
        return super().__str__() + ",heures travaillées:{:7.2f} taux horaire: {:7.2f} " \
            .format(self.heures, self.taux)

    def calculer_salaire(self):
        if self.heures <= HEURES_SUP:
            salaire = self.heures * self.taux
        else:
            salaire = (self.heures - HEURES_SUP) * TAUX_SUP * self.taux + HEURES_SUP * self.taux
        # imposition
        return salaire * (1 - TAUX_IMPOSITION)


class EmpTempsPlein(Employe):
    def __init__(self, nom, prenom, code, salaire):
        super().__init__(nom, prenom, code)
        self.salaire = salaire

    def __str__(self):
        return super().__str__() + ",salaire:{:7.2f} " \
            .format(self.salaire)

    def calculer_salaire(self):
        return self.salaire * (1 - TAUX_IMPOSITION)


def main():
    """instancier objet"""
    nom = input('Saisir le nom:')
    prenom = input('Saisir le prenom:')
    code = input('Saisir le code:')
    statut = int(input('Saisir le statut en choisissant 1 ou 2\n1. Temps plein\n2. Temps partiel:\n'))
    # Saisir les autres données selon le statut
    if statut == 1:
        salaire = float(input('Saisir le salaire:'))
        obj1 = EmpTempsPlein(nom=nom, prenom=prenom, code=code, salaire=salaire)
    else:
        heures = float(input("Saisir le nombre d'heures:"))
        taux = float(input("Saisir le taux horaire:"))
        obj1 = EmpTempsPartiel(nom=nom, prenom=prenom, code=code, heures=40, taux=20)

    # Calculer salaire
    print(obj1.calculer_salaire())


if __name__ == '__main__':
    main()
