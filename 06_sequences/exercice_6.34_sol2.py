# version 1 - utilisation de slicing sur str
#Palindrome sur une phrase au lieu d'un mot

def valider_phrase_palindrome(phrase):
    #Tenir compte que des lettres et des chiffres en utilisant isalnum()
    phrase = ''.join([x for x in phrase.strip().lower() if x.isalnum()])
    print(phrase)
    return phrase == phrase[::-1]


def main():
    mot = input('Saisir une phrase:')
    resultat = valider_phrase_palindrome(mot.strip().lower())
    print('La phrase {} palindrome '.format("est un " if resultat else "n'est pas un "))


if __name__ == '__main__':
    main()
