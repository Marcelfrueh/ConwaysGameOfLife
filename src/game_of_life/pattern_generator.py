from game_of_life.game import Game
from pathlib import Path
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class PatternGenerator:

    @staticmethod
    def from_text_file() -> Game:
        while True:
            user_input = input("\nPlease provide the file name of your pattern: ").strip()

            base_dir = Path(__file__).parent.parent
            filepath = base_dir / "custom_patterns" / user_input

            try:
                with open(filepath, 'r') as file:
                    lines = [line.strip() for line in file.readlines() if line.strip()]

                game = PatternGenerator._parse_file_content(lines)

                if game is not None:
                    return game

            except FileNotFoundError:
                logger.error(f"Error: '{filepath}' not found!")


    @staticmethod
    def _parse_file_content(lines: list[str]) -> Game | None:
        if not lines:
            logger.error("File is empty!")
            return None

        rows = len(lines)
        cols = len(lines[0])
        alive_cells = set()

        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == '1':
                    alive_cells.add((r, c))

        return Game(initial_cells=alive_cells, rows=rows, cols=cols)

    @staticmethod
    def from_coordinates() -> Game:
        while True:
            try:
                rows = int(input("Amount of rows: "))
                cols = int(input("Amount of columns: "))
                break
            except ValueError:
                logger.error("Error: 'Amount of rows and columns' must be an integer!")

        while True:
            print("\n Please provide the coordinates for your cell configurations.")
            print("Format: Row, Column (separated by space, e.g.: '1,2 2,2 3,2')")
            user_input = input("> ").strip()
            game = PatternGenerator._parse_coordinates(user_input, rows, cols)

            if game is not None:
                return game

    @staticmethod
    def _parse_coordinates(coordinates: str, rows: int, cols: int) -> Game | None:
        alive_cells = set()
        try:
            for coordinate in coordinates.split():
                row, col = map(int, coordinate.split(','))
                if 0 <= row < rows and 0 <= col < cols:
                    alive_cells.add((row, col))
                else:
                    logger.warning(f"Warning: '{coordinates}' is out of bounds!")

            return Game(initial_cells=alive_cells, rows=rows, cols=cols)

        except ValueError:
            logger.error("Wrong format! Please use 'row,col row,col ...'! ")
            return None

    @staticmethod
    def from_random() -> Game:
        while True:
            try:
                rows = int(input("Amount of rows: "))
                cols = int(input("Amount of columns: "))
                break
            except ValueError:
                logger.error("Invalid Input!")

        alive_cells = set()
        for row in range(rows):
            for col in range(cols):
                if random.randint(0, 1) == 1:
                    alive_cells.add((row, col))

        return Game(initial_cells=alive_cells, rows=rows, cols=cols)