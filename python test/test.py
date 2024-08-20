import math

def menu():
    print("\n--- Calculadora Científica ---")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("5: Exponenciação")
    print("6: Raiz Quadrada")
    print("7: Seno")
    print("8: Cosseno")
    print("9: Tangente")
    print("10: Logaritmo (base 10)")
    print("11: Logaritmo Natural (base e)")
    print("12: Fatorial")
    print("13: Área de um Círculo")
    print("14: Perímetro de um Círculo")
    print("15: Área de um Triângulo")
    print("16: Sair")

def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

def exponenciar(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Erro! Raiz de número negativo."
    else:
        return math.sqrt(x)

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x):
    if x <= 0:
        return "Erro! Logaritmo de número não positivo."
    else:
        return math.log10(x)

def logaritmo_natural(x):
    if x <= 0:
        return "Erro! Logaritmo de número não positivo."
    else:
        return math.log(x)

def fatorial(x):
    if x < 0:
        return "Erro! Fatorial de número negativo."
    else:
        return math.factorial(x)

def area_circulo(raio):
    return math.pi * (raio ** 2)

def perimetro_circulo(raio):
    return 2 * math.pi * raio

def area_triangulo(base, altura):
    return 0.5 * base * altura

def main():
    while True:
        menu()
        escolha = input("Escolha uma opção (1-16): ")
        
        if escolha == '16':
            print("Encerrando a calculadora...")
            break
        
        elif escolha in ('1', '2', '3', '4', '5'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print("Resultado: ", adicionar(num1, num2))
            
            elif escolha == '2':
                print("Resultado: ", subtrair(num1, num2))
            
            elif escolha == '3':
                print("Resultado: ", multiplicar(num1, num2))
            
            elif escolha == '4':
                print("Resultado: ", dividir(num1, num2))
            
            elif escolha == '5':
                print("Resultado: ", exponenciar(num1, num2))
        
        elif escolha == '6':
            num = float(input("Digite o número: "))
            print("Resultado: ", raiz_quadrada(num))
        
        elif escolha == '7':
            angulo = float(input("Digite o ângulo em graus: "))
            print("Resultado: ", seno(angulo))
        
        elif escolha == '8':
            angulo = float(input("Digite o ângulo em graus: "))
            print("Resultado: ", cosseno(angulo))
        
        elif escolha == '9':
            angulo = float(input("Digite o ângulo em graus: "))
            print("Resultado: ", tangente(angulo))
        
        elif escolha == '10':
            num = float(input("Digite o número: "))
            print("Resultado: ", logaritmo(num))
        
        elif escolha == '11':
            num = float(input("Digite o número: "))
            print("Resultado: ", logaritmo_natural(num))
        
        elif escolha == '12':
            num = int(input("Digite um número inteiro: "))
            print("Resultado: ", fatorial(num))
        
        elif escolha == '13':
            raio = float(input("Digite o raio do círculo: "))
            print("Área do círculo: ", area_circulo(raio))
        
        elif escolha == '14':
            raio = float(input("Digite o raio do círculo: "))
            print("Perímetro do círculo: ", perimetro_circulo(raio))
        
        elif escolha == '15':
            base = float(input("Digite a base do triângulo: "))
            altura = float(input("Digite a altura do triângulo: "))
            print("Área do triângulo: ", area_triangulo(base, altura))
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
