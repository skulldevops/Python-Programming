from tkinter import*
import tkinter as tk
from functools import partial
root = tk.Tk
input1 = StringVar(value = "")
input2 = StringVar(value = "")
result = StringVar(value = " ")
add = ()
subtract = ()
light_gray = "#f5f5f5"
def increment(input1):
     input1.set(int(input1.get()))

e1 = Entry(root, textvariable = input1)
e2 = Entry(root, textvariable = input2)

i1 = Label(root, text = "Enter something")
i1.grid (row = 0, column = 0)

i2 = Label(root, text = "And another thing")
i2.grid(row = 1, column = 1)

plus_button = Button(root, text = "+")
plus_button.config(command = lambda increment: input1)
plus_button.config(background = light_gray)
plus_button.pack(side = "right", padx = 10)
plus_button.grid(row = 0, column = 1)
plus_button.grid(row = 2, column = 0)
plus_button.config(command = lambda add:(e1.get(), e2.get()))

minus_button = Button(root, text = "-" , command = lambda result:set(subtract(int(input1.get()), int(input2.get()))))
minus_button.config(command = lambda increment: input1)
minus_button.config(background = light_gray)
minus_button.pack(side = "left" , padx = 10)
minus_button.grid(row = 0, column = 2)
minus_button.grid(row = 3, column = 1)
minus_button.config(command = lambda subtract:(e1.get(), e2.get()))

e1 = Entry(root, width=50)
e1.grid(row = 0, column = 1)

e2 = Entry(root, width=50)
e2.grid(row = 1, coolumn = 0)


root = tk.Tk()
root.title("Simple Dev Calc")

i = Label(root, text ="-")
i1 = Label(root, text = "Enter something")
i1.grid(row = 0, column = 1)

i2 = Label(root, text = "And another thing")
i2.grid(row = 1, column = 1)

def get_input():
        input1.set(e1.get())
        input2.set(e2.get())
b1 = Button(root, text = "Get Input", command = get_input)
b1.grid(row = 2, column = 0)
root.mainloop()
num1 = 0 , num2 = 0, result = ""

result_label = tk.Label(root, textvariable = result, font = ("Arial", 14))
result_label.pack(pady = 10)
result_entry = Entry(root, width = 10, font = ("Arial , 20") , background = "white")
result_entry.pack(pady = 10)
result_entry.grid(row = 0, column = 2)

def add(num1, num2):
    global input1, input2, result
    return num1 + num2
result.set(str(float(num1) + float(num2)))
minus_button.config(command = lambda subtract:(e1.get(), e2.get()))
plus_button.config(command = lambda add:(e1.get(), e2.get()))

def subtract(num1, num2):
    return num1 - num2
print(result.get())
e1 = Entry(root)
e2 = Entry(root)
i = Label(root, text ="-")

exit_button = tk.Button(root, text ="Exit" , command= root.destroy)
exit_button.pack(side= "bottom")