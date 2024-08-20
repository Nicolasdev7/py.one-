a = 0
b = 1
i = 0
termos = [a,b]

numero = int(input('Quantos termos da sequencia de fibonate vc quer imprimir? '))
print(f'Os {numero} primeiros da sequênca de fibonate sâo\n')

while i < numero:
    a, b = b, a + b
    termos.append(b)
    i += + 1
print(f'{termos}')
