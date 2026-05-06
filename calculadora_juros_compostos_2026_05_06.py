"""
Calculadora de Juros Compostos
Compound Interest Calculator

Uma ferramenta educacional para calcular juros compostos.
An educational tool to calculate compound interest.

Author: Daily GitHub Project
Date: 2026-05-06
"""

def calcular_juros_compostos(principal, taxa_anual, tempo_anos, composicoes_ano=12):
      """
          Calcula o valor final com juros compostos.
              Calculates the final amount with compound interest.

                  Args:
                          principal (float): Valor inicial / Initial amount
                                  taxa_anual (float): Taxa de juros anual em % / Annual interest rate in %
                                          tempo_anos (float): Período em anos / Time period in years
                                                  composicoes_ano (int): Vezes que juros são compostos por ano / Compounding periods per year

                                                      Returns:
                                                              tuple: (valor_final, juros_ganhos) / (final_amount, interest_earned)
                                                                  """
      # Converter taxa percentual para decimal
      # Convert percentage rate to decimal
      taxa = taxa_anual / 100

    # Fórmula: A = P(1 + r/n)^(nt)
      # Formula: A = P(1 + r/n)^(nt)
      valor_final = principal * (1 + taxa / composicoes_ano) ** (composicoes_ano * tempo_anos)

    # Juros ganhos
      # Interest earned
      juros_ganhos = valor_final - principal

    return valor_final, juros_ganhos


def exibir_menu():
      """
          Exibe o menu principal.
              Display the main menu.
                  """
      print("\n" + "="*50)
      print("Calculadora de Juros Compostos")
      print("Compound Interest Calculator")
      print("="*50)
      print("1. Calcular juros compostos / Calculate compound interest")
      print("2. Comparar diferentes taxas / Compare different rates")
      print("3. Sair / Exit")
      print("="*50)


def calcular_simples():
      """
          Modo simples de cálculo.
              Simple calculation mode.
                  """
      try:
                principal = float(input("\nValor inicial (Principal): R$ "))
                taxa = float(input("Taxa de juros anual (Annual rate): % "))
                anos = float(input("Período em anos (Years): "))
                composicoes = int(input("Composições por ano (Compounding periods/year) [padrão: 12]: ") or "12")

          valor_final, juros = calcular_juros_compostos(principal, taxa, anos, composicoes)

        print(f"\n{'='*40}")
        print(f"Valor Inicial / Initial Amount: R$ {principal:,.2f}")
        print(f"Taxa Anual / Annual Rate: {taxa}%")
        print(f"Período / Period: {anos} anos/years")
        print(f"{'='*40}")
        print(f"Juros Ganhos / Interest Earned: R$ {juros:,.2f}")
        print(f"Valor Final / Final Amount: R$ {valor_final:,.2f}")
        print(f"{'='*40}\n")

except ValueError:
        print("Erro: Digite valores numéricos válidos / Error: Enter valid numeric values")


def comparar_taxas():
      """
          Compara diferentes taxas de juros.
              Compare different interest rates.
                  """
    try:
              principal = float(input("\nValor inicial (Principal): R$ "))
              anos = float(input("Período em anos (Years): "))

        print(f"\n{'='*50}")
        print("Comparação de Taxas / Rate Comparison")
        print(f"{'='*50}")

        taxas = [4, 6, 8, 10, 12]
        for taxa in taxas:
                      valor_final, juros = calcular_juros_compostos(principal, taxa, anos)
                      print(f"{taxa}%: R$ {valor_final:>10,.2f} (Juros/Interest: R$ {juros:>10,.2f})")

        print(f"{'='*50}\n")

except ValueError:
        print("Erro: Digite valores numéricos válidos / Error: Enter valid numeric values")


def main():
      """
          Função principal / Main function
              """
    while True:
              exibir_menu()
              opcao = input("Escolha uma opção / Choose an option: ").strip()

        if opcao == "1":
                      calcular_simples()
elif opcao == "2":
            comparar_taxas()
elif opcao == "3":
            print("\nObrigado por usar a Calculadora!")
            print("Thank you for using the Calculator!\n")
            break
else:
            print("Opção inválida / Invalid option!")


if __name__ == "__main__":
      main()
