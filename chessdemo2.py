#Welcome to chess! - Rose

import pygame as pg

# Define the coordinates and size of the squares (in pixels)
square_size = 30

# Define the color scheme
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Define the starting position of the first row and column
START_POS = (-175, 100)

# Set window settings
pg.init()
pg.display.set_caption("Chess")
screen = pg.display.set_mode((800, 600))

# Set screen settings
screen_width = 800
screen_height = 600
screen_size = (screen_width, screen_height)

# Create the board
board_width = screen_width // 30
board_height = screen_height // 30
board_surface = pg.Surface((30,30))
board_surface.fill((255,255,255))

board = [[0 for i in range(8)] for j in range(8)]

# Set colors
black = pg.Color("black")
white = pg.Color("white")

# Create the screen
screen = pg.display.set_mode(screen_size)


# Create the clock
clock = pg.time.Clock()

# Create the board
board_width = board_width // 30
board_height = board_height // 30

# Create the board squares
board_list = []
for i in range(board_width):
    row = []
    for j in range(board_height):
        square = pg.Rect(i * 30, j * 30, 30, 30)
        row.append(square)
    board_list.append(row)
    
# Create empty board surface
board = pg.Surface((30,30))
# Copy board data onto board surface

# Start game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    board_surface.fill(white)

    # Flip screen
    pg.display.flip()
    clock
    
game = ()
game.run()