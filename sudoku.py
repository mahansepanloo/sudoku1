from datetime import datetime
def is_valid_move(board, row, col, num):  #اعتبار سنجی جدول 
    
    if num in board[row]:  #چک کردن سطر ها
        # print(f"row!!!{board[row].index(num)+1}")
        return False  

    if num in [board[i][col] for i in range(9)]:   #چک کردن ستون ها
        return False  

    
    block_col =  3 * (col // 3)  #چک کردن مربع  3*3
    block_row = 3 * (row // 3)

    if num in [  board[r][c]  for r in range(block_row, block_row + 3)  for c in range(block_col, block_col + 3) ]:  
        return False  
    return True  



def is_winner(board):  #چک کردن پیروزی
    for row in board:  
        if 0 in row:  
            return False  
    return True 


def iterbord(board):  
    for row in board:  
        yield (row)

def check_conflict(board, row, col, num):  
    conflicts = {
        "row":[],
        "col":[],
        "Square":[]
    }

    for i in range(9):  
        if board[row][i] == num:  
            conflicts["row"].append((row+1, i+1))  

    for i in range(9):  
        if board[i][col] == num:  
            conflicts["col"].append((i+1, col+1))  

    
    square_row = ((row) // 3) * 3  
    square_col = ((col) // 3) * 3  

    for i in range(3):  
        for j in range(3):  
            if board[square_row + i][square_col + j] == num:  
                conflicts["Square"].append((square_row + i+1, square_col + j+1))  

    return conflicts  

def play_sudoku():   # بازی 
    t1 = datetime.now()
    board=Level()
    print("\nEmpty Sudoku Board:")  

    iterbord(board)  
    
    while not is_winner(board):  


        if board[row][col] != 0:
            print(f'you cant change row {row + 1} and col {col + 1}')
            continue


        if is_valid_move(board, row, col, num):  
            board[row][col] = num  
            print("Updated Sudoku Board:") 

        else:
            conflicts = check_conflict(board, row, col, num)  
            if conflicts:  
                print(f"Conflict found for number {num} at row {row+1} and column {col+1} whit : {conflicts}")





        iterbord(board)  
    print("amazing! You have won the game!")  
    t2 = datetime.now()
    T =t2 - t1
    print(f'Game duration:{T}')
play_sudoku()