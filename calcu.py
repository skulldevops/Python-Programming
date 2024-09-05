#   Welcome to my first fully coded calculator using Python. This is a work in progress as I'm always loookng to improve my creations and share them
#   First, I start with importing our tkinter module and add root along with our root title Which is Simple Dev Calc* for now.
from tkinter import*
import tkinter as tk
root = tk.Tk()
root.title("Simple Dev Calc")
#   In order to start building in our separate window we have to add defined elements that are connected to funtons that can be called by our output 
#   and displayed for the user, like any basic calculator application. Starting with our first entry, an integer
input_1 = (Entry)
#   Adding our second integer soo that the functions can equate the two numbers properly
input_2 = (Entry)
#   Adding labels for extra user interaction, making it look like a real calculator
input_1_L = (Label)
input_2_L = (Label)
#   And our results to call the final functons to sum everything up[ and display back an answer to the user
result = StringVar(value = "")
light_gray = "#f5f5f5"
white = "#000000"
#   These two def functions will get the inputs when called to do so by clicking the button.
def increment(input1):
     input_1.set(int(input_1.get()))
def increment(input2):
     input_2.set(int(input_2.get()))
#   Here both oof our labeled entry buttons, so the user can navigate to the boxes properly, just an extra step to make everything look nice 
#   and put together for the user
input_1_L = Button(root, text = "Enter # ", width = 5, background = white)
input_1_L.grid (row = 1, column = 1)
#   Here is our labeled entry buttons, so that the user can know where to go
input_2_L = Button(root, text = "Enter # ", width = 5, background = white)
input_2_L.grid(row = 1, column = 2)
#   Here is our first entry boox foor the user too input an integer specifically since we are using a calculator, everything will be done in 
#   another window in an application that we created by importing our modules at the top of our script
input_1 = Entry(root, textvariable = input_1)
input_1 = Entry(root, width = 50, background = light_gray)
input_1.config(background = light_gray)
input_1.pack(side = "left" , padx = 25)
input_1.grid(row = 0, column = 1)
input_1.grid(row = 0, column = 1)
#   Here is our 2nd entry box, so the user csn enter another integer to be evaluated by our functions and sent to results
input_2 = Entry(root, textvariable = input_2)
input_2 = Entry(root, width = 50, background = light_gray)
input_2.config(background = light_gray)
input_2.pack(side = "right", padx = 25)
input_2.grid(row = 0, column = 2)
input_2.grid(row = 0, column = 2)
#   Here is our plus button, the first of our buttoons, in order for us to call one function oof the buttons of a calculator we have too make 
#   sure that they are labeled and identified correctly
plus_button = Button(root, text = "+" , command = lambda increment: input_1)
plus_button.config(command = lambda increment: input_1)
plus_button.config(background = light_gray)
plus_button.pack(side = "right", padx = 10)
plus_button.grid(row = 0, column = 2)
plus_button.grid(row = 0, column = 2)
#   Here is the minus button, which is also identified with the minus sign, that way we can identify our buttons and call these buttons to allow 
#   results to get the proper equation done
minus_button = Button(root, text = "-" , command = lambda increment: input_1)
minus_button.config(command = lambda increment: input_1)
minus_button.config(background = light_gray)
minus_button.pack(side = "right" , padx = 10)
minus_button.grid(row = 0, column = 1)
minus_button.grid(row = 0, column = 1)
#   Here is the get results function after we enter an integer into our entry, this function will call exactly what's froom the entry and make sure 
#   it's an integer to be calculated
def get_input():
        input_1.set(input_1.get())
        input_2.set(input_2.get())
b1 = Button(root, text = "Get Input", command = get_input)
b1.grid(row = 0, column = 3)
#   Here is my mainloop(), adding all oof my elements inside, anything outside the mainloop is a product of the function after everything is set correctly.
root.mainloop()
#   Here I add my def functions, starting with our add function to perform the correct evaluations before the user can move foward
def add(input_1, input_2):
     return input_1 + input_2
print(result.get())
input_1 = Entry(root)
input_2 = Entry(root)
i = Label(root, text = "+")   
#   Here is the subtract function, same funtion but different result
def subtract(input_1, input_2):
    return input_1 - input_2
print(result.get())
input_1 = Entry(root)
input_2 = Entry(root)
i = Label(root, text = "-")
#   Here is the get result functioon, which will get the result of input_1 and input2 so after it gets those it can display the correct sum of both of the user inputs implemented in our calculator
def add(input_1, input_2):
    input_1, input_2, result
    return input_1 + input_2
result.set(str(float(input_1) + float(input_2)))
minus_button.config(command = lambda subtract:(input_1.get(), input_2.get()))
plus_button.config(command = lambda add:(input_1.get(), input_2.get()))
#   This is the results display, making it visible for the user
result = tk.Label(root, textvariable = result, font = ("Arial", 14))
result = Entry(root, width = 10, font = ("Arial , 20") , background = "white")
result.grid(row = 0, column = 2)
result.pack(pady = 10)
#   I add an exit button to make sure that the user can close the program before anything else, if they cn't cloose the program there will be problems with the script
exit_button = tk.Button(root, text ="Exit" , command = root.destroy)
exit_button.pack(side= "bottom")