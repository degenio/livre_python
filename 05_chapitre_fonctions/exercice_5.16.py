TAUX_REMBOURSEMENT = 0.85
def saisir_infos():
    nom = input('Nom:')
    prenom = input('Prénom:')
    courriel = input('Courriel:')
    montant_paye = float(input('Montant à payer pour les travaux:'))
    contribution = float(input('Votre contribution:'))
    return nom, prenom, courriel, montant_paye, contribution

def calculer_remboursement(infos):
    return infos[3] * TAUX_REMBOURSEMENT - infos[4]

def afficher_resultat(infos, remboursement):
    print('Voici les détails de la demande de remboursement des frais')
    print('Voici les montants qui vous concernent')
    print('Montant des travaux nécessaires:{}'.format(infos[3]))
    print('Votre contribution déclarée:{}'.format(infos[4]))
    print('Remboursement auquel vous avez droit:{}'.format(remboursement))


#Appel de fonctions
infos = saisir_infos()
remboursement = calculer_remboursement(infos)
afficher_resultat(infos, remboursement)
