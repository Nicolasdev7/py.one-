from time import sleep

n1 = 0 
n2 = 0
user = 0 
result = 0

n1 = int(input('Digite o primeiro numéro: '))
n2 = int(input('Digite o segundo número: '))

while user != 5:
    sleep(2)
    print('\n\n----- Menu -----\n')
    user = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior Número\n[4]Novos Números\n[5]Encerrar Programa\n\n'))
    print('\n')
    if user == 1:
        result = n1 + n2
        print(f'O resultado da soma de {n1} e {n2} é {result}!!!')
    elif user == 2:
        result = n1 * n2
        print(f'O resultado da multiplicação entre {n1} e {n2} é {result}!!!')
    elif user == 3:
        if n1 > n2:
            result = n1
            print(f'O maior número é {result}')
        elif n2 > n1:
            result = n2
        else:
            print('Os valores são iguais')
    elif user == 4:
        n1 = int(input('Digite o primeiro numéro: '))
        n2 = int(input('Digite o segundo número: '))
    elif user == 5:
        print('---- FIM DO PROGRAMA ----')    
    else:
        print('Função não encontrada')    
