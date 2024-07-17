from datetime import datetime




def Level():
    level = int(input("choose alevel between 1,2 and 3: "))       
    while True:
        if level < 1 or level > 3:
            level = int(input("wrong\n choose alevel between 1,2 and 3: "))        
        else:
            break
        
    # if level == 0:  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      برای تست کردنه ردیف 9 ستون 9 اگه 9 بزاری بازی تموم میشه      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #     board = [[5,3,4,6,7,8,9,1,2],            
    #              [6,7,2,1,9,5,3,4,8],  
    #              [1,9,8,3,4,2,5,6,7],  
    #              [8,5,9,7,6,1,4,2,3],  
    #              [4,2,6,8,5,3,7,9,1],  
    #              [7,1,3,9,2,4,8,5,6],  
    #              [9,6,1,5,3,7,2,8,4],  
    #              [2,8,7,4,1,9,6,3,5],
    #              [3,4,5,2,8,6,1,7,0]]
   
    if level == 1:
        board = [[8, 0, 0, 9, 1, 3, 4, 0, 0],            
                 [0, 4, 0, 0, 0, 7, 9, 0, 5],  
                 [0, 9, 0, 2, 0, 0, 6, 0, 0],  
                 [6, 0, 0, 3, 0, 5, 0, 7, 0],  
                 [1, 5, 0, 0, 2, 0, 3, 0, 9],  
                 [3, 7, 0, 8, 9, 0, 0, 5, 0],  
                 [4, 0, 7, 1, 0, 0, 0, 0, 0],  
                 [0, 8, 0, 4, 7, 9, 0, 3, 0],  
                 [9, 0, 0, 0, 3, 0, 0, 6, 4]]  
        
    elif level == 2:
        board = [[2, 0, 0, 0, 4, 0, 0, 5, 7],
             [0, 0, 1, 0, 0, 8, 0, 0, 0],
             [4, 0, 6, 0, 0, 0, 1, 3, 0],
             [0, 3, 5, 0, 0, 6, 0, 0, 0],
             [0, 7, 9, 4, 8, 5, 2, 1, 0],
             [0, 2, 4, 1, 3, 0, 6, 9, 5],
             [0, 0, 2, 7, 1, 0, 0, 0, 0],
             [0, 0, 0, 8, 0, 2, 0, 6, 1],
             [5, 0, 0, 0, 0, 0, 7, 0, 0]]
        
    elif level == 3:
        board  = [[0, 0, 0, 7, 0, 0, 0, 0, 0],
             [8, 0, 2, 0, 6, 9, 0, 0, 0],
             [0, 0, 5, 2, 8, 0, 0, 0, 0],
             [0, 0, 5, 2, 8, 0, 0, 0, 0],
             [0, 1, 3, 8, 0, 0, 5, 0, 9],
             [0, 0, 0, 0, 0, 0, 8, 0, 1],
             [0, 0, 4, 0, 1, 0, 6, 7, 0],
             [3, 7, 0, 9, 2, 0, 0, 0, 0],
             [4, 0, 9, 0, 0, 0, 0, 6, 0],
             [0, 0, 0, 3, 4, 0, 9, 0, 8]]
                          
    return board









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
        print(f"""
        {board[0][0]} {board[0][1]} {board[0][2]} | {board[0][3]}  {board[0][4]}  {board[0][5]} | {board[0][6]}  {board[0][7]}  {board[0][8]} 
        {board[1][0]} {board[1][1]} {board[1][2]} | {board[1][3]}  {board[1][4]}  {board[1][5]} | {board[1][6]}  {board[1][7]}  {board[1][8]} 
        {board[2][0]} {board[2][1]} {board[2][2]} | {board[2][3]}  {board[2][4]}  {board[2][5]} | {board[2][6]}  {board[2][7]}  {board[2][8]} 
        -------------------------
        {board[3][0]} {board[3][1]} {board[3][2]} | {board[3][3]}  {board[3][4]}  {board[3][5]} | {board[3][6]}  {board[3][7]}  {board[3][8]} 
        {board[4][0]} {board[4][1]} {board[4][2]} | {board[4][3]}  {board[4][4]}  {board[4][5]} | {board[4][6]}  {board[4][7]}  {board[4][8]} 
        {board[5][0]} {board[5][1]} {board[5][2]} | {board[5][3]}  {board[5][4]}  {board[5][5]} | {board[5][6]}  {board[5][7]}  {board[5][8]} 
        -------------------------
        {board[6][0]} {board[6][1]} {board[6][2]} | {board[6][3]}  {board[6][4]}  {board[6][5]} | {board[6][6]}  {board[6][7]}  {board[6][8]} 
        {board[7][0]} {board[7][1]} {board[7][2]} | {board[7][3]}  {board[7][4]}  {board[7][5]} | {board[7][6]}  {board[7][7]}  {board[7][8]} 
        {board[8][0]} {board[8][1]} {board[8][2]} | {board[8][3]}  {board[8][4]}  {board[8][5]} | {board[8][6]}  {board[8][7]}  {board[8][8]} 

""")  #final board
        row = (input("Enter row number (1-9): ")) 
        col = (input("Enter column number (1-9): "))  
        num = (input("Enter number to fill (1-9): ")) 
        if row.isdigit() and col.isdigit() and num.isdigit():
            row = int(row)-1
            col = int(col)-1
            num = int(num)
            if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                 pass
            else:
                print("Please enter numbers within the range (1-9).")
                continue
        else:
            print("Please enter numeric values.")
            continue



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
