
def init_board():
    global board
    board=[0]*9

def possible_moves():
    global board
    return [a+1 for a,b in enumerate(board) if b==0] 

def jugar(pos,XO):
    print(XO)
    board[pos-1]= 1 if XO =='x'else 2
    show_board()
    return end_game()

def show_board():
    print(board)


def end_game():
    possible_combinations=[[1,2,3],[4,5,6],[7,8,9],
                           [1,4,7],[2,5,8],[3,6,9],
                           [1,5,9],[3,5,7]]
    # winer
    for p in [1,2]:
        for c,combination in enumerate(possible_combinations):
           three=all([(board[i-1]==p) for i in combination])
           if three:
              print(c+1,p)
              return (c+1,p)
    
    out=(0,0) # draw
    
    for c in board:
        if c==0:
            out=(-1,0) # -1 =  playing
            break
        
    return  out     