from random import randint

TAILLE_LETTRE = 4
TAILLE_NBRE = 4
ASCII_DEBUT = 65
ASCII_FIN = 90
num =0

def code_generation():
    global num
    code = ''
    if num == 9999:
        num = 0
    num += 1
    #generer les lettres
    for i in range(0,TAILLE_LETTRE):
        #generer un nombre aleatoire pour avoir une lettre majuscule
        nbre = randint(ASCII_DEBUT,ASCII_FIN)
        code += chr(nbre)

    #Former le code en effectuant un padding si nécessaire
    return code + str(num).zfill(TAILLE_NBRE)


#Appel de la fonction
code1 = code_generation()
code2 = code_generation()

#Affichage du code
print('Le code est:{}'.format(code1))
print('Le code est:{}'.format(code2))