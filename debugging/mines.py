#!/usr/bin/python3

import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height

        # Random mine positions
        self.mines = set(random.sample(range(width * height), mines))

        # Track revealed cells
        self.revealed = [
            [False for _ in range(width)]
            for _ in range(height)
        ]

    def print_board(self, reveal=False):
        clear_screen()

        print('  ' + ' '.join(str(i) for i in range(self.width)))

        for y in range(self.height):
            print(y, end=' ')

            for x in range(self.width):

                if reveal or self.revealed[y][x]:

                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')

                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')

                else:
                    print('.', end=' ')

            print()

    def count_mines_nearby(self, x, y):
        count = 0

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                # Skip current cell
                if dx == 0 and dy == 0:
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1

        return count

    def reveal(self, x, y):

        # Prevent invalid coordinates
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True

        # Prevent revealing already revealed cells
        if self.revealed[y][x]:
            return True

        # Hit a mine
        if (y * self.width + x) in self.mines:
            return False

        self.revealed[y][x] = True

        # Auto-reveal nearby cells if no mines nearby
        if self.count_mines_nearby(x, y) == 0:

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:

                    if dx == 0 and dy == 0:
                        continue

                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if not self.revealed[ny][nx]:
                            self.reveal(nx, ny)

        return True

    def has_won(self):
        """
        Player wins when all non-mine cells are revealed.
        """

        for y in range(self.height):
            for x in range(self.width):

                cell_index = y * self.width + x

                # If cell is NOT a mine and NOT revealed
                if cell_index not in self.mines and not self.revealed[y][x]:
                    return False

        return True

    def play(self):

        while True:

            self.print_board()

            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))

                # Reveal selected cell
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Check win condition
                if self.has_won():
                    self.print_board(reveal=True)
                    print("Congratulations! You won!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    game = Minesweeper()
    game.play() 
