n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

m = (n1 + n2) / 2

if m < 5.0:
    print('Aluno REPROVADO!!!')

elif m >= 7:
    print('Aluno APROVADO!!!')

else:
    print('Aluno de RECUPERAÇÃO!!!')
            