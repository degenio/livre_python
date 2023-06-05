# Prise en charge de FileNotFoundError et logs avec module csv
import getpass
import socket
import csv


def ecrire_log(fico):
    username = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    # ecrire le log
    with open(fico, 'a', newline='\n') as fo:
        ecriteur = csv.writer(fo, delimiter='|', quoting=csv.QUOTE_NONNUMERIC)
        try:
            ecriteur.writerow((username, hostname, ip))
        except FileNotFoundError as e:
            print('Probleme de fichier logs')


def traiter_casse(ficin, ficout):
    try:
        with open(ficin) as fi:
            with open(ficout, 'w') as fo:
                for ligne in fi:
                    if not ligne.strip().islower():
                        fo.write(ligne)
    except FileNotFoundError as e:
        print('Probleme de fichiers')
        ecrire_log('logs.csv')


if __name__ == '__main__':
    traiter_casse('cass.txt', 'sortie.txt')
