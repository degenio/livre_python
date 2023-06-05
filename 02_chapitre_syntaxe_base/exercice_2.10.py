nom_etudiant = input('Saisir le nom étudiant:')
examen_intra = float(input('Saisir la note intra:'))
examen_final = float(input('Saisir la note du final:'))
moyenne_etudiant = 0.4 * examen_intra + 0.6 * examen_final
print('Nom etudiant: {} Moyenne:{}'.format(nom_etudiant, moyenne_etudiant))