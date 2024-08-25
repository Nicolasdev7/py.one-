produto, preco, tot_gasto, acima_de_mil, menor_preco, decisao = '', -1, 0, 0, None, ''

print('--------------------')
print('Loja baratão')
print('--------------------')

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))

    while preco <= 0:
       preco = float(input('Preço do produto (o preço deve ser maior que zero): ')) 

    tot_gasto += preco

    # Contagem de produtos com preço acima de 1000
    if preco >= 1000:
        acima_de_mil += 1

    # Verificação do menor preço
    if menor_preco is None or preco < menor_preco:
        menor_preco = preco

    # Pergunta se o usuário quer continuar
    decisao = str(input('Quer continuar (S/N)? ')).strip().upper()
    while decisao not in 'SN':
        decisao = str(input('Quer continuar (Por favor, digite S ou N)? ')).strip().upper()
    
    if decisao == 'N':
        break

# Exibição dos resultados
print(f'\nTotal gasto: R$ {tot_gasto:.2f}')
print(f'Produtos acima de R$ 1000: {acima_de_mil}')
print(f'Menor preço: R$ {menor_preco:.2f}')
