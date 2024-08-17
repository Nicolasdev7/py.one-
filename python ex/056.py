
nome = [0] * 4
idade = [0] * 4
sexo = [0] * 4

idadade_mais_velho = 0
nome_mais_velho  = ''
media_de_idade = 0
mulheres_com_menos_de_vinte = 0

for i in range(1,5):
    print(f'-----{i}° Pessoa -----')
    nome [i] = str(input('Digite seu nome: '))
    sexo [i] = str(input('Digite seu sexo(M/F): '))
    idade [i] = int(input('Digite sua idade: '))
    print('\n\n')

for i in range(4):
    if sexo[i].upper() == 'M' and idade[i] > idadade_mais_velho:
        nome_mais_velho = nome[i]
        idadade_mais_velho = idade[i]

for i in range(4):
    if sexo[i].upper() == 'F' and idade[i] < 20:
        mulheres_com_menos_de_vinte += + 1

media_de_idade = sum(idade) / 4

print(f'A media de idade do grupo é {media_de_idade}')
print(f'O homem mais velho é {nome_mais_velho} com a idade de {idadade_mais_velho}')
print(f'{mulheres_com_menos_de_vinte} mulheres possuem menos de vinte anos')
