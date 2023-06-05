def valider_mot_anagrame(mot_1, mot_2):
    # verifier longueur
    if len(mot_1) != len(mot_2):
        return False

    # construire dict mot 1
    dict_1 = {}
    for i, c in enumerate(mot_1):
        dict_1[i] = c
    # construire dict mot 2
    dict_2 = {}
    for i, c in enumerate(mot_2):
        dict_2[i] = c

    # Verifier anagrame
    for k in dict_1.keys():
        for m, n in dict_2.items():
            if dict_1[k] == n:
                dict_2.pop(m)
                break

    # Verifier la longueur de dict_2: autre que 0 indique que ce n'est pas un anagrame
    return len(dict_2) == 0


def main():
    mot_1 = input('Saisir le premier mot:')
    mot_2 = input('Saisir le deuxieme mot:')
    resultat = valider_mot_anagrame(mot_1.strip().lower(), mot_2.strip().lower())
    print('Les 2 mots {} anagrames '.format("sont des " if resultat else "ne sont pas des "))


if __name__ == '__main__':
    main()
