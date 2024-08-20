a, b = 0, 0 
soma = [a, b] 
cont = 0
decisão = ''

num = int(input('\nDigite um número: '))
termos = [num]

while decisão != 'N':
    num = int(input('\nDigite um número: '))
    decisão = str(input('\nDeseja continuar o programa?[N/S]')).upper().strip() [0]
    a = num
    b = num + b
    soma =  b
    cont += +1
    termos.append(num)

M = max(termos)
m = min(termos)
media = soma / cont 
print(f'\nA média foi: {media}')
print(f'Sendo o maior {M} e o menor {m}')