def calculer_affranchissement(poids: float, destination: str) -> float:
    '''
    Determination du montant à payer pour l'affranchissement d'une lettre

    :param poids: Poids de la lettre
    :param destination: Destination de la lettre
    :return: le montant de l'affranchissement
    '''
    if poids <= 0 or poids > 50:
        montant = 999

    elif poids <= 30:
        # Valider la destination
        if destination == 'usa':
            montant = 2.71
        else:
            montant = 1.07
    else:  # poids entre 30 et 50
        if destination == 'usa':
            montant = 3.88
        else:
            montant = 1.30

    return montant


def afficher_montant(montant):
    '''
    Affichage du montant de l'affranchissement

    :param montant: Montant à afficher
    :return: None
    '''
    if montant == 999:
        print('Envoi impossible')
    else:
        print('Le montant est:{0:5.2f}'.format(montant))


def main():
    poids = float(input('Saisir le poids entre 0 et 50 grs:'))
    destination = input('Saisir la destination:')
    montant = calculer_affranchissement(poids, destination)
    afficher_montant(montant)
    print("Merci d'avoir utilisé la poste")


if __name__ == '__main__':
    main()
