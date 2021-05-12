
def init_board():
    global board
    board=[0]*9


def is_over():
  return (possible_moves()==[] or end_game())

# Compute the score
def scoring():
    return -100 if end_game() else 0

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


#################################################################################################
## Funcion recursiva: (funcion que se llama a si misma) ########################################

def Negamax(board,depth,alpha=-inf, beta=+inf):

    # caso base: (caso que marca el fin de la recursividad)
    # En este caso es que hay un ganador o el tablero esta lleno
 
    if is_over(): # si la partida ha terminado
        score = scoring() # valoro el resultado final (derrota o empate)

        if score == 0:
            return (score,None) 
        else: 
            return  ((score - 0.01*depth*abs(score)/score),None) # valoro la progundida para busjar victorias
                                                                 # rapidas o derrotas lentas. 