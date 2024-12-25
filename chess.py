#Welcome! This is my demo app for a chess game I am creating. It's still a work in progress! - Rose
import tkinter as tk
import time
from tkinter import PhotoImage 
from tkinter import *
from tkinter import Canvas
from PIL import Image, ImageTk, ImageDraw

#Main window
main_window = tk.Tk()
main_window.title("Chess")
main_window.config(background="black")
main_window.geometry("1600x1000")

timer_label = Label(main_window, text="0:00:00")
timer_label.config(font=("Arial Bold", 15), bg="red", fg="white")
timer_label.grid(row=1, column=2)

demo_label = Label(main_window, text="DEMO MODE", fg="black", bg="white")
demo_label.config(font=("Arial Bold", 15))
demo_label.grid(row=3, column=3)

button = Button(main_window, text="Start Game", fg="black", bg="white")
button.config(font=("Arial Bold", 15))
button.grid(row=6, column=2)
  
# Player 1 Score:
labelp1score = Label(main_window, text = "Player 1 Score ")
labelp1score.config(font=("Arial Bold", 32), fg="blue", bg="black")
labelp1score.grid(row=1, column=1)

# Player 2 Score:
labelp2score = Label(main_window, text = "Player 2 Score ")
labelp2score.config(font=("Arial Bold", 32), fg="red", bg="black")
labelp2score.grid(row=1, column=3)

#On-Click event for the board
def on_click(event, board):
    x = event.x
    y = event.y
    row = y // 110
    global column
    column = x // 110
    canvas.itemconfigure(board[row][column], fill="red")
    
#Board Canvas
canvas = Canvas(main_window, borderwidth=10, width = 850, height = 850)
canvas.bind("<Button-1>", on_click)
canvas.grid(row=2, column=2, sticky="nsew")
canvas.config(bg="black")

for i in range(8):
    for j in range(8):
        canvas.create_rectangle(75 * (i + 1) + 75, 75 *(j + 1) + 75, 75 * (i + 2) + 75, 75 * (j + 2) + 75, fill = "black" if (i + j) % 2 == 0 else "beige")

for i in range(8):
    for j in range(8):
        canvas.create_rectangle(75 * (i + 1) + 75, 75 * (j + 1) + 75, 75 * (i + 2) + 75, 75 * (j + 2) + 75, fill= "beige")
        
def get_square_coords(rank, file):
    return rank * 8 + file

square_list = []
for i in range(8):
    for j in range(8):
            square_coords = get_square_coords(i + 1, j + 1)
#Board
board = []
for i in range(8):
    board.append(dict())
    row = []
    for j in range(8):
        square_coords = get_square_coords (i + 1, j + 1)
        row.append(square_coords)
        board.append(dict())
        for square_coords in square_list:
            canvas.bind('<Button-1>', lambda event, square_coords=square_coords: on_click(event, square_coords))
            
#Pieces Rendering
def render_rook(draw, x, y):
  draw.rectangle((x-32, y-32, x+32, y+32), fill=(0, 0, 0)) 

#P1 Chess pieces       
P1Rook1 = Label(text="♖", font=("Comic Sans MS", 28))
P1Rook1.config(bg="beige", fg="black")
P1Rook1.place(x=490, y=210)

P1Knight1 = Label(text="♘", font=("Comic Sans MS", 28))
P1Knight1.config(bg="beige", fg="black")
P1Knight1.place(x=490, y=285)

P1Bishop1 = Label(text="♗", font=("Comic Sans MS", 28))
P1Bishop1.config(bg="beige", fg="black")
P1Bishop1.place(x=490, y=360)

P1Queen1 = Label(text="♕", font=("Comic Sans MS", 28))
P1Queen1.config(bg="beige", fg="black")
P1Queen1.place(x=490, y=435)

P1King = Label(text="♔", font=("Comic Sans MS", 28))
P1King.config(bg="beige", fg="black")
P1King.place(x=490, y=510)

