import random

def p():
    input("Press EXE...")

def print_board(board):
    print("\n")
    for i in range(3):
        row=""
        for j in range(3):
            cell=board[i][j]
            if cell==0:
                row+=str(i*3+j+1)
            else:
                row+="X" if cell==1 else "O"
            row+=" | "
        print(row)
        if i<2:
            print("---------")
    print()

def check_win(board,player):
    win_cond=[[0,1,2],[3,4,5],[6,7,8],
              [0,3,6],[1,4,7],[2,5,8],
              [0,4,8],[2,4,6]]
    for cond in win_cond:
        if all(board[c//3][c%3]==player for c in cond):
            return True
    return False

def game():
    print("\n" + "="*32)
    print("TIC-TAC-TOE")
    print("="*32)
    
    board=[[0]*3 for _ in range(3)]
    moves=0
    
    while moves<9:
        print_board(board)
        
        while True:
            try:
                pos=int(input("Your move (1-9): "))-1
                if 0<=pos<9 and board[pos//3][pos%3]==0:
                    board[pos//3][pos%3]=1
                    break
                print("Invalid")
            except:
                print("Invalid")
        
        if check_win(board,1):
            print_board(board)
            print("YOU WIN!\n")
            p()
            return
        
        moves+=1
        if moves==9:
            break
        
        empty=[i for i in range(9) 
                if board[i//3][i%3]==0]
        if empty:
            pos=random.choice(empty)
            board[pos//3][pos%3]=2
            moves+=1
        
        if check_win(board,2):
            print_board(board)
            print("CPU WINS!\n")
            p()
            return
    
    print_board(board)
    print("TIE!\n")
    p()

while True:
    print("\n" + "="*32)
    print("TIC-TAC-TOE")
    print("="*32 + "\n")
    print("1 = Play")
    print("2 = Exit\n")
    ch=input("Choose: ")
    
    if ch=="1":
        game()
    elif ch=="2":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice.")
