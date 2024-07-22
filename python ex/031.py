viajem = int(input('Digite a distancia da sua viagem em km: '))
if viajem <= 200:
    viajem = viajem * 0.50
    print(f'Sua viajem ficou no valor de R$ {viajem}0')
else:
    viajem = viajem * 0.45
    print(f'Sua viajem ficou no valor de R$ {viajem}0')
