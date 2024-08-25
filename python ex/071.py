while True:
    saque, decision, cinquenta, vinte, dez, um = 0, '', 0, 0, 0, 0

    print('\n=-=-=-=-=-=-=-=- Banco CV -=-=-=-=-=-=-=-=\n')
    saque = int(input('Que valor você deseja sacar? R$'))

    if saque > 0:
        if saque >= 50:
            cinquenta = saque // 50
        saque %= 50

        if saque >= 20:
            vinte = saque // 20
        saque %= 20
            
        if saque >= 10:
            dez = saque // 10
        saque %= 10

        if saque >= 1:
            um = saque // 1
        saque %= 1

        print(f'\nTotal de {cinquenta} cédulas de cinquenta')
        print(f'Total de {vinte} cédulas de vinte')
        print(f'Total de {dez} cédulas de dez')
        print(f'Total de {um} cédulas de um')

    else:
        print('\nDigite um valor maior que 0')

    decision = str(input('\nDeseja sacar outro valor [S/N]? ')).upper()
    while decision not in 'SN':
        decision = str(input('Deseja sacar outro valor [S/N]? ')).upper()
    if decision == 'N':
        break
