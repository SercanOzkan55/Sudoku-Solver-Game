import tkinter as tk

def create_entries():
    entries = []
    for i in range(9):
        row_entries = []
        for j in range(9):
            entry = tk.Entry(frame, font=("Arial", 12), justify='center', width=4, bg="red")
            entry.grid(row=i, column=j, padx=5, pady=5, ipady=8)
            row_entries.append(entry)
        entries.append(row_entries)
    return entries

def get_user_input(entries):
    user_input = []
    for row_entries in entries:
        row_values = []
        for entry in row_entries:
            value = entry.get()
            row_values.append(value)
        user_input.append(row_values)
    return user_input

def is_valid(board, row, col, num):
    # Row and column check
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
        if board[i][col] == num and i != row:
            return False

    # 3x3 region check
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False

    return True

def find_empty_position(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == "":
                return i, j
    return None

def solve_sudoku(board):
    empty = find_empty_position(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        num = str(num)
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = ""

    return False

def get_3x3_region(board, start_row, start_col):
    return [board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]

def hint():
    user_input = get_user_input(entries)

    # Row and column check
    for i in range(9):
        for j in range(9):
            num = user_input[i][j]
            if num and not is_valid(user_input, i, j, num):
                print("Sudoku cannot be solved. Duplicate number found in the same row, column, or 3x3 region.")
                return

    # 3x3 region duplicate check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            region_values = set(get_3x3_region(user_input, i, j))
            if "" in region_values:
                region_values.remove("")
            if len(region_values) != len(set(region_values)):
                print("Sudoku cannot be solved. Duplicate number found in the same 3x3 region.")
                return

    print("No issues found. Ready for solving.")

def submit():
    user_input = get_user_input(entries)
    sudoku_board = [[str(user_input[i][j]) if user_input[i][j] else "" for j in range(9)] for i in range(9)]
    if solve_sudoku(sudoku_board):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, sudoku_board[i][j])

def clear():
    for row_entries in entries:
        for entry in row_entries:
            entry.delete(0, "end")

form = tk.Tk()
form.title("Sudoku Solver")
form.geometry("700x600")
form.resizable(False, False)
etiket = tk.Label(form, text="Welcome The League Of Sudoku ", bg="white", fg="#1c0f45", font="Monaco 20").place(relx=0.18, rely=0.001)
form.config(bg="white")
frame = tk.Frame(form, bg="black")
frame.pack(padx=35, pady=50)

entries = create_entries()

yatay1 = tk.Label(form, bg="yellow", fg="yellow", text="t")
yatay1.place(relx=0.18, rely=0.32, width=447, height=4)

yatay2 = tk.Label(form, bg="yellow", fg="yellow", text="t")
yatay2.place(relx=0.18, rely=0.56, width=447, height=4)

dikey1 = tk.Label(form, bg="yellow", fg="yellow", text="t")
dikey1.place(relx=0.39, rely=0.083, width=4, height=430)

dikey2 = tk.Label(form, bg="yellow", fg="yellow", text="t")
dikey2.place(relx=0.604, rely=0.083, width=4, height=430)

submit_button1 = tk.Button(form, text="Submit", command=submit, bg="gray", activebackground="blue")
submit_button1.place(height=20, width=50, x=220, y=520)

hint_button2 = tk.Button(form, text="Hint", command=hint, bg="gray", activebackground="blue")
hint_button2.place(height=20, width=50, x=320, y=520)

clear_button3 = tk.Button(form, text="Clear", command=clear, bg="gray", activebackground="blue")
clear_button3.place(height=20, width=50, x=420, y=520)

form.mainloop()
