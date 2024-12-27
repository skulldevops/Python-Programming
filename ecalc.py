#This is a Python Dev Calc App I created, starting with creating a window using Tkinter
#Rose Parker - GitHub Link
import time
my_website = "http://github.com/skulldevops/"

slice = slice(7, -1)

print("...")

print(my_website[slice])

for seconds in range(5, 0, -1):
    print(seconds)
    time.sleep(1)
print("Continue...")

#Imports
import tkinter as tk

root = tk.Tk()
root.title("Dev-Calc App")

import math as math

#I create a label title within the app, just for a more pleasing GUI
label_title = tk.Label(root, text="DEV CALC")
label_title.pack(side="top", padx=10, pady=10)
label_title.config(fg='blue')

#I define my values we will need for the app, two inputs and an output for the results
a_value = 0
b_value = 0
label_c = tk.Label(root, text ="Result")
result = 0


#Plus Button function
def on_click_plus():
    a_value = float(entry.get())
    b_value = float(entry2.get())
    result = a_value + b_value
    entry3.insert(0, result)

#Minus Button function
def on_click_minus():
    a_value = float(entry.get())
    b_value = float(entry2.get())
    result = a_value - b_value
    entry3.insert(0, result)

#Divide Button function
def on_click_divide():
    a_value = float(entry.get())
    b_value = float(entry2.get())
    result = a_value / b_value
    entry3.insert(0, result)

#Multiply Button function
def on_click_multiply():
    a_value = float(entry.get())
    b_value = float(entry2.get())
    result = a_value * b_value
    entry3.insert(0, result)

def clear_entry3():
    entry3.delete(0, tk.END)

#First Number entry
entry = tk.Entry(root, width=5)
entry.pack(side=tk.LEFT, fill=tk.X)

#Second Number entry
entry2 = tk.Entry(root, width=5)
entry2.pack(side=tk.LEFT, fill=tk.X)

#Plus Button
button = tk.Button(root, text="+", width=5)
button.pack(side="left")
button.bind(on_click_plus)
button.config(command=on_click_plus)

#Minus Button
button2 = tk.Button(root, text="-", width=5)
button2.pack(side="left")
button2.bind(on_click_minus)
button2.config(command=on_click_minus)

#Divide Button
button3 = tk.Button(root, text="/", width=5)
button3.pack(side="left")
button3.bind(on_click_divide)
button3.config(command=on_click_divide)

#Multiply Button
button4 = tk.Button(root, text="*", width=5)
button4.pack(side="left")
button4.bind(on_click_multiply)
button4.config(command=on_click_multiply)

#Clear Button
clear_button =tk.Button(root,width=3, text="Clear", command=lambda: clear_entry3())
clear_button.bind(clear_entry3)
clear_button.pack(side="left")

#Result Entry Display
entry3 = tk.Entry(root, width=4)
entry3.insert(0, result)
entry3.pack(side=tk.RIGHT, fill=tk.X)

#Result Label of Entries
label_c.text = "Result" + str(result)
label_c.pack(side=tk.LEFT)

root.mainloop()