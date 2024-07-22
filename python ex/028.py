import random
num = random.randint(0,5)
print ('Vamos jogar um jogo?')
user = 6
while user != num:
    user = int(input('Tente adivinhar o número entre 0 e 5: '))
    if user == num:
         print('Comgratulations!!!')
         print('VC acertou') 
    else:
         print('tente novamente')    