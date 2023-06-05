# version 1

def saisir_code_postal(message):
    return input(message)


def valider_code_postal(code):
    # Vérifier longueur
    if len(code) != 6:
        return 'Code invalide'
    else:
        c = [x for x in code[0:len(code):2] if not x.isdigit()]
        d = [x for x in code[1:len(code):2] if x.isdigit()]
    return len(c) == 3 and len(d) == 3 and code[0].upper() not in ["D", "F", "I", "O", "Q", "U", "W", "Z"]


def main():
    code_postal = saisir_code_postal('Saisir un code postal canadien:')
    resultat = valider_code_postal(code_postal)
    print(resultat)


if __name__ == '__main__':
    main()
