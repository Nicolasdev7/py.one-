print('Será possível formar um triângulo?')

a = int(input('Digite o segmento a: '))
b = int(input('Digite o segmento b: '))
c = int(input('Digite o segmento c: '))

if a + b > c and a + c > b and b + c > a:
    print('Sim, você pode formar um triângulo!!!')
else:
    print('Não, você não pode formar um triângulo com essas medidas.')
