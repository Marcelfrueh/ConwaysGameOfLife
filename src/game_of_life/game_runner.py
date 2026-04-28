import time
import os
from pynput import keyboard
from game_of_life.game import Game
from game_of_life.pattern_generator import PatternGenerator
from game_of_life.renderer import ConsoleRenderer
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class GameRunner:
    def __init__(self):
        self._renderer = ConsoleRenderer()
        self._game = None
        self._is_paused = False
        self._tick_rate = 0.5

    @staticmethod
    def _setup_game() -> Game | None:
        while True:
            print("\nHow would you like to configure your board?")
            print("[1] Provide coordinates of pattern")
            print("[2] Use pattern from file")
            print("[3] Use random pattern")
            choice = input("Choose 1, 2 or 3: ").strip()

            if choice == '1':
                game = PatternGenerator.from_coordinates()
            elif choice == '2':
                game = PatternGenerator.from_text_file()
            elif choice == '3':
                game = PatternGenerator.from_random()
            else:
                logger.error("Invalid input! Use 1, 2 or 3.")
                continue

            if game is not None:
                return game

    def _on_press(self, key):
        try:
            if key.char == 'q':
                os._exit(0)
            elif key.char == 'p':
                self._is_paused = not self._is_paused
        except AttributeError:
            pass

    def run(self):
        self._game = self._setup_game()
        self._is_paused = False
        listener = keyboard.Listener(on_press=self._on_press)
        listener.start()

        while True:
            self._renderer.render(self._game)
            status = "PAUSED" if self._is_paused else "RUNNING"
            print(f"\nStatus: {status} | [P] - Pause, [Q] - Quit")

            if not self._is_paused:
                self._game.next_generation()

            time.sleep(self._tick_rate)


def main():
    app = GameRunner()
    app.run()

if __name__ == "__main__":
    main()
