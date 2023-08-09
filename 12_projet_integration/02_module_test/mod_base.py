risque=['Accru','Moindre','Accru','Élevé','Très élevé','Extrêmement élevé']
classification=['Poids insuffisant','Poids normal',
'Excès de poids','Obésité, classe I','Obésité, classe II','Obésité, classe III']

poids = float(input("Saisir votre poids:"))
taille = float(input("Saisir votre taille:"))
#Calcul imc selon la regle
imc = poids / (taille ** 2)
print("Votre imc est:{0:7.2f}".format(imc))
#Determination risque et classification
if imc < 18.5:
    index  = 0
elif imc < 25:
    index = 1
elif imc < 30:
    index  =2
elif imc < 35:
    index = 3
elif imc < 40:
    index = 4
else:
    index = 5

print('Classfication:{}'.format(classification[index]))
print('Risque:{}'.format(risque[index]))