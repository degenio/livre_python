poids = float(input("Saisir votre poids:"))
taille = float(input("Saisir votre taille:"))
#Calcul imc selon la regle
imc = poids / (taille ** 2)
print("Votre imc est:{0:7.2f}".format(imc))