def calcul_change(montant_total, montant_remis):
    '''
    Calcul du change à remettre en coupure de billets de banque
    
    :param montant_total: Le montant total à payer
    :param montant_remis: Le montant remis par le client
    :return: Un tuple des coupures à remettre en billets 
    de 20$, 10$, 5$ et 1$
    '''
    change = montant_remis - montant_total
    cp_vingt = change // 20
    cp_dix = (change % 20) // 10
    cp_cinq = (change % 10) // 5
    cp_un = change - cp_vingt * 20 - cp_dix * 10 - cp_cinq * 5
    return cp_vingt, cp_dix, cp_cinq, cp_un


# Appel de la fonction
remise = calcul_change(95, 98)
print('Vingt: {0}, Dix: {1}, Cinq:{2}, Un:{3}'.format(
    remise[0], remise[1], remise[2], remise[3]))
