import os
from game_of_life.game import Game

class ConsoleRenderer:
    def __init__(self, alive_char: str = ' o ', dead_char: str = ' - '):
        self.alive_char = alive_char
        self.dead_char = dead_char

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self, game: Game):
        self.clear_console()
        print(f"=== Generation: {game.generation} ===")

        for row in range(game.rows):
            line = ""
            for col in range(game.cols):
                if (row, col) in game.cells:
                    line += self.alive_char
                else:
                    line += self.dead_char
            print(line)