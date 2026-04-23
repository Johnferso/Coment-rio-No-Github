# Calculadora Simples / Simple Calculator
# Data / Date: 2026-04-23
# Projeto para aprender operações básicas / Project to learn basic operations

def adicionar(a, b):
      """Adiciona dois números / Adds two numbers"""
      return a + b

def subtrair(a, b):
      """Subtrai dois números / Subtracts two numbers"""
      return a - b

def multiplicar(a, b):
      """Multiplica dois números / Multiplies two numbers"""
      return a * b

def dividir(a, b):
      """Divide dois números / Divides two numbers"""
      if b == 0:
                return "Erro: Divisão por zero / Error: Division by zero"
            return a / b

def potencia(a, b):
      """Calcula a potência / Calculates power"""
    return a ** b

def raiz_quadrada(a):
      """Calcula a raiz quadrada / Calculates square root"""
    if a < 0:
              return "Erro: Número negativo / Error: Negative number"
          return a ** 0.5

def main():
      """Função principal / Main function"""
    print("=" * 50)
    print("CALCULADORA SIMPLES / SIMPLE CALCULATOR")
    print("=" * 50)

    while True:
              print("\nOperações / Operations:")
              print("1. Adição (+) / Addition")
              print("2. Subtração (-) / Subtraction")
              print("3. Multiplicação (*) / Multiplication")
              print("4. Divisão (/) / Division")
              print("5. Potência (**) / Power")
              print("6. Raiz Quadrada / Square Root")
              print("7. Sair / Exit")

        escolha = input("\nEscolha uma operação / Choose an operation (1-7): ").strip()

        if escolha == '7':
                      print("Até logo! / Goodbye!")
                      break

        if escolha == '6':
                      try:
                                        num = float(input("Digite o número / Enter the number: "))
                                        resultado = raiz_quadrada(num)
                                        print(f"Resultado / Result: √{num} = {resultado}")
except ValueError:
                print("Erro de entrada / Input error!")
elif escolha in ['1', '2', '3', '4', '5']:
            try:
                              num1 = float(input("Primeiro número / First number: "))
                              num2 = float(input("Segundo número / Second number: "))

                if escolha == '1':
                                      print(f"Resultado / Result: {num1} + {num2} = {adicionar(num1, num2)}")
elif escolha == '2':
                    print(f"Resultado / Result: {num1} - {num2} = {subtrair(num1, num2)}")
elif escolha == '3':
                    print(f"Resultado / Result: {num1} * {num2} = {multiplicar(num1, num2)}")
elif escolha == '4':
                    print(f"Resultado / Result: {num1} / {num2} = {dividir(num1, num2)}")
elif escolha == '5':
                    print(f"Resultado / Result: {num1} ** {num2} = {potencia(num1, num2)}")
except ValueError:
                print("Erro de entrada / Input error!")
else:
            print("Opção inválida / Invali
