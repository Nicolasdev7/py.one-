valor  = float(input('Qual o valor do prduto? '))
metodo = int(input('Qualmetodo de pagamento? (1)à vista dinheiro/cheque (2)à vista no cartão (3)2x no cartão (4)3x ou mais no cartão: '))

if metodo == 1: #10% de desconto
    valor_Final = valor - valor * 0.1
    print(f'O preço final do produto sera R${valor_Final}')

elif metodo == 2: #5%
    valor_Final = valor - valor * 0.05
    print(f'O preço final do produto sera R${valor_Final}')

elif metodo == 3: #sem desconto
    print(f'O preço final do produto sera R${valor}')

elif metodo == 4: #20% juros
    valor_Final = valor + valor * 0.2
    print(f'O preço final do produto sera R${valor}')

else:
    print('ERRO!!!')
    print('Por favor digite um metodo disponivel')    
