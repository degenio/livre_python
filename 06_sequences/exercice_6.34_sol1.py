# version 1 - utilisation de slicing sur str

def valider_mot_palindrome(mot):
    return mot == mot[::-1]


def main():
    mot = input('Saisir un mot:')
    resultat = valider_mot_palindrome(mot.strip().lower())
    print('Le mot {} palindrome '.format("est un " if resultat else "n'est pas un "))


if __name__ == '__main__':
    main()
