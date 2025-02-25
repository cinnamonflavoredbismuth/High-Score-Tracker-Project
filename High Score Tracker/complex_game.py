#WORK IN PROGRESS
import random
class Tetris:
    def __init__(self):

        self.squares = [    "🟥", "🟧", "🟨", "🟩", "🟦", "🟪"]
        self.grid_width = 10
        self.grid_height = 20
        self.grid = [["　" for _ in range(self.grid_width)] for _ in range(self.grid_height)]  # 2D grid with full-width spaces
        self.game_over = False

    def display_grid(self):
        print("\nCurrent Grid:")
        for row in self.grid:
            # Join cells with borders and ensure consistent spacing
            formatted_row = "|" + "|".join(row) + "|"
            print(formatted_row)
        print("-" * (self.grid_width * 3 + 1))  # Adjust the divider length for spacing

    def place_shape(self, column):
        if column < 0 or column >= self.grid_width:
            print(f"Invalid column! Please choose a column between 0 and {self.grid_width - 1}.")
            return False

        # Find the lowest empty row in the selected column
        for row in range(self.grid_height - 1, -1, -1):
            if self.grid[row][column] == "　":  # Check for full-width space
                self.grid[row][column] = random.choice(self.squares)  # Place the shape
                return True

        print("Column is full! Choose another column.")
        return False

    def check_game_over(self):
        # Check if the top row is full (game over condition)
        if any(cell != "　" for cell in self.grid[0]):
            self.game_over = True
            print("\nGame Over! The grid is full.")
            return True
        return False

    def play(self):
        print("Welcome to the Suika-like Grid Game!")
        print(f"Place 🟦s in the grid. The grid is {self.grid_width} columns wide and {self.grid_height} rows tall.")
        print("The 🟦 will fall to the bottom of the selected column.")

        while not self.game_over:
            self.display_grid()
            try:
                column = int(input(f"Enter a column (0-{self.grid_width - 1}) to place 🟦: "))
                if self.place_shape(column):
                    if self.check_game_over():
                        break
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 9.")

        self.display_grid()
        print("Thanks for playing!")

#if __name__ == "__main__":
#    game = Tetris()
#    game.play()
