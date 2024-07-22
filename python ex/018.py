import math

angulo_graus = float(input('Digite o ângulo em graus: '))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'Seno do ângulo {angulo_graus}°: {seno:.2f}')
print(f'Cosseno do ângulo {angulo_graus}°: {cosseno:.2f}')
print(f'Tangente do ângulo {angulo_graus}°: {tangente:.2f}')
