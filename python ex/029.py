carKm = float(input('Digite a quantos km/h o carro estava: '))
if carKm > 80:
    multa = 7*(carKm - 80)
    print(f'Você devera pagar a multa de {multa} por excesso de velocidade')
else:
    print('Velociadae permitida')    
