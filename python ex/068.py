from random import randint

jogador, cont, result, decision = 0, 0, 0, ''

print('=-=-=- Vamos jogar um jogo -=-=-=')

while True:
    computador = randint(1, 10)
    
    # Validar se o jogador escolhe Par ou Ímpar corretamente
    decision = str(input('\nPar ou Impar? [P/I]: ')).strip().upper()
    while decision not in 'PI':
        decision = str(input('Opção inválida. Escolha Par ou Ímpar [P/I]: ')).strip().upper()

    # Validar se o jogador escolhe um número entre 1 e 10
    jogador = int(input('Escolha um número de 1 a 10: '))
    while jogador < 1 or jogador > 10:
        jogador = int(input('Número inválido. Escolha um número entre 1 e 10: '))

    result = jogador + computador

    # Verificar se o resultado é Par ou Ímpar
    if (decision == 'P' and result % 2 == 0) or (decision == 'I' and result % 2 != 0):
        print(f'\nVocê ganhou! O computador escolheu {computador} e você {jogador}. Total: {result}')
        cont += 1
    else:
        print(f'\nVocê perdeu! O computador escolheu {computador} e você {jogador}. Total: {result}')
        break

print('\n=-=-=- FIM DO JOGO -=-=-=')
print(f'Você ganhou {cont} vez(es) seguidas!')
