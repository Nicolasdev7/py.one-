n = int(input('Digite o número inicial: '))
r = int(input('Digite o número referente à progressão: '))
i = 1

print(f'\nOs dez primeiros termos da progreção são')

while i < 11:
    print(f'{n}')
    n += r  
    i += +1

c = int(input('\nVoê quer printar mais quantos termos? '))
i = 0
print(f'\nOs próximos {c} da progreção são')

while i != c:
    print(f'{n}')
    n += r  
    i += +1
