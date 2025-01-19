#Welcome to Chess 2.0, a PyGame version of my Tkinterchess game
#This is still a work in progress but w are making ti slowly but surely, enjoy!

#Imports
import pygame as pg
import moderngl as mgl
import sys
from model import *

#Chess GUI 1
class ChessGUI:
    def __init(self, master):
        self.master = master
        master.title = "Chess"
        
        self.label = self.Label(master, text="Chess")
        self.label.pack()
        
        self.button = self.Button(master, text="Start Game")
        self.button.pack()

#New chess GUI
class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        pg.init()
        self.WIN_SIZE = win_size
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #------#
        self.ctx = mgl.create_context()
        self.clock = pg.time.Clock()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit() 
                
    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18, 0.20))
        pg.display.flip()
        
    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)    
           
#Board
size = 20

#board length, must be even
boardLength = 8
pg.display.fill("white")

cnt = 0
for i in range(1,boardLength+1):
    for z in range(1,boardLength+1):
        #check if current loop value is even
        if cnt % 2 == 0:
            pg.draw.rect(pg.display, "white",[size*z,size*i,size,size])
        else:
            pg.draw.rect(pg.display, "black", [size*z,size*i,size,size])
        cnt +=1
    #since theres an even number of squares go back one value
    cnt-=1
#Add a nice boarder
pg.draw.rect(pg.display, "black",[size,size,boardLength*size,boardLength*size],1)

pg.display.update()

#Chess piece class
class ChessPiece:
    def __init__(self, color, type, position):
        self.color = color
        self.type = type
        self.position = position
        
    #Chess move piece
    def move(self, new_position):
        # Logic to validate the move based on the piece type
        # ...
        self.position = new_position
    #Chess piece place
    def place(self):
        return f"{self.color} {self.type} at {self.position}"

#----------------------#
# Player 1 Chess Pieces
white_pawn1 = ChessPiece("white", "pawn", "A2")
white_pawn2 = ChessPiece("white", "pawn2", "B2")
white_pawn3 = ChessPiece("white", "pawn3", "C2")
white_pawn4 = ChessPiece("white", "pawn4", "D2")
white_pawn5 = ChessPiece("white", "pawn5", "E2")
white_pawn6 = ChessPiece("white", "pawn6", "F2")
white_pawn7 = ChessPiece("white", "pawn7", "G2")
white_pawn8 = ChessPiece("white", "pawn8", "H2")

white_rook = ChessPiece("white", "rook", "A1")
white_knight = ChessPiece("white", "knight", "B1")
white_bishop = ChessPiece("white", "bishop", "C1")
white_queen = ChessPiece("white", "queen", "D1")
white_king = ChessPiece("white", "king", "E1")
white_bishop2 = ChessPiece("white", "bishop2", "F1")
white_knight2 = ChessPiece("white", "knight2", "G1")
white_rook2 = ChessPiece("white", "rook2", "H1")

#---------------------#
#Player 2 Chess Pieces
black_pawn1 = ChessPiece("black", "pawn", "A7")
black_pawn2 = ChessPiece("black", "pawn2", "B7")
black_pawn3 = ChessPiece("black", "pawn3", "C7")
black_pawn4 = ChessPiece("black", "pawn4", "D7")
black_pawn5 = ChessPiece("black", "pawn5", "E7")
black_pawn6 = ChessPiece("black", "pawn6", "F7")
black_pawn7 = ChessPiece("black", "pawn7", "G7")
black_pawn8 = ChessPiece("black", "pawn8", "H7")

black_rook = ChessPiece("black", "rook", "A8")
black_knight = ChessPiece("black", "knight", "B8")
black_bishop = ChessPiece("black", "bishop", "C8")
black_queen = ChessPiece("black", "queen", "D8")
black_king = ChessPiece("black", "king", "E8")
black_bishop2 = ChessPiece("black", "bishop2", "F8")
black_knight2 = ChessPiece("black", "knight2", "G8")
black_rook2 = ChessPiece("black", "rook2", "H8")

white_pawn1.place()
white_pawn2.place()
white_pawn3.place()

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()      
        
        
        
        
        
        
        
        