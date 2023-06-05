# Déterminer le total de nombre pairs pour obtenir un nombre donné
a = int(input('Saisir a:'))
sum = 0
i = 1
while sum < a:
    print(2 * i)
    sum += 2 * i
    i += 1

print('On a besoin des {} premiers nombres pairs'.format(i - 1))
