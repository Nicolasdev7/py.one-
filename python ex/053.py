import re

frase = input('Digite uma frase: ')

frase = re.sub(r'[^a-zA-Z]', '', frase).lower()

if frase == frase[::-1]:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
