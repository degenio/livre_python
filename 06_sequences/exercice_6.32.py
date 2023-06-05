# version 1
equipe = []


def saisir_joueur():
    nom = input('Saisir le nom du joueur:')
    code = input('Saisir le code du joueur:')
    nb_buts = int(input('Saisir le nombre de buts:'))
    nb_aides = int(input("Saisir le nombre d'aides:"))
    equipe.append({'nom': nom, 'code': code, 'buts': nb_buts, 'aides': nb_aides})


def afficher_statistiques():
    # moyennes des buts
    buts = [x['buts'] for x in equipe]
    moyenne_but = sum(buts) / len(buts)
    print('La moyenne des buts est:{:7.2f}'.format(moyenne_but))
    # moyennes des aides
    aides = [x['aides'] for x in equipe]
    moyenne_aide = sum(aides) / len(aides)
    print('La moyenne des aides est:{:7.2f}'.format(moyenne_aide))
    # nombre de joueurs dont le nombre de buts marqués est inférieur à la moyenne
    but_inf_moy = len([x for x in equipe if x['buts'] < moyenne_but])
    print('Le nombre de joueurs ayant nombre de but inferieur à la moyenne:{}'.format(but_inf_moy))
    # nombre de joueurs dont le nombre d'aides est supérieur ou égal à la moyenne
    aide_sup_moy = len([x for x in equipe if x['aides'] >= moyenne_aide])
    print('Le nombre de joueurs ayant nombre aide supérieur ou égal à la moyenne:{}'.format(aide_sup_moy))
    return buts, aides


def calculer_efficacite(buts, aides):
    for tmp in equipe:
        # Calculer efficacité
        tmp['efficacite'] = (0.6 * tmp['buts'] / sum(buts)) + (0.4 * tmp['aides'] / sum(aides))


def selectionner_joueur(seuil):
    for tmp in equipe:
        if tmp['efficacite'] > seuil:
            print('Le joueur {} avec le code {} sera gardé !'.format(tmp['nom'], tmp['code']))


def main():
    nb_joueurs = int(input('Saisir le nombre de joueurs:'))
    i = 0
    while i < nb_joueurs:
        saisir_joueur()
        i += 1
    # Statistiques
    buts, aides = afficher_statistiques()
    seuil = float(input('Saisir le seuil pour garder le joueur:'))
    calculer_efficacite(buts, aides)
    selectionner_joueur(seuil)


if __name__ == '__main__':
    main()
