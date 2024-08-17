import random
pc = random.randint(1, 3)

# tabela: 1 = pedra 2 = papeu 3 = teosura 

user = int(input('Escolha o seu obijeto: tabela: 1 = pedra 2 = papeu 3 = teosura '))

if user == 1 and pc == 1 or user == 2 and pc == 2 or user == 3 and pc == 3:
    print('IMPATE!!!')

elif user == 1 and pc == 3 or user == 2 and pc == 1 or user == 3 and pc == 2:
    print('VOCÊ GANHOU!!!')

elif user == 1 and pc == 2 or user == 2 and pc == 3 or user == 3 and pc == 1:
    print('VOCÊ PERDEU!!!')        

else:
    print('ERRO!!!')
    print('Por favor digite uma opção disponivel')
