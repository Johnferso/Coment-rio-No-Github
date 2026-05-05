#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de Juros Compostos / Compound Interest Calculator
Projeto educacional para cálculo de juros compostos
Educational project for compound interest calculation

Author: Coment-rio No Github
Date: 2026-05-05
"""

def calculate_compound_interest(principal, rate, time, compounds_per_year=12):
      r = rate / 100
      n = compounds_per_year
      t = time
      amount = principal * (1 + r / n) ** (n * t)
      interest = amount - principal
      return {
          'principal': principal,
          'amount': round(amount, 2),
          'interest': round(interest, 2),
          'rate': rate,
          'time': time,
          'compounds_per_year': compounds_per_year
      }

def display_result(result):
      print("\n" + "="*50)
      print("CALCULADORA DE JUROS COMPOSTOS")
      print("COMPOUND INTEREST CALCULATOR")
      print("="*50)e_compound_interest(example['principal'], example['rate'], example['time'], example['compounds'])
          display_result(result)

if __name__ == "__main__":
      print("\n1. Calculadora Interativa / Interactive Calculator")
    print("2. Ver Exemplos / View Examples")
    choice = input("\nEscolha uma opção (1 ou 2) / Choose an option (1 or 2): ").strip()
    if choice == "1":
              interactive_calculator()
    elif choice == "2":
        example_calculations()
else:
        print("❌ Opção inválida! / Invalid option!")
      print(f"Capital Inicial / Initial Capital: R$ {result['principal']:.2f}")
      print(f"Taxa Anual / Annual Rate: {result['rate']}%")
      print(f"Período / Time Period: {result['time']} anos / years")
      print(f"Composição / Compounding: {result['compounds_per_year']}x ao ano / per year")
      print("-"*50)
      print(f"Montante Final / Final Amount: R$ {result['amount']:.2f}")
      print(f"Juros Ganhos / Interest Earned: R$ {result['interest']:.2f}")
      print("="*50 + "\n")

def interactive_calculator():
      print("\n🎯 Bem-vindo à Calculadora de Juros Compostos!")
      print("🎯 Welcome to the Compound Interest Calculator!\n")
      try:
                principal = float(input("Capital inicial (R$) / Initial capital: "))
                rate = float(input("Taxa anual (%) / Annual rate (%): "))
                time = float(input("Tempo (anos) / Time (years): "))
                compounds = input("Composição anual? (mensal=12, trimestral=4, anual=1) / Compounds per year? (monthly=12, quarterly=4, yearly=1): ")
                compounds = int(compounds) if compounds else 12
                if principal <= 0 or rate < 0 or time <= 0:
                              print("❌ Valores inválidos! / Invalid values!")
                              return
                          result = calculate_compound_interest(principal, rate, time, compounds)
                display_result(result)
except ValueError:
        print("❌ Erro ao ler valores! / Error reading values!")

def example_calculations():
      examples = [
                {'principal': 1000, 'rate': 5, 'time': 10, 'compounds': 12},
                {'principal': 5000, 'rate': 8, 'time': 5, 'compounds': 12},
                {'principal': 10000, 'rate': 3, 'time': 20, 'compounds': 12},
      ]
      print("\n📊 EXEMPLOS DE CÁLCULO / EXAMPLE CALCULATIONS:")
      for example in examples:
                result = calculat
