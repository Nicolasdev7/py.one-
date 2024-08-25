num, cont, soma = 0, 0, 0

while True:
    num = int(input('Digite um número (ou [999] para encerrar o programa): '))
    if num == 999:
        break
    cont += 1
    soma += num

print('\n=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Foram digitados {cont} números.')
print(f'A soma dos números é {soma}.')
