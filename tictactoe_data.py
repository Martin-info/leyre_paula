import random

def init_board():
    global board, nplayer,nopponent,inf
    board=[0]*9
    nplayer = 1
    nopponent = 2
    inf = float('infinity')


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

def desordenar_casillas(l2):
    l1=[]
    l1.extend(l2)
    random.shuffle(l1)
    return l1

# Make a move
def make_move(move):
    board[int(move) - 1] = nplayer


# Undo a move
def undo_move(move):
    board[int(move) - 1] = 0

def switch_player():
   global nplayer, nopponent
   aux=nplayer
   nplayer=nopponent
   nopponent=aux

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

    # caso general: 
    # Probamos jugadas como jugador y como oponente hasta que encontremos la jugada optima 

    # En la primer jugada,elegimos la casilla de forma aleatoria para que el juego sea mas variado. 
    # Si no el ordenador empezaria siempre de la misma forma.

    if len(possible_moves())==9:
        return (None,random.randint(1,9))


    bestValue = -inf

    for move in desordenar_casillas(possible_moves()):  # para todas las casillas disponibles    
        make_move(move)                                 # juego en esa casilla (jugada de prueba)
        switch_player()                                 # cambio de jugdor a oponente
        value = - (Negamax(board, depth+1,-beta, -alpha)[0])  # juego como el oponente
        switch_player()                                       # cambio de oponente a jugador
        undo_move(move)                                       # deshago la jugada de pueba

        if value > bestValue:     # si es la mejor jugada
            bestValue=value       # guardo el valor de la jugada
            bestMove=move         # guardo la casilla de la jugada.
        
        # alpha = limite inferior forzado por el oponente al jugador (inicialmente -inf)
        # beta  =  limite superior forzado por el jugador al oponente (inicialmente inf)
        
        if  alpha < value :      
                alpha = value      # actualizo el lim inf consegudo por el oponente


        if (alpha >= beta):        # ignoro los casos o jugadas en que los lim inf y sup son >=
            break                  # ya que son casos redundantes

    return (bestValue,bestMove)    # devuelvo el valor y la casilla de la juga
