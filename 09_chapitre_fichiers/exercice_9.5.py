# version 1: Solution basique
input = open("heures.csv")
for ligne in input:
    code, nom, j1, j2, j3, j4, j5 = ligne.split()

    # Moyenne
    heures = float(j1) + float(j2) + float(j3) + \
             float(j4) + float(j5)

    print(nom, "Code:", code, " a travaillé:", \
          heures, "heures avec une moyenne de:  ", heures / 5, "/ jour")
input.close()

# version 2
input = open("heures.csv")
for ligne in input:
    res = ligne.split()
    # Moyenne
    heures = float(res[2]) + float(res[3]) + float(res[4]) + \
             float(res[5]) + float(res[6])
    print('{0:<10s} Code: {1:<3s}  a travaillé:{2:7.2f}  '
          'heures avec une moyenne de {3:7.2f} / jour'.format(res[1], res[0], heures, heures / 5))
input.close()

# version 3: slicing et list comprehension
with open("heures.csv") as input:
    for ligne in input:
        res = ligne.split()
        # Moyenne
        heures = sum([float(x) for x in res[2:7]])
        print('{0:<10s} Code: {1:<3s}  a travaillé:{2:7.2f}  '
              'heures avec une moyenne de {3:7.2f} / jour'.format(res[1], res[0], heures, heures / 5))
