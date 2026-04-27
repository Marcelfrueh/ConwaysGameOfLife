# Conway's Game of Life

---

## Installation

**Prerequisites:** Python 3.10 or newer.

**1. Clone the repository and navigate into ConwaysGameOfLife**
```bash
git clone https://github.com/Marcelfrueh/ConwaysGameOfLife.git
cd ConwaysGameOfLife
```

**2. Create a virtual environment**

Mac/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install project & dependencies**
```bash
pip install -e ".[dev]"
```


**4. Run the game**
```bash
game-of-life
```

---
## Game Modes

When starting the application, you will be asked how you want to initialize your board. You have three modes available:

**1. Coordinates**\
You set the size of the board and input the exact positions of the living cells.

Format: Row,Column (separated by a space).\
Example: 1,2 2,2 3,2 (Creates a blinker).

**2. Custom Patterns (Load from file)** \
You can place your own patterns as text files into the custom_patterns/ folder.

Use 0 for dead cells and 1 for living cells.

For example, create a file glider.txt with the following content: 

010\
001\
111

Save this file into the directory /src/custom_patterns.
Then, simply type the file name (e.g., glider.txt) in the startup menu.

**3. Random Pattern**

Just enter the desired width and height of the board. The algorithm will then randomly fill the grid with living and dead cells.

---

## Testing
The project includes a test suite that ensures the core rules of Conway's Game of Life (underpopulation, survival, boundaries, etc.) as well as file parsing work correctly.

To run the tests, simply type:

```bash
pytest
```
