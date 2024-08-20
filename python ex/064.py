a, b = 0, 0 
soma = [a, b] 
cont = 0
num = 0 

while num != 999:
    print('\n----- [999] para encerrar o progama -----\n')
    num = int(input('Digite um número: '))
    a = num
    b = num + b
    soma =  b
    cont += +1

print(f'\nForam digitados {cont - 1} números')
print(f'Sendo o produto dos mesmos iquevalentes à {soma - 999}')