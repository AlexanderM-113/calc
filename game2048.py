import random

def p():
    input("Press EXE...")

def print_board(board):
    print("\n")
    for row in board:
        print(str(row[0]).rjust(4) + str(row[1]).rjust(4) + 
              str(row[2]).rjust(4) + str(row[3]).rjust(4))
    print()

def add_tile(board):
    empty=[(i,j) for i in range(4) for j in range(4)
           if board[i][j]==0]
    if empty:
        i,j=random.choice(empty)
        board[i][j]=2 if random.random()<0.9 else 4

def move_left(board):
    for row in board:
        non_zero=[x for x in row if x!=0]
        merged=[]
        skip=False
        for i,val in enumerate(non_zero):
            if skip:
                skip=False
                continue
            if i+1<len(non_zero) and val==non_zero[i+1]:
                merged.append(val*2)
                skip=True
            else:
                merged.append(val)
        row[:]=merged+[0]*(4-len(merged))

def rotate_cw(board):
    for i in range(4):
        for j in range(i,4):
            board[i][j],board[j][i]=board[j][i],board[i][j]
    for row in board:
        row.reverse()

def game():
    print("\n" + "="*32)
    print("2048 GAME")
    print("="*32 + "\n")
    
    board=[[0]*4 for _ in range(4)]
    add_tile(board)
    add_tile(board)
    score=0
    
    while True:
        print_board(board)
        print("Score: " + str(score))
        print("1=Left 2=Right 3=Up 4=Down 5=Quit\n")
        
        ch=input("Move: ")
        
        if ch=="5":
            break
        
        old=[[board[i][j] for j in range(4)] 
             for i in range(4)]
        
        if ch=="1":
            move_left(board)
        elif ch=="2":
            for _ in range(3):
                rotate_cw(board)
            move_left(board)
            rotate_cw(board)
        elif ch=="3":
            rotate_cw(board)
            move_left(board)
            for _ in range(3):
                rotate_cw(board)
        elif ch=="4":
            for _ in range(3):
                rotate_cw(board)
            move_left(board)
            rotate_cw(board)
        else:
            continue
        
        if board!=old:
            add_tile(board)
            for row in board:
                for val in row:
                    if val==2048:
                        print("\nYOU WIN!\n")
                        p()
                        return
    
    print("\nGoodbye!\n")
    p()

while True:
    print("\n" + "="*32)
    print("2048 GAME")
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
