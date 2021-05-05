import pygame
from pygame.locals import *
from tictactoe_data import * 
import time
import sys 



def game_init():
    global gameDisplay, white,line_color,width, height
    global CLOCK,fps, XO,x_img,o_img
    global game_over
    
    
    game_over=False
    white=(255,255,255) # color RGB (red,green,blue)
    line_color=(0,0,155)
    width=400
    height=400
    
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
    
    pygame.display.set_caption("My Tic Tac Toe ( X )") 
    XO='x'
    init_board()



def drawXO(pos): 
    global XO
    
    row=(pos-1)//3 #  n fila
    col=(pos-1)%3  # n col

    posx = width // 3 * (row) + 30 #  
    posy = height // 3 * (col) + 30

    if(XO == 'x'): 
        gameDisplay.blit(x_img, (posy, posx))
        pygame.display.set_caption("My Tic Tac Toe ( O )") 
        XO = 'o' 
    else: 
        gameDisplay.blit(o_img, (posy, posx))
        pygame.display.set_caption("My Tic Tac Toe ( X )") 
        XO = 'x' 
  


    
def cross_lines(line,w):
    global game_over    

    # still playing
    if line==-1:                              
       return
    

    game_over=True
    # draw
    if line == 0:
       pygame.display.set_caption("My Tic Tac Toe ( DRAW GAME !!)") 
       return
    

    L = 'X' if w == 1 else 'O'
    pygame.display.set_caption("My Tic Tac Toe (" + str(L)+" WINS )") 

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
 
    
    

def user_click(): 
    global XO
    x, y = pygame.mouse.get_pos() 
     
    if(x<width / 3): 
        col = 1
    elif (x<width / 3 * 2): 
        col = 2
    elif(x<width): 
        col = 3
    else: 
        col = None

    if(y<height / 3): 
        row = 1    
    elif (y<height / 3 * 2): 
        row = 2
    elif(y<height): 
        row = 3
    else: 
        row = None
        
    p=col+3*(row-1) 
    
    if p in possible_moves() and not game_over:
        line,winner= jugar(p,XO) 
        drawXO(p)
        cross_lines(line,winner)
    
        

def game_reset():
    global XO, game_over    
    init_board()
    game_over = False   
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
            user_click() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_reset()



def draw_board():
    gameDisplay.fill(white) 
    
    # drawing vertical lines 
    pygame.draw.line(gameDisplay, line_color, (width / 3, 0), (width / 3, height), 7) 
    pygame.draw.line(gameDisplay, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7) 

    # drawing horizontal lines 
    pygame.draw.line(gameDisplay, line_color, (0, height / 3), (width, height / 3), 7) 
    pygame.draw.line(gameDisplay, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    
    CLOCK.tick(fps)   



def main():
    game_init()
    draw_board()    

    while True:   
        check_events()
        pygame.display.update()
 



if __name__ == "__main__":
    main()
                                                               