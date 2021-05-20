import pygame
from pygame.locals import *
import random
import time
import sys 


nplayer = 1
nopponent = 2
board = [0] * 1
inf = float('infinity')


# Check if the game is over
def is_over():
    return (possible_moves() == []) or loss_condition()


# Define possible moves
def possible_moves():
    return [a + 1 for a, b in enumerate(board) if b == 0] # lista de casillas vacias.


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


def desordenar_casillas(l2):
    l1=[]
    l1.extend(l2)
    random.shuffle(l1)
    return l1


def show():
    print()
    print('\n'+'\n'.join([' '.join([['.', 'X', 'O'][board[4*j+ i]] for i in range(4)]) for j in range(4)]))
    print()
    

# Does the opponent have three in a line?
def loss_condition():
    possible_combinations = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16],
    [1,5,9,13], [2,6,10,14], [3,7,11,15], [4,8,12,16], [1,6,11,16], [4,7,10,13]]

    return any([all([(board[i-1] == nopponent)
               for i in combination]) for combination in possible_combinations]) 


# Compute the score
def scoring():
    return -100 if loss_condition() else 0


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


############################################################################################
############################################################################################

def init_board():
    global board, nplayer,nopponent,inf
    board=[0]*9
    nplayer = 1
    nopponent = 2
    inf = float('infinity')


def game_reset():
    global XO   
    init_board()   
    XO='x'
    draw_board()
    pygame.display.set_caption("My Tic Tac Toe ( X )") 
    print("Game RESET")


def check_events():
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit() 
            print("Adios")
            sys.exit() 
        elif event.type==MOUSEBUTTONDOWN:
            print("has pulsado") 
            return user_click() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_reset()
                return -2
    return -1       


def user_click(): 
    global game_over,board, XO
    x, y = pygame.mouse.get_pos() 
     
    if(x<width / 4): 
        col = 1
    elif (x<width / 4 * 2): 
        col = 2
    elif (x<width / 4 * 3): 
        col = 3
    elif(x<width): 
        col = 4
    else: 
        col = None

    if(y<height / 4): 
        row = 1    
    elif (y<height / 4 * 2): 
        row = 2
    elif (y<height / 4 * 3): 
        row = 3
    elif(y<height): 
        row = 4
    else: 
        row = None
        
    p=col+4*(row-1) 
    
    if p in possible_moves() and not is_over():
        return p
    else:
        return -1


def drawXO(): 
    global board,gameDisplay
    
    for pos,val in enumerate(board):
        if val == 0:
            continue
        
        row=(pos)//4 #  n fila
        col=(pos)%4  # n col
    
        posx = width // 4 * (row) + 30 #  
        posy = height // 4 * (col) + 30
    
        if(val==1): 
            gameDisplay.blit(x_img, (posy, posx))
            pygame.display.set_caption("My Tic Tac Toe ( O )")  
        else: 
            gameDisplay.blit(o_img, (posy, posx))
            pygame.display.set_caption("My Tic Tac Toe ( X )") 
            XO = 'x' 

    pygame.display.update()




def cross_lines(line):
      
    # horizontal lines
    if line==1 or line==2 or line==3:     
        pygame.draw.line(gameDisplay, (250, 0, 0), 
                    (0+10, (line)*height / 3 -height / 6), 
                    (width -10, (line)*height / 3 - height / 6 ), 14)  
    
    # vertical lines
    elif line==4 or line==5 or line==6:          
        pygame.draw.line (gameDisplay, (250, 0, 0),
                     ((line-3)* width / 3 - width / 6, 0+10),
                     ((line-3)* width / 3 - width / 6, height -10), 14) 
    
    # diagonal line left to right
    elif line==7:                             
        pygame.draw.line (gameDisplay, (250, 70, 70), (50, 50), (350, 350), 14) 
    
    # diagonal line right to left
    elif line==8:                             
        pygame.draw.line (gameDisplay, (250, 70, 70), (350, 50), (50, 350), 14)
    
    pygame.display.update()



def end_game():
    possible_combinations=[[1,2,3],[4,5,6],[7,8,9],
                           [1,4,7],[2,5,8],[3,6,9],
                           [1,5,9],[3,5,7]]
    for p in [1,2]:
        for c,combination in enumerate(possible_combinations):
           three=all([(board[i-1]==p) for i in combination])
           if three:
              return cross_lines(c+1)

###################################################################################
# Creamos la ventana ##############################################################

def draw_board():    
    pygame.display.set_caption("My Tic Tac Toe ( X )") 
    XO='x'
        
    
    white=(255,255,255) # color RGB (red,green,blue)
    line_color=(0,0,155)
    gameDisplay.fill(white) 
        
    # drawing vertical lines 
    pygame.draw.line(gameDisplay, line_color, (width / 4, 0), (width / 4, height), 7) 
    pygame.draw.line(gameDisplay, line_color, (width / 4 * 2, 0), (width / 4 * 2, height), 7) 
    pygame.draw.line(gameDisplay, line_color, (width / 4 * 3, 0), (width / 4 * 3, height), 7) 
        
    
    # drawing horizontal lines 
    pygame.draw.line(gameDisplay, line_color, (0, height / 4), (width, height / 4), 7) 
    pygame.draw.line(gameDisplay, line_color, (0, height / 4 * 2), (width, height / 4 * 2), 7)
    pygame.draw.line(gameDisplay, line_color, (0, height / 4 * 3), (width, height / 4 * 3), 7)
    
    pygame.display.update()



width=532
height=532
        
pygame.init()
    
# setting fps manually 
fps = 10
    
# this is used to track time 
CLOCK = pygame.time.Clock() 
    
# loading the images as python object 
x_img = pygame.image.load("X_modified.png") 
o_img = pygame.image.load("o_modified.png") 
    
# resizing images 
x_img = pygame.transform.scale(x_img, (80, 80)) 
o_img = pygame.transform.scale(o_img, (80, 80)) 
    
gameDisplay= pygame.display.set_mode((width,height))

draw_board()


###########################################################################################
## Partida ################################################################################



while True:
    turn=1 #random.randint(0,1)             # turno aleatorio  
    while not is_over():                 # mientras no termine el juego.
    
        if turn==1:                      # Si turno =1 juega el usuario
            move=-1  
            while move<1:                     # mostramos el tablero 
                move=check_events()            # el usuario elige jugada

#            turn=2                       # cambio de turno
        else:                            # sino, juega el ordenador
            score,move=Negamax(board,0)  # ordenador elige jugada
            turn=1                       # cambiamos de turno

        make_move(move)                  # hacemos la jugada elegida 
        drawXO()
        switch_player()                  # intercambiamos jugador <-> oponente


##########################################################################################
## La partida ha terminado ###############################################################

    show()                               # mostramos el tablero final 

    if loss_condition():                 # vemos si ha ganado alguien
        if turn==1:                      # turn=1 gana ordenador
            pygame.display.set_caption("My Tic Tac Toe (Computer WINS)")       
        else:                            # sino gana usuario
            pygame.display.set_caption("My Tic Tac Toe (You WIN)") 
            time.sleep(100)

        end_game()
    else:                                # si no ha ganado nadie empate.
        pygame.display.set_caption("My Tic Tac Toe ( DRAW GAME !!)")

    while check_events()!=-2:
        pass

