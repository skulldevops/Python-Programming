#Welcome! This is my demo app for a chess game I am creating. It's still a work in progress! - Rose
import tkinter as tk
import time
from datetime import datetime
from time import strftime
from tkinter import *
from tkinter import Canvas


#Rose Parker - GitHub Link
my_website = "http://github.com/skulldevops/"

slice = slice(7, -1)

print("...")

print(my_website[slice])

for seconds in range(3, 0, -1):
    print(seconds)
    time.sleep(1)
print("Continue...")

#Main window
main_window = tk.Tk()
main_window.title("Chess")
main_window.config(background="white")
main_window.geometry("2048x1000")

demo_label = Label(main_window, text="DEMO MODE", fg="black", bg="white")
demo_label.config(font=("Arial Bold", 20))
demo_label.grid(row=3, column=3)

start_button = Button(main_window, text="Start Game", fg="black", bg="white")
start_button.bind()
start_button.config(font=("Arial Bold", 15))
start_button.grid(row=6, column=2)
  
# Player 1 Score:
labelp1score = Label(main_window, text = "Player 1 Score ")
labelp1score.config(font=("Arial Bold", 32), fg="white", bg="white")
labelp1score.grid(row=1, column=1)

# Player 2 Score:
labelp2score = Label(main_window, text = "Computer Score ")
labelp2score.config(font=("Arial Bold", 32), fg="white", bg="white")
labelp2score.grid(row=1, column=3)

class Chessboard:
    def __init__(self):
        self.board = []

square_list = []
window_x = main_window.winfo_x
window_y = main_window.winfo_y

piece_height = 75

def on_click_motion(event):
 # Move the piece to the clicked square
        def get_row_and_column_from_click(event):
    # Get the coordinates of the click
            x = event.x
            y = event.y
    # Convert to row and column indexes   
            row = get_row_and_column_from_click(event)
            column = get_row_and_column_from_click(event)
            print(f"Row: {event.x}, Column: {event.y}")
    # Update the piece's position on the screen

def get_square_coords(rank, file):
    return rank * 8 + file
           
#Board Canvas

chess_canvas = Canvas(main_window, borderwidth=10, width = 850, height = 850)
chess_canvas.bind()
chess_canvas.grid(row=2, column=2, sticky="nsew")
chess_canvas.config(bg="gray")
        
for i in range(8):
    for j in range(8):
        chess_canvas.create_rectangle(75 * (i + 1) + 75, 75 *(j + 1) + 75, 75 * (i + 2) + 75, 75 * (j + 2) + 75, fill = "black" if (i + j) % 2 == 0 else "black")

for i in range(8):
    for j in range(8):
        chess_canvas.create_rectangle(75 * (i + 1) + 75, 75 * (j + 1) + 75, 75 * (i + 2) + 75, 75 * (j + 2) + 75, fill= "beige" if (i + j) % 2 == 0 else "black")   
     
for i in range(8):
    for j in range(8):
            square_coords = get_square_coords(i + 1, j + 1)



#Piece List

#P1 Chess pieces  
     
P1Rook1 = Label(text="♖", font=("Comic Sans MS", 28))
P1Rook1.bind("<Button-1>", on_click_motion)
P1Rook1.config(bg="gray", fg="black")
P1Rook1.place(x=490, y=210)

P1Knight1 = Label(text="♘", font=("Comic Sans MS", 28))
P1Knight1.bind("<Button-1>", on_click_motion)
P1Knight1.config(bg="gray", fg="black")
P1Knight1.place(x=490, y=285)

P1Bishop1 = Label(text="♗", font=("Comic Sans MS", 28))
P1Bishop1.bind("<Button-1>", on_click_motion)
P1Bishop1.config(bg="gray", fg="black")
P1Bishop1.place(x=490, y=360)

P1Queen1 = Label(text="♕", font=("Comic Sans MS", 28))
P1Queen1.bind("<Button-1>", on_click_motion)
P1Queen1.config(bg="gray", fg="black")
P1Queen1.place(x=490, y=435)

P1King = Label(text="♔", font=("Comic Sans MS", 28))
P1King.bind("<Button-1>", on_click_motion)
P1King.config(bg="gray", fg="black")
P1King.place(x=490, y=510)

P1Bishop2 = Label(text="♗", font=("Comic Sans MS", 28))
P1Bishop2.bind("<Button-1>",on_click_motion)
P1Bishop2.config(bg="gray", fg="black")
P1Bishop2.place(x=490, y=585)

P1Knight2 = Label(text="♘", font=("Comic Sans MS", 28))
P1Knight2.bind("<Button-1>", on_click_motion)
P1Knight2.config(bg="gray", fg="black")
P1Knight2.place(x=490, y=660)

P1Rook2 = Label(text="♖", font=("Comic Sans MS", 28))
P1Rook2.bind("<Button-1>", on_click_motion)
P1Rook2.config(bg="gray", fg="black")
P1Rook2.place(x=490, y=735)

#P1 Pawns

P1Pawn1 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn1.bind("<B1-Motion>", on_click_motion)
P1Pawn1.config(bg="gray", fg="black")
P1Pawn1.place(x=565, y=210)

