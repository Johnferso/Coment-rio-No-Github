"""
Embaralhador de Palavras (Word Scrambler)
A fun word guessing game where players unscramble letters to form words.

Autor / Author: Claude
Data / Date: 2026-04-22
Linguagem / Language: Python 3
"""

import random
import os
from typing import List, Tuple


class WordScrambler:
    """
    Um jogo simples de desembaralhar palavras.
    A simple word unscrambling game.
    """

    def __init__(self):
        """Initialize the game with a word list."""
        # Portuguese and English words for the game
        self.words: List[str] = [
            "python", "computador", "programação", "algoritmo",
            "internet", "desenvolvimento", "software", "hardware",
            "database", "servidor", "cliente", "rede",
            "código", "função", "variável", "constante"
        ]
        self.score: int = 0
        self.total_rounds: int = 0

    def scramble_word(self, word: str) -> str:
        """
        Embaralha uma palavra (Scrambles a word).

        Args:
            word: The word to scramble

        Returns:
            The scrambled version of the word
        """
        word_list = list(word.lower())
        random.shuffle(word_list)
        return ''.join(word_list)

    def play_round(self) -> bool:
        """
        Executa uma rodada do jogo (Plays one round of the game).

        Returns:
            True if player guessed correctly, False otherwise
        """
        # Select a random word
        correct_word = random.choice(self.words)
        scrambled = self.scramble_word(correct_word)

        # Make sure the scrambled word is different from the original
        while scrambled == correct_word:
            scrambled = self.scramble_word(correct_word)

        print(f"\n{'='*40}")
        print(f"Palavra Embaralhada: {scrambled.upper()}")
        print(f"Dica / Hint: A palavra tem {len(correct_word)} letras")
        print(f"{'='*40}")

        # Get player's guess
        guess = input("Qual é a palavra? / What is the word? ").strip().lower()

        # Check the answer
        if guess == correct_word:
            print(f"✓ Correto! / Correct! A palavra era: {correct_word.upper()}")
            self.score += 1
            return True
        else:
            print(f"✗ Errado! / Wrong! A palavra era: {correct_word.upper()}")
            return False

    def clear_screen(self) -> None:
        """Limpa a tela do console (Clears the console screen)."""
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_menu(self) -> None:
        """Exibe o menu principal (Displays the main menu)."""
        self.clear_screen()
        print("╔════════════════════════════════════════╗")
        print("║   EMBARALHADOR DE PALAVRAS             ║")
        print("║   WORD SCRAMBLER GAME                  ║")
        print("╚════════════════════════════════════════╝")
        print(f"\nPontuação / Score: {self.score}/{self.total_rounds}")
        print("\n1. Jogar / Play")
        print("2. Ver Palavras / Show Words")
        print("3. Sair / Quit")

    def show_words(self) -> None:
        """Exibe todas as palavras do jogo (Shows all words in the game)."""
        print("\n📚 Palavras do Jogo / Game Words:")
        print("-" * 40)
        for i, word in enumerate(self.words, 1):
            print(f"{i}. {word}")
        print("-" * 40)
        input("Pressione Enter / Press Enter para continuar...")

    def run(self) -> None:
        """Executa o loop principal do jogo (Runs the main game loop)."""
        while True:
            self.display_menu()
            choice = input("\nEscolha uma opção / Choose an option: ").strip()

            if choice == '1':
                self.total_rounds += 1
                self.play_round()

            elif choice == '2':
                self.show_words()

            elif choice == '3':
                self.display_stats()
                print("\nObrigado por jogar! / Thanks for playing!")
                break

            else:
                print("Opção inválida / Invalid option!")
                input("Pressione Enter / Press Enter...")

    def display_stats(self) -> None:
        """Exibe as estatísticas finais (Displays final statistics)."""
        self.clear_screen()
        print("\n╔════════════════════════════════════════╗")
        print("║          ESTATÍSTICAS / STATS          ║")
        print("╚════════════════════════════════════════╝")

        if self.total_rounds > 0:
            percentage = (self.score / self.total_rounds) * 100
            print(f"\nAcertos / Correct: {self.score}/{self.total_rounds}")
            print(f"Percentual / Percentage: {percentage:.1f}%")
        else:
            print("\nNenhuma rodada jogada / No rounds played")


def main():
    """Função principal (Main function)."""
    game = WordScrambler()
    game.run()


if __name__ == "__main__":
    main()
