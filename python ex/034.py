salario = float(input('Digite o salario do funcionario: '))
if salario > 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print(f'O funcionario devera receber um novo salario de R${salario:.2f}')
