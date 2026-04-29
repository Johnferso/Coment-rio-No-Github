# Calculadora de Juros Compostos
# Compound Interest Calculator
# Data: 2026-04-29
# Simple calculator to compute compound interest with monthly deposits

import math
from datetime import datetime


class CompoundInterestCalculator:
      """
          Uma classe simples para calcular juros compostos.
              A simple class to calculate compound interest.
                  """

    def __init__(self, principal: float, annual_rate: float, years: int):
              """
                      Inicializa a calculadora.
                              Initialize the calculator.

                                      Args:
                                                  principal: Valor inicial / Initial amount
                                                              annual_rate: Taxa anual (em %) / Annual interest rate (in %)
                                                                          years: Número de anos / Number of years
                                                                                  """
              self.principal = principal
              self.annual_rate = annual_rate / 100  # Converter percentual / Convert percentage
        self.years = years

    def calculate_compound_interest(self, compounds_per_year: int = 12) -> dict:
              """
                      Calcula juros compostos.
                              Calculate compound interest.

                                      Args:
                                                  compounds_per_year: Vezes por ano que os juros são compostos
                                                                                 Times per year interest is compounded

                                                                                         Returns:
                                                                                                     Dictionary com resultados / Dictionary with results
                                                                                                             """
              n = compounds_per_year
              t = self.years
              r = self.annual_rate
              p = self.principal

        # Fórmula: A = P(1 + r/n)^(nt)
              amount = p * math.pow((1 + r / n), n * t)
              interest_earned = amount - p

        return {
                      'principal': round(p, 2),
                      'final_amount': round(amount, 2),
                      'interest_earned': round(interest_earned, 2),
                      'annual_rate': self.annual_rate * 100,
                      'years': t,
                      'compounds_per_year': n
        }

    def calculate_with_monthly_deposits(self, monthly_deposit: float) -> dict:
              """
                      Calcula com depósitos mensais regulares.
                              Calculate with regular monthly deposits.

                                      Args:
                                                  monthly_deposit: Depósito mensal / Monthly deposit amount

                                                          Returns:
                                                                      Dictionary com resultados / Dictionary with results
                                                                              """
              r = self.annual_rate / 12  # Taxa mensal / Monthly rate
        n_months = self.years * 12

        # Valor final do principal / Final value of principal
        principal_final = self.principal * math.pow((1 + r), n_months)

        # Valor final dos depósitos / Final value of deposits
        # Fórmula da série geométrica / Geometric series formula
        deposits_final = monthly_deposit * (((math.pow((1 + r), n_months) - 1) / r))

        total_amount = principal_final + deposits_final
        total_deposited = self.principal + (monthly_deposit * n_months)
        interest_earned = total_amount - total_deposited

        return {
                      'principal': round(self.principal, 2),
                      'monthly_deposit': round(monthly_deposit, 2),
                      'total_deposited': round(total_deposited, 2),
                      'final_amount': round(total_amount, 2),
                      'interest_earned': round(interest_earned, 2),
                      'years': self.years,
                      'annual_rate': self.annual_rate * 100
        }


def display_results(title: str, results: dict):
      """
          Exibe resultados formatados.
              Display formatted results.
                  """
      print(f"\n{'='*50}")
      print(f"{title}")
      print(f"{'='*50}")
      for key, value in results.items():
                formatted_key = key.replace('_', ' ').title()
                print(f"{formatted_key}: {value}")


# Main execution
if __name__ == "__main__":
      print("╔════════════════════════════════════════════════════╗")
      print("║  Calculadora de Juros Compostos                    ║")
      print("║  Compound Interest Calculator                      ║")
      print("╚════════════════════════════════════════════════════╝")

    # Exemplo 1: Juros simples / Simple compound interest
      calc1 = CompoundInterestCalculator(principal=1000, annual_rate=5, years=5)
      results1 = calc1.calculate_compound_interest(compounds_per_year=12)
      display_results("Exemplo 1: Juros Compostos Mensais / Example 1: Monthly Compound Interest", results1)

    # Exemplo 2: Com depósitos mensais / With monthly deposits
      calc2 = CompoundInterestCalculator(principal=500, annual_rate=8, years=10)
      results2 = calc2.calculate_with_monthly_deposits(monthly_deposit=100)
      display_results("Exemplo 2: Com Depósitos Mensais / Example 2: With Monthly Deposits", results2)

    # Exemplo 3: Teste rápido / Quick test
      calc3 = CompoundInterestCalculator(principal=2000, annual_rate=6, years=3)
      results3 = calc3.calculate_compound_interest()
      display_results("Exemplo 3: 3 Anos a 6% / Example 3: 3 Years at 6%", results3)

    print("\n✓ Calculadora funcionando corretamente!")
    print("✓ Calculator working correctly!")
