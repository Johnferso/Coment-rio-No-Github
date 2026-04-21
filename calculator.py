#!/usr/bin/env python3
"""
Calculadora - Simple Calculator
Uma calculadora interativa com operacoes basicas
"""

def display_menu():
      """Display the calculator menu"""
      print("\n" + "="*50)
      print("   CALCULADORA - SIMPLE CALCULATOR")
      print("="*50)
      print("\nOperacoes disponiveis (Available operations):")
      print("1. Adicao (+)")
      print("2. Subtracao (-)")
      print("3. Multiplicacao (*)")
      print("4. Divisao (/)")
      print("5. Potencia (**)")
      print("6. Sair (Exit)")
      print("\nDigite o numero da operacao (Enter operation number)")

def get_numbers():
      """Get two numbers from user"""
      try:
                num1 = float(input("\nPrimeiro numero (First number): "))
                num2 = float(input("Segundo numero (Second number): "))
                return num1, num2
except ValueError:
        print("Erro! Digite numeros validos (Error! Enter valid numbers)")
        return None, None

def calculate(num1, num2, operation):
      """Perform calculation"""
      operations = {
          '1': (lambda a, b: a + b, "Adicao"),
          '2': (lambda a, b: a - b, "Subtracao"),
          '3': (lambda a, b: a * b, "Multiplicacao"),
          '4': (lambda a, b: a / b if b != 0 else None, "Divisao"),
          '5': (lambda a, b: a ** b, "Potencia"),
      }

    if operation not in operations:
              print("Operacao invalida! (Invalid operation!)")
              return None

    func, op_name = operations[operation]

    try:
              if operation == '4' and num2 == 0:
                            print("Erro: Nao e possivel dividir por zero! (Cannot divide by zero!)")
                            return None

              result = func(num1, num2)
              print(f"\n{num1} {op_name[0]} {num2} = {result}")
              return result
except Exception as e:
          print(f"Erro ao calcular: {e} (Error in calculation: {e})")
          return None

def main():
      """Main calculator loop"""
      print("\nBem-vindo a Calculadora! (Welcome to Calculator!)")

    history = []

    while True:
              display_menu()
              choice = input("\nSua escolha (Your choice): ").strip()

        if choice == '6':
                      print("\n" + "="*50)
                      print("Obrigado por usar a calculadora! (Thanks for using!)")
                      if history:
                                        print("\nHistorico (History):")
                                        for i, calc in enumerate(history, 1):
                                                              print(f"  {i}. {calc}")
                                                      print("="*50)
                                    break

        num1, num2 = get_numbers()
        if num1 is None or num2 is None:
                      continue

        result = calculate(num1, num2, choice)
        if result is not None:
                      history.append(f"{num1} (op {choice}) {num2} = {result}")

if __name__ == "__main__":
      main()
