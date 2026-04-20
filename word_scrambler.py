#!/usr/bin/env python3
"""
Word Scrambler - Embaralhador de Palavras
A simple game that scrambles words and asks the player to guess the original word.
"""

import random
import string


def scramble_word(word):
      """Scrambles a word by rearranging its letters."""
      word_list = list(word.lower())
      random.shuffle(word_list)
      return ''.join(word_list)


def word_scrambler_game():
      """Main game loop for the word scrambler."""
      # Word list for the game
      words = [
          'python', 'programming', 'computer', 'developer',
          'algorithm', 'database', 'network', 'internet',
          'software', 'hardware', 'keyboard', 'monitor'
      ]

    score = 0
    round_num = 1

    print("=" * 50)
    print("   WORD SCRAMBLER - EMBARALHADOR DE PALAVRAS")
    print("=" * 50)
    print("\nWelcome! Try to guess the original word from its scrambled version.")
    print("Bem-vindo! Tente adivinhar a palavra original de sua versao embaralhada.\n")

    while True:
              if round_num > len(words):
                            print("\nGame Over! You completed all rounds!")
                            print(f"Final Score: {score}/{len(words)}")
                            break

              # Select a random word
              word = words[round_num - 1]
              scrambled = scramble_word(word)

        print(f"\nRound {round_num}: The scrambled word is: {scrambled.upper()}")

        # Get player's guess
        guess = input("Your guess (or 'quit' to exit): ").strip().lower()

        if guess == 'quit':
                      print(f"\nYou finished with a score of {score}/{round_num - 1}")
                      break

        # Check answer
        if guess == word:
                      print(f"✓ Correct! The word was '{word}'")
                      score += 1
else:
              print(f"✗ Wrong! The correct word was '{word}'")

        round_num += 1

    print("\nThanks for playing!")


if __name__ == "__main__":
      word_scrambler_game()
  
