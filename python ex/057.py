sexo = ''

while (sexo != 'F' and 'M'):
    sexo = str(input('Digite seu sexo: ')).upper()
if  sexo == 'M':
    print('\n')
    print('Seu sexo é Masculino!!')
else:
    print('\n')
    print('Seu sexo é Feminino!!')
