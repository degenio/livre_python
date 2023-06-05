def calculer_affranchissement(poids: float, destination: str) -> float:
    '''
    Determination du montant à payer pour l'affranchissement d'une lettre

    :param poids: Poids de la lettre
    :param destination: Destination de la lettre
    :return: le montant de l'affranchissement
    '''
    if destination == 'usa':
        if poids <= 30:
            montant = 2.71
        elif poids <= 50:
            montant = 3.88

    else:
        if poids <= 30:
            montant = 1.07
        elif poids <= 50:
            montant = 1.3
    return montant


def afficher_montant(montant):
    '''
    Affichage du montant de l'affranchissement

    :param montant: Montant à afficher
    :return: None
    '''
    print('Le montant est:{0:5.2f}'.format(montant))


def main():
    # verifier le poids
    poids = 0
    poids = float(input('Saisir le poids entre 0 et 50 grs:'))
    if poids <= 0 or poids > 50:
        print("Le poids depasse les limites d'envoi")
    else:
        destination = input('Saisir la destination:')
        montant = calculer_affranchissement(poids, destination)
        afficher_montant(montant)
    print("Merci d'avoir utilisé la poste")


if __name__ == '__main__':
    main()
