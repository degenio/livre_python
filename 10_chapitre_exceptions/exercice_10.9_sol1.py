# Utilisation d'une collection de stockage d'objets

class Employe:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return 'Nom:{}, prenom:{}, age:{}'.format(self.nom, self.prenom, self.age)


class ListeEmploye:
    def __init__(self):
        self.registre = []

    def ajouter_employe(self, emp):
        self.registre.append(emp)

    def afficher_employes(self):
        for emp in self.registre:
            print(emp)


if __name__ == '__main__':
    emp1 = Employe('FlouFlou', 'Alain', 25)
    emp2 = Employe('FlouClair', 'Abdel', 34)
    emp3 = Employe('Annie', 'FlouFlou', 22)
    # Ajout des employés
    listing = ListeEmploye()
    listing.ajouter_employe(emp1)
    listing.ajouter_employe(emp2)
    listing.ajouter_employe(emp3)
    # Affichage des employés
    listing.afficher_employes()
