# Solicita o peso e a altura ao usuário
peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em metros): '))

# Calcula o IMC
imc = peso / (altura ** 2)

# Interpreta o resultado do IMC
if imc < 18.5:
    resultado = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    resultado = "Peso normal"
elif 25 <= imc < 29.9:
    resultado = "Sobrepeso"
else:
    resultado = "Obesidade"

# Exibe o resultado
print(f'Seu IMC é: {imc:.2f}')
print(f'Interpretação: {resultado}')
