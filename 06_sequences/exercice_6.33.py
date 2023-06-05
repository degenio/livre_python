import random

def generer_loto(longueur, nombre):
    loto = set()
    while len(loto) <= longueur:
        loto.add(random.randrange(nombre))
    return loto


def main():
    longueur = int(input('Saisir le nombre de numéros:'))
    nombre = int(input('Saisir un nombre entre 1 et 49:'))
    resultat = generer_loto(longueur, nombre)
    print('La séquence loto est:{} '.format(resultat))


if __name__ == '__main__':
    main()
