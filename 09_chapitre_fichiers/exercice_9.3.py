# solution avec retour de la longueur 
def calcul_fichier_longueur(fichier):
    maximum = ""
    for ligne in open(fichier):
        if len(ligne) > len(maximum):
            maximum = ligne
    return len(maximum)



# solution avec retour de la longueur et la phrase elle meme
def calcul_fichier_stats(fichier):
    ligne_maximum = ""
    for ligne in open(fichier):
        if len(ligne) > len(ligne_maximum):
            ligne_maximum = ligne
    return len(ligne_maximum), ligne_maximum

def main():
    maximus = calcul_fichier_longueur("stats.txt")
    print("Longueur maximum:", maximus)

    maximus, ligne_max = calcul_fichier_stats("stats.txt")
    print("Longueur maximum:", maximus)
    print("Ligne avec longueur maximum:", ligne_max)

if __name__ == '__main__':
    main()

