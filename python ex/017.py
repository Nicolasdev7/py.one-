import math
C1 = float(input('Digite o primeiro cateto: '))
C2 = float(input('Digite o segundo cateto: '))
H = math.sqrt(pow(C1, 2)+pow(C2, 2))
print ('Sua hipotenusa será :{:.2f}' .format(H))