import random

cont = 0
user = 6
num = random.randint(0,10)

print ('----- Vamos jogar um jogo? -----\n')

while user != num:
    user = int(input('Tente adivinhar o número entre 0 e 10: '))
    cont += 1
    if num > user:
        print('Maior..... tente novamente!!!')
    elif num < user:
        print('Menos..... tente novamente!!!')

if user == num:
    print('\n')
    print('Comgratulations!!!')
    print(f'O número era {num}') 
    print(f'Foram nescerios {cont} palpites')
else:
    print('tente novamente')    