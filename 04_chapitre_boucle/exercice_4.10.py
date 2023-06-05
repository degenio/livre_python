flag = True
while flag:
    print("================")
    print("1.Addition")
    print("2.Soustraction")
    print("3.Multiplication")
    print("4.Quitter")
    print("================")
    option = int(input("Saisir une option de menu 1-4:"))

    if option ==4:
        print("Merci d’avoir utilisé notre application")
        flag = False
    elif 1<=option<=3 :
        a = int(input("Saisir le premier nombre:"))
        b = int(input("Saisir le deuxieme nombre:"))
        if option ==1:
            resultat = a+b
        elif option ==2:
            resultat = a-b
        else:
            resultat = a * b
        print("Resultat de l'opération:{}".format(resultat))
    else:
        print("Option de menu non valide")