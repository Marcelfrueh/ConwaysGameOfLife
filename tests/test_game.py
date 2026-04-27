from game_of_life.game import Game
from game_of_life.pattern_generator import PatternGenerator

def test_underpopulation():
    initial_cells = {(1,1)}
    game = Game(initial_cells, rows = 5, cols = 5)

    game.next_generation()

    assert len(game.cells) == 0

def test_block_pattern():
    initial_cells = {(1,1), (1,2), (2,1), (2,2)}
    game = Game(initial_cells, rows = 5, cols = 5)

    game.next_generation()

    assert game.cells == {(1,1), (1,2), (2,1), (2,2)}

def test_blinker():
    initial_cells = {(2,1), (2,2), (2,3)}
    game = Game(initial_cells, rows = 5, cols = 5)

    game.next_generation()
    expected_cells = {(1,2), (2,2), (3,2)}
    assert game.cells == expected_cells
    assert game.generation == 1

    game.next_generation()
    assert game.cells == initial_cells
    assert game.generation == 2

def test_boundaries():
    initial_cells = {(0,0), (0,1), (1,0)}
    game = Game(initial_cells, rows = 3, cols = 3)
    game.next_generation()

    # check if a cell has negative coordinates
    for row, col in game.cells:
        assert 0 <= row < 3
        assert 0 <= col < 3

def test_file_loader_parsing():
    dummy_lines = [
        "010",
        "001",
        "100"
    ]

    game = PatternGenerator._parse_file_content(dummy_lines)
    assert game.rows == 3
    assert game.cols == 3
    assert (0,1) in game.cells
    assert (1,2) in game.cells
    assert (2,0) in game.cells
    assert (0,0) not in game.cells
    assert (2,2) not in game.cells


