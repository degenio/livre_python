# Gestion de contact avec Héritage
class Contact:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def __str__(self):
        return "nom: {0:<15s} et email: {1:<15s}".format(self.nom, self.email)

class Fournisseur(Contact):
    def __init__(self, nom, email, code_scn):
        super().__init__(nom, email)
        self.code_scn = code_scn

    def passer_commande(self, commande):
        print('La commande est pour: {}'.format(commande))

    def __str__(self):
        return "nom: {0:<15s} et email: {1:<15s}, code:{2:25s}".format(self.nom, self.email, self.code_scn)


obj1 = Contact("Alain Clairflou", "a.flouflou@monsite.com")
print(obj1)

objF = Fournisseur("Annie Clairclair Inc", "a.clairclair@monsite.com", "1234")
print(objF)