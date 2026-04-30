#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Word Scrambler Game / Jogo Embaralhador de Palavras
A fun game where players guess original words from scrambled versions.
Um jogo divertido onde jogadores adivinham palavras originais de versões embaralhadas.
"""

import random
import os
from typing import List, Tuple

class WordScrambler:
      """
          A word scrambler game class.
              Classe para um jogo de embaralhador de palavras.
                  """

    def __init__(self, words: List[str]):
              """
                      Initialize the game with a list of words.
                              Inicializa o jogo com uma lista de palavras.
                                      """
              self.words = words
              self.score = 0
              self.current_word = None
              self.scrambled_word = None
              self.attempts = 0

    def scramble_word(self, word: str) -> str:
              """
                      Scramble a word randomly.
                              Embaralha uma palavra aleatoriamente.
                                      """
              letters = list(word.lower())
              random.shuffle(letters)
              return ''.join(letters)

    def start_round(self) -> Tuple[str, str]:
              """
                      Start a new round with a random word.
                              Inicia uma nova rodada com uma palavra aleatória.
                                      """
              self.current_word = random.choice(self.words)
              self.scrambled_word = self.scramble_word(self.current_word)
              self.attempts = 0
              return self.current_word, self.scrambled_word

    def check_answer(self, guess: str) -> bool:
              """
                      Check if the player's guess is correct.
                              Verifica se o palpite do jogador está correto.
                                      """
              self.attempts += 1
              if guess.lower() == self.current_word.lower():
                            self.score += max(5 - self.attempts, 1)
                            return True
                        return False

    def clear_screen(self):
              """Clear the console screen."""
        os.system('clear' if os.name == 'posix' else 'cls')

    def play(self, num_rounds: i
