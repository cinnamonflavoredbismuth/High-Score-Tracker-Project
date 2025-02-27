import random

class Tetris:
    def __init__(self):
        # Define the shapes as 2D matrices
        self.shapes = {
            "I": [[1, 1, 1, 1]],
            "O": [[1, 1],
                  [1, 1]],
            "S": [[0, 1, 1],
                  [1, 1, 0]],
            "Z": [[1, 1, 0],
                  [0, 1, 1]],
            "J": [[1, 0, 0],
                  [1, 1, 1]],
            "L": [[0, 0, 1],
                  [1, 1, 1]],
            "T": [[0, 1, 0],
                  [1, 1, 1]],
        }
        # Define colors for the shapes
        self.colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪"]
        # Grid dimensions
        self.grid_width = 10
        self.grid_height = 18
        # Initialize the grid with empty spaces
        self.grid = [["　" for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.game_over = False

    def display_grid(self):
        """Display the current state of the grid."""
        if self.game_over:
            print("\nFinal Grid:")
        elif not self.game_over:
            print("\nCurrent Grid:")
        for row in self.grid:
            formatted_row = "|" + "|".join(row) + "|"
            print(formatted_row)
        print("-" * (self.grid_width * 3 + 1))  # Adjust the divider length for spacing

    def rotate_shape(self, shape):
        """Rotate the shape 90 degrees clockwise."""
        return [list(row) for row in zip(*shape[::-1])]

    def can_place_shape(self, row, column, shape):
        """Check if the shape can be placed at the specified position."""
        for r in range(len(shape)):
            for c in range(len(shape[r])):
                if shape[r][c] and (row + r >= self.grid_height or column + c < 0 or column + c >= self.grid_width or self.grid[row + r][column + c] != "　"):
                    return False
        return True

    def put_shape(self, row, column, shape):
        """Place the shape in the grid."""
        color = random.choice(self.colors)
        for r in range(len(shape)):
            for c in range(len(shape[r])):
                if shape[r][c]:
                    self.grid[row + r][column + c] = color

    def place_shape(self, column, shape):
        """Place a shape at the specified column."""
        shape_height = len(shape)
        shape_width = len(shape[0])

        # Check if the shape fits in the grid
        if column < 0 or column + shape_width > self.grid_width:
            print(f"Shape doesn't fit in column {column}!")
            return False

        # Find the lowest row where the shape can be placed
        for row in range(self.grid_height - shape_height, -1, -1):
            if self.can_place_shape(row, column, shape):
                self.put_shape(row, column, shape)
                return True

        print("Not enough space to place the shape!")
        return False

    def clear_completed_rows(self):
        """Clear completed rows and shift rows down."""
        completed_rows = []
        for row in range(self.grid_height):
            if all(cell != "　" for cell in self.grid[row]):
                completed_rows.append(row)

        for row in completed_rows:
            del self.grid[row]
            self.grid.insert(0, ["　" for _ in range(self.grid_width)])

        return len(completed_rows)

    def check_game_over(self):
        """Check if the game is over by seeing if the top row is filled."""
        if any(cell != "　" for cell in self.grid[0]):
            self.game_over = True
            print("\nGame Over! The top row is filled.")
            return True
        return False
        
    def rotate_again_ask(self, rotateAgain, shape):
        if rotateAgain == "y":
            again, shape = self.rotate_again_ask(input("Roate again (y/n)?").strip().lower(), shape)
            if again == "y":
                return "y", shape

            elif again == "n":
                return "n", shape
            

        elif rotateAgain == "n":
            return "n", shape

        else:
            return self.rotatate_again_ask(input("invalid input, roate again (y/n)?").strip().lower(), shape)

    def rotate_ask(self, rotate, shape):
        # Allow the player to rotate the shape
        if rotate == "y":
            shape = self.rotate_shape(shape)
            again, shape = self.rotate_again_ask(input("Roate again (y/n)?").strip().lower(), shape)
            if again == "y":
                pass

            elif again == "n":
                return shape
        
        elif rotate == "n":
            return shape
        else:
            self.rotate_ask(input("Invalid input, rotate shape 90 degrees? (y/n): ").strip().lower(), shape)

    def play(self):
        """Main game loop."""
        print("Welcome to Tetris!")
        print(f"The grid is {self.grid_width} columns wide and {self.grid_height} rows tall.")

        while not self.game_over:
            self.display_grid()

            # Randomly select a shape
            shape_name = random.choice(list(self.shapes.keys()))
            shape = self.shapes[shape_name]
            print(f"Current shape: {shape_name}")

            shape = self.rotate_ask(input("Rotate shape 90 degrees? (y/n): ").strip().lower(), shape)

            # Get the column from the player
            try:
                column = int(input(f"Enter a column (0-{self.grid_width - len(shape[0])}) to place the shape: "))
                if self.place_shape(column, shape):
                    rows_cleared = self.clear_completed_rows()
                    if rows_cleared:
                        print(f"Cleared {rows_cleared} row(s)!")
                    if self.check_game_over():
                        print("Thanks for playing!")
                    else:
                        pass
            except ValueError:
                print("Invalid input! Please enter a number.")

        self.display_grid()


# Start the game
if __name__ == "__main__":
    game = Tetris()
    game.play()