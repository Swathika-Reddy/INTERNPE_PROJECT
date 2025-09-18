class ConnectFour:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        self.current_player = '\U0001F535'  # Blue Circle

    def print_board(self):
        print("\n".join(["|".join(row) for row in self.board]))
        print('-' * (2 * self.columns - 1))
        print(" ".join(map(str, range(self.columns))))

    def is_valid_move(self, column):
        return 0 <= column < self.columns and self.board[0][column] == ' '

    def make_move(self, column):
        for row in reversed(range(self.rows)):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return row, column

    def check_winner(self, row, column):
        def count_consecutive(delta_row, delta_col):
            r, c = row, column
            count = 0
            while 0 <= r < self.rows and 0 <= c < self.columns and self.board[r][c] == self.current_player:
                count += 1
                r += delta_row
                c += delta_col
            return count

        directions = [
            (0, 1),  # Horizontal right
            (1, 0),  # Vertical down
            (1, 1),  # Diagonal down-right
            (1, -1)  # Diagonal down-left
        ]

        for delta_row, delta_col in directions:
            total = (count_consecutive(delta_row, delta_col) +
                     count_consecutive(-delta_row, -delta_col) - 1)
            if total >= 4:
                return True
        return False

    def switch_player(self):
        self.current_player = '\U0001F534' if self.current_player == '\U0001F535' else '\U0001F535'  # Red Circle if Blue Circle

    def is_draw(self):
        return all(self.board[0][col] != ' ' for col in range(self.columns))

    def play(self):
        print("Welcome to Connect Four!")
        while True:
            self.print_board()
            try:
                column = int(input(f"Player {self.current_player}, choose a column (0-{self.columns - 1}): "))

                if not self.is_valid_move(column):
                    print("Invalid move. Try again.")
                    continue

                row, col = self.make_move(column)

                if self.check_winner(row, col):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break

                if self.is_draw():
                    self.print_board()
                    print("It's a draw!")
                    break

                self.switch_player()
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    game = ConnectFour()
    game.play()
