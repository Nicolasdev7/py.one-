decisao, idade, sexo, cont_menos_18, cont_menos_20, cont_homens = '', 0, '', 0, 0, 0

print('--------------------')
print('Cadastre uma pessoa')
print('--------------------')

while True:
    idade = int(input('\nDigite sua idade: '))

    while idade <= 0:
        print('Idade inválida. Digite um valor maior que zero.')
        idade = int(input('\nDigite sua idade: '))
    
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()
        if sexo not in 'MF':
            print('Sexo inválido. Por favor, digite M ou F.')

    if idade < 18:
        cont_menos_18 += 1

    if sexo == 'M':
        cont_homens += 1

    if sexo == 'F' and idade < 20:
        cont_menos_20 += 1

    decisao = str(input('\nQuer continuar? (S/N) ')).strip().upper()
    while decisao not in 'SN':
        decisao = str(input('\nQuer continuar? (S/N) ')).strip().upper()

    if decisao == 'N':
        break

    print('\n--------------------')
    print('Cadastre uma pessoa')
    print('--------------------')

print('\n-----------------------------------')
print(f'Foram cadastrados\n\n{cont_homens} Homen(s)\n{cont_menos_20} Mulher(es) com menos de vinte anos\n{cont_menos_18} Pessoa(s) com menos de 18 anos')
