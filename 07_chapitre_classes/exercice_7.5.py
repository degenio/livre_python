# class Etudiant et manipulation
class Etudiant:
    """initialisateur"""
    def __init__(self, nom, prenom, sexe, adresse, code_etudiant, note_finale):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe
        self.adresse = adresse
        self.code_etudiant = code_etudiant
        self.note_finale = note_finale

    def __str__(self):
        return "Étudiant  nom:{:<10} prénom: {:<10} " \
               "sexe: {:<7} adresse: {:<20} code: {:<8} " \
               "note finale: {:<8}".format(self.nom, self.prenom, self.sexe,
                                           self.adresse, self.code_etudiant, self.note_finale)
    def faire_devoir(self):
        print("je suis un eleve assidu")

def main():
    """instancier les objets"""
    obj1 = Etudiant(prenom="Alain", nom="Flouflou", sexe="M", adresse="14 rue des pins", code_etudiant="118907",
                    note_finale=78)
    print(obj1)
    # demander à faire devoir
    obj1.faire_devoir()

if __name__ == '__main__':
    main()
