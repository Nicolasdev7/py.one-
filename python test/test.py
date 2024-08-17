nome = [0] * 4
idade = [0] * 4
sexo = [0] * 4

idade_mais_velho = -1
nome_mais_velho = ''
media_de_idade = 0
mulheres_com_menos_de_vinte = 0

for i in range(4):
    nome[i] = str(input('Digite seu nome: '))
    sexo[i] = str(input('Digite seu sexo (M/F): '))
    idade[i] = int(input('Digite sua idade: '))
    print('\n\n')

# Encontrar o homem mais velho
for i in range(4):
    if sexo[i].upper() == 'M' and idade[i] > idade_mais_velho:
        idade_mais_velho = idade[i]
        nome_mais_velho = nome[i]

# Contar o número de mulheres com menos de 20 anos
for i in range(4):
    if sexo[i].upper() == 'F' and idade[i] < 20:
        mulheres_com_menos_de_vinte += 1

# Calcular a média de idade
media_de_idade = sum(idade) / 4

print(f'A média de idade do grupo é {media_de_idade}')
if nome_mais_velho:
    print(f'O homem mais velho é {nome_mais_velho} com {idade_mais_velho} anos')
else:
    print("Não há homens na lista.")
print(f'{mulheres_com_menos_de_vinte} mulher(es) possuem menos de vinte anos')