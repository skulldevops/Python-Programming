import tkinter 

root = tkinter.Tk()
root.title("Function Test")
root.geometry("300x300")

name = ["Mario, Luigi, Wario"]
grocery = ["Bananas", "Oranges", "Apples"]

a_value = 0
b_value = 0
result = 0

#Update Function
def update():
    if clicks:
        print("Updating...")
        print("Done!")
        return click_count.config(text="Updated!")
    
#Detect user typing Function 
def change():        
    if user_input.get():
        print("User typing...")
    else: 
        user_input.get() == None
        print("No words detected")
        
#Add function       
def on_click_plus():
    a_value = float(entry1.get())
    b_value = float(entry2.get())
    result = a_value + b_value
    entry3.insert(0, result)
    
def clear_entry3():
    entry3.delete(0, tkinter.END)
    
#List Function
def print_list():
    if list_entry.get() == "name":
        print(name)
        return list_label.config(text="Name list printed!")
    elif list_entry.get() == "grocery":
        print(grocery)
        return list_label.config(text="Grocery list printed!")
    else:
        user_input.get() == None
        print("No list detected!")
        return list_label.config(text="No list detected!")
            
#String test function
click_count = tkinter.Label(root, text="String Test")
click_count.pack()

detect_typing = tkinter.Button(root,text="Detect User Typing", command=change)
detect_typing.pack()
 
#Label Update function   
clicks = tkinter.Button(root, text="Update", command=update)
clicks.pack()

user_input = tkinter.Entry(root)
user_input.pack()

#Add Function
entry1 = tkinter.Entry(root, textvariable=input)
entry1.pack()

entry2 = tkinter.Entry(root, textvariable=input)
entry2.pack()

#Add Button and Clear button

button = tkinter.Button(root, text="+", width=5)
button.pack(side="left")
button.bind(on_click_plus)
button.config(command=on_click_plus)

clear_button =tkinter.Button(root,width=3, text="Clear", command=lambda: clear_entry3())
clear_button.bind(clear_entry3)
clear_button.pack(side="left")

entry3 = tkinter.Entry(root, textvariable=input)
entry3.pack()

#List Function
list_entry = tkinter.Entry(root)
list_entry.pack()

list_label = tkinter.Label(root, text="___List___")
list_label.pack()

get_list = tkinter.Button(root, text="Print", command=print_list)
get_list.pack()

root.mainloop()