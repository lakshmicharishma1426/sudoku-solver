import tkinter as tk
from tkinter import messagebox

# Sudoku Solver Functions
def is_valid(board, row, col, num):

    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve(board):

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:

                for num in range(1, 10):

                    if is_valid(board, row, col, num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True


# GUI Functions
def solve_sudoku():

    board = []

    try:
        for i in range(9):
            row = []

            for j in range(9):

                value = entries[i][j].get()

                if value == "":
                    row.append(0)
                else:
                    row.append(int(value))

            board.append(row)

        if solve(board):

            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(board[i][j]))

        else:
            messagebox.showerror("Error", "No Solution Exists!")

    except ValueError:
        messagebox.showerror("Error", "Enter only numbers 1-9")


def clear_board():

    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("550x650")

entries = []

# Sudoku Grid
for i in range(9):

    row_entries = []

    for j in range(9):

        e = tk.Entry(
            root,
            width=3,
            font=("Arial", 20),
            justify="center"
        )

        e.grid(row=i, column=j, padx=2, pady=2)

        row_entries.append(e)

    entries.append(row_entries)

# Buttons
solve_btn = tk.Button(
    root,
    text="Solve Sudoku",
    font=("Arial", 14),
    command=solve_sudoku
)

solve_btn.grid(row=10, column=1, columnspan=3, pady=20)

clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 14),
    command=clear_board
)

clear_btn.grid(row=10, column=6, columnspan=2, pady=20)

root.mainloop()