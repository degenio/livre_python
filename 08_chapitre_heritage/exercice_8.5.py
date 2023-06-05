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


class RegistreContacts():
    def __init__(self, nom, registre=()):
        self.nom = "liste des contacts"
        self.registre=list()

    def rechercherContacts(self, motcle):
        resultats = list()
        for contact in self.registre:
            if motcle in contact.nom:
                resultats.append(contact)
        return resultats

    def afficher_contact(self):
        print("Nombre de contacts: {:<4d}".format(len(self.registre)))
        for tmp in self.registre:
            print(tmp)

    def ajouter_contact(self, contact):
        self.registre.append(contact)


# créer le registre de contacts
listing = RegistreContacts("liste des contacts")

obj1 = Contact("Alain Clairflou", "a.flouflou@monsite.com")
# print(obj1)
listing.ajouter_contact(obj1)

objF = Fournisseur("Annie Clairclair Inc", "a.clairclair@monsite.com", "1234")
# print(objF)
listing.ajouter_contact(objF)

# Afficher le contenu du registre
listing.afficher_contact()

# rechercher un contact
mot = "Clair"
resultats = listing.rechercherContacts(mot)
print("*" * 25)
print("Elements trouvés")
print("*" * 25)
for res in resultats:
    print(res)