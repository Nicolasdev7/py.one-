num = int(input('Digite o numero: '))
num_convert = int(input('Para convertê-lo para binário (1), para octal (2), para hexadecimal (3): '))

if num_convert == 1: # conversão para binário
    print(f'O número {num} em binário é {bin(num)[2:]}.')

elif num_convert == 2: # conversão para octal
    print(f'O número {num} em octal é {oct(num)[2:]}.')

elif num_convert == 3: # conversão para hexadecimal
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}.')
    
else:
    print('ERRO!!!')

print('=-=-=-=-=-=-=-=-=-=-=')

