n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))
n4 = float(input('digite a quarta nota: '))

m = (n1 + n2 + n3 + n4)/4

if m < 6:
    print(f'estude mais, sua nota foi {m}')
else:
    print(f'parabens vc foi aprovado!!!')
    print(f'sua nota foi {m}')
       
