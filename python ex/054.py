from datetime import date

const = 0 
idade = 0 
defer = 0
atual = date.today().year

for i in range (7):
    idade = int(input('Digite o ano que vc naceu: '))
    idade = atual - idade
    if idade >= 21:
        const = const + 1

    else: 
        defer += + 1
print(f'{const} pessoas ja atigingiram a maior idade')           
print(f'{defer} pessoas ainda não atigingiram a maior idade')    