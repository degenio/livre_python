montant_remis = int(input('Saisir le montant remis:'))
montant_total = int(input('Saisir le montant total:'))
change = montant_remis - montant_total
cp_vingt = change // 20
cp_dix = (change % 20) // 10
cp_cinq = (change % 10) // 5
cp_un = change - cp_vingt * 20 - cp_dix * 10 - cp_cinq * 5
print('Vingt: {0}, Dix: {1}, Cinq:{2}, Un:{3}'.format(
    cp_vingt, cp_dix, cp_cinq, cp_un))