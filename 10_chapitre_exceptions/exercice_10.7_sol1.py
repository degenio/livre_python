def traiter_casse(ficin, ficout):
    with open(ficin) as fi:
        with open(ficout, 'w') as fo:
            for ligne in fi:
                if not ligne.strip().islower():
                    fo.write(ligne)


if __name__ == '__main__':
    traiter_casse('casse.txt', 'sortie.txt')