P1Bishop2 = Label(text="♗", font=("Comic Sans MS", 28))
P1Bishop2.config(bg="beige", fg="black")
P1Bishop2.place(x=490, y=585)

P1Knight2 = Label(text="♘", font=("Comic Sans MS", 28))
P1Knight2.config(bg="beige", fg="black")
P1Knight2.place(x=490, y=660)

P1Rook2 = Label(text="♖", font=("Comic Sans MS", 28))
P1Rook2.config(bg="beige", fg="black")
P1Rook2.place(x=490, y=735)

#P1 Pawns

P1Pawn1 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn1.config(bg="beige", fg="black")
P1Pawn1.place(x=565, y=210)

P1Pawn2 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn2.config(bg="beige", fg="black")
P1Pawn2.place(x=565, y=285)

P1Pawn3 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn3.config(bg="beige", fg="black")
P1Pawn3.place(x=565, y=360)

P1Pawn4 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn4.config(bg="beige", fg="black")
P1Pawn4.place(x=565, y=435)

P1Pawn5 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn5.config(bg="beige", fg="black")
P1Pawn5.place(x=565, y=510)

P1Pawn6 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn6.config(bg="beige", fg="black")
P1Pawn6.place(x=565, y=585)

P1Pawn7 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn7.config(bg="beige", fg="black")
P1Pawn7.place(x=565, y=660)

P1Pawn8 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn8.config(bg="beige", fg="black")
P1Pawn8.place(x=565, y=735)

#P2 Chess pieces
P2Rook1 = Label(text="♜", font=("Comic Sans MS", 28))
P2Rook1.config(bg="beige", fg="black")
P2Rook1.place(x=1015, y=210)

P2Knight1 = Label(text="♞", font=("Comic Sans MS", 28))
P2Knight1.config(bg="beige", fg="black")
P2Knight1.place(x=1015, y=285)

P2Bishop1 = Label(text="♝", font=("Comic Sans MS", 28))
P2Bishop1.config(bg="beige", fg="black")
P2Bishop1.place(x=1015, y=360)

P2Queen1 = Label(text="♛", font=("Comic Sans MS", 28))
P2Queen1.config(bg="beige", fg="black")
P2Queen1.place(x=1015, y=435)

P2King = Label(text="♚", font=("Comic Sans MS", 28))
P2King.config(bg="beige", fg="black")
P2King.place(x=1015, y=510)

P2Bishop2 = Label(text="♝", font=("Comic Sans MS", 28))
P2Bishop2.config(bg="beige", fg="black")
P2Bishop2.place(x=1015, y=585)

P2Knight2 = Label(text="♞", font=("Comic Sans MS", 28))
P2Knight2.config(bg="beige", fg="black")
P2Knight2.place(x=1015, y=660)

P2Rook2 = Label(text="♜", font=("Comic Sans MS", 28))
P2Rook2.config(bg="beige", fg="black")
P2Rook2.place(x=1015, y=735)

#P2 Pawns

P2Pawn1 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn1.config(bg="beige", fg="black")
P2Pawn1.place(x=940, y=210)

P2Pawn2 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn2.config(bg="beige", fg="black")
P2Pawn2.place(x=940, y=285)

P2Pawn3 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn3.config(bg="beige", fg="black")
P2Pawn3.place(x=940, y=360)

P2Pawn4 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn4.config(bg="beige", fg="black")
P2Pawn4.place(x=940, y=435)

P2Pawn5 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn5.config(bg="beige", fg="black")
P2Pawn5.place(x=940, y=510)

P1Pawn6 = Label(text="♟", font=("Comic Sans MS", 28))
P1Pawn6.config(bg="beige", fg="black")
P1Pawn6.place(x=940, y=585)

P2Pawn7 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn7.config(bg="beige", fg="black")
P2Pawn7.place(x=940, y=660)

P2Pawn8 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn8.config(bg="beige", fg="black")
P2Pawn8.place(x=940, y=735)

main_window.mainloop()