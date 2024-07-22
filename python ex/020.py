import random

aluno_1 = input('digite o nome do primiero aluno: ')
aluno_2 = input('digite o nome do segundo aluno: ')
aluno_3 = input('digite o nome do terciro aluno: ')
aluno_4 = input('digite o numero do quarto aluno: ')

alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(alunos)

print (f'lista de apresentação será {alunos}')

