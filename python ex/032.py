ano = int(input('Enque anos nos estamo? '))
if ano % 4 == 0 and ano % 10 == 0 and ano % 400 == 0:
    print(f'{ano} É um ano bissexto')
else:
    print(f'{ano} Não é um ano bissexto')
