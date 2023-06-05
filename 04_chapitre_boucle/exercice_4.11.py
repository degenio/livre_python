phrase = input('Saisir une phrase:')
longueur = len(phrase)
print('Le nombre de caractères est:{}'.format(longueur))
#nombre de repétition de la lettre a
compteur = 0
for tmp in phrase:
    if tmp =='a':
        compteur += 1
print('Le caractere {} se retrouve {} fois'.format('a', compteur))

#nombre de repétition de la lettre a ou A
compteur = 0
for tmp in phrase:
    if tmp in ['a','A']:
        compteur += 1
print('Le caractere {} ou {} se retrouve {} fois'.format('a', 'A', compteur))