P1Pawn2 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn2.bind("<Button-1>", on_click_motion)
P1Pawn2.config(bg="gray", fg="black")
P1Pawn2.place(x=565, y=285)

P1Pawn3 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn3.bind("<Button-1>", on_click_motion)
P1Pawn3.config(bg="gray", fg="black")
P1Pawn3.place(x=565, y=360)

P1Pawn4 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn4.bind("<Button-1>", on_click_motion)
P1Pawn4.config(bg="gray", fg="black")
P1Pawn4.place(x=565, y=435)

P1Pawn5 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn5.bind("<Button-1>", on_click_motion)
P1Pawn5.config(bg="gray", fg="black")
P1Pawn5.place(x=565, y=510)

P1Pawn6 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn6.bind("<Button-1>", on_click_motion)
P1Pawn6.config(bg="gray", fg="black")
P1Pawn6.place(x=565, y=585)

P1Pawn7 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn7.bind("<Button-1>", on_click_motion)
P1Pawn7.config(bg="gray", fg="black")
P1Pawn7.place(x=565, y=660)

P1Pawn8 = Label(text="♙", font=("Comic Sans MS", 28))
P1Pawn8.bind("<Button-1>", on_click_motion)
P1Pawn8.config(bg="gray", fg="black")
P1Pawn8.place(x=565, y=735)

#P2 Chess pieces

P2Rook1 = Label(text="♜", font=("Comic Sans MS", 28))
P2Rook1.bind("<Button-1>", on_click_motion)
P2Rook1.config(bg="gray", fg="black")
P2Rook1.place(x=1015, y=210)

P2Knight1 = Label(text="♞", font=("Comic Sans MS", 28))
P2Knight1.bind("<Button-1>", on_click_motion)
P2Knight1.config(bg="gray", fg="black")
P2Knight1.place(x=1015, y=285)

P2Bishop1 = Label(text="♝", font=("Comic Sans MS", 28))
P2Bishop1.bind("<Button-1>", on_click_motion)
P2Bishop1.config(bg="gray", fg="black")
P2Bishop1.place(x=1015, y=360)

P2Queen1 = Label(text="♛", font=("Comic Sans MS", 28))
P2Queen1.bind("<Button-1>", on_click_motion)
P2Queen1.config(bg="gray", fg="black")
P2Queen1.place(x=1015, y=435)

P2King = Label(text="♚", font=("Comic Sans MS", 28))
P2King.bind("<Button-1>", on_click_motion)
P2King.config(bg="gray", fg="black")
P2King.place(x=1015, y=510)

P2Bishop2 = Label(text="♝", font=("Comic Sans MS", 28))
P2Bishop2.bind("<Button-1>", on_click_motion)
P2Bishop2.config(bg="gray", fg="black")
P2Bishop2.place(x=1015, y=585)

P2Knight2 = Label(text="♞", font=("Comic Sans MS", 28))
P2Knight2.bind("<Button-1>", on_click_motion)
P2Knight2.config(bg="gray", fg="black")
P2Knight2.place(x=1015, y=660)

P2Rook2 = Label(text="♜", font=("Comic Sans MS", 28))
P2Rook2.bind("<Button-1>", on_click_motion)
P2Rook2.config(bg="gray", fg="black")
P2Rook2.place(x=1015, y=735)

#P2 Pawns

P2Pawn1 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn1.bind("<Button-1>", on_click_motion)
P2Pawn1.config(bg="gray", fg="black")
P2Pawn1.place(x=940, y=210)

P2Pawn2 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn2.bind("<Button-1>", on_click_motion)
P2Pawn2.config(bg="gray", fg="black")
P2Pawn2.place(x=940, y=285)

P2Pawn3 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn3.bind("<Button-1>", on_click_motion)
P2Pawn3.config(bg="gray", fg="black")
P2Pawn3.place(x=940, y=360)

P2Pawn4 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn4.bind("<Button-1>", on_click_motion)
P2Pawn4.config(bg="gray", fg="black")
P2Pawn4.place(x=940, y=435)

P2Pawn5 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn5.bind("<Button-1>", on_click_motion)
P2Pawn5.config(bg="gray", fg="black")
P2Pawn5.place(x=940, y=510)

P2Pawn6 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn6.bind("<Button-1>", on_click_motion)
P2Pawn6.config(bg="gray", fg="black")
P2Pawn6.place(x=940, y=585)

P2Pawn7 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn7.bind("<Button-1>", on_click_motion)
P2Pawn7.config(bg="gray", fg="black")
P2Pawn7.place(x=940, y=660)

P2Pawn8 = Label(text="♟", font=("Comic Sans MS", 28))
P2Pawn8.bind("<Button-1>", on_click_motion)
P2Pawn8.config(bg="gray", fg="black")
P2Pawn8.place(x=940, y=735)

#Clock and Time

#Clock label
clock_label = Label(main_window, text=datetime.now(), font=("Ariel", 28))
clock_label.bind()
clock_label.config(bg="white", fg="black")
clock_label.grid(row=1, column=2)

while True:
#New time update
    main_window.update()
    new_time = datetime.now()
    
#Current time label
    clock_label["text"] = strftime("%H:%M %p")
    hour = str(new_time.hour)
    minute = str(new_time.minute)
    am_pm = "AM" "PM"

    main_window.mainloop()
    