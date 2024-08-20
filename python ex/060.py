num = int(input('Digite um número: '))
i = 1
cont = 1

while i < num:
    i += 1
    cont = cont * i

print(f'\nO fatorial de {num} é {cont}')
