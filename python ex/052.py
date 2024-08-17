tot = 0
num = int(input('Digite um número: '))

print('\n')

for i in range(1, num + 1):
  
        tot += 1
  

print('\n')

if tot == 2:
    print(f'{num} é um número primo')
else:
    print(f'{num} não é um numero primo')    
