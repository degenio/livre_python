# Prise en charge d'exception personnalisée
class EmployeDoublonError(Exception):
    def __init__(self, emp):
        self.emp = emp

    def __str__(self):
        return self.emp


class Employe:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __eq__(self, other):
        return self.nom == other.nom and self.prenom == other.prenom

    def __str__(self):
        return 'Nom:{}, prenom:{}, age:{}'.format(self.nom, self.prenom, self.age)


class ListeEmploye:
    def __init__(self):
        self.registre = []

    def valider_employe(self, emp):
        for tmp in self.registre:
            if emp == tmp:
                return True
        return False

    def ajouter_employe(self, emp):
        if self.valider_employe(emp):
            raise EmployeDoublonError(emp)
        else:
            self.registre.append(emp)

    def afficher_employes(self):
        for emp in self.registre:
            print(emp)


if __name__ == '__main__':
    emp1 = Employe('FlouFlou', 'Alain', 25)
    emp2 = Employe('FlouClair', 'Abdel', 34)
    emp3 = Employe('FlouFlou', 'Alain', 22)
    # Ajout des employés
    listing = ListeEmploye()
    try:
        listing.ajouter_employe(emp1)
    except EmployeDoublonError as e:
        print('Doublon:{},{},{}'.format(e.emp.nom, e.emp.prenom, e.emp.age))

    try:
        listing.ajouter_employe(emp2)
    except EmployeDoublonError as e:
        print('Doublon:{},{},{}'.format(e.emp.nom, e.emp.prenom, e.emp.age))

    try:
        listing.ajouter_employe(emp3)
    except EmployeDoublonError as e:
        print('Doublon:{},{},{}'.format(e.emp.nom, e.emp.prenom, e.emp.age))
    # Affichage des employés
    listing.afficher_employes()
