casa = float(input('Quanto custa a casa? '))
salario = float(input('Qual sua média salarial? '))
prazo = int(input('Quantos meses você pretende quitar a casa? '))

mensalidade = casa / prazo
limite_salarial = salario * 0.3

if mensalidade > limite_salarial:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Seu empréstimo não poderá ser aprovado pois os dados informados não estão de acordo com a política da empresa.')
else:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('Seu empréstimo foi aprovado!')
    print(f'As parcelas ficarão em R${mensalidade:.2f} para serem quitadas em {prazo} meses.')
