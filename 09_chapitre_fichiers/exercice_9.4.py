#Solution de base
def traiter_casse_op1(infile, outfile):
    output = open(outfile, "w")
    for ligne in open(infile):
        print(ligne.strip())
        if not ligne.strip()[0] in "abcdefghijklmnopqrstuvwxyz":
            output.write(ligne)
    output.close()


#Solution 2 avec la fonction built-in isupper()
def traiter_casse_op2(infile, outfile):
    output = open(outfile, "w")
    for ligne in open(infile):
        if ligne.strip()[0].isupper():
            output.write(ligne)
    output.close()


#Solution 3  avec with open sur les deux fichiers
def traiter_casse_op3(infile, outfile):
    with open(outfile, "w") as output, open(infile, 'r', encoding='windows-1252') as input:
        for ligne in input:
            if ligne.strip()[0].isupper():
                output.write(ligne)

def main():
    traiter_casse_op1("casse.txt", "sortie.txt")
    traiter_casse_op2("casse.txt", "sortie.txt")
    traiter_casse_op3("casse.txt", "sortie.txt")

if __name__ == '__main__':
    main()
