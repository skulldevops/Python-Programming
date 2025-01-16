import tkinter 

root = tkinter.Tk()
root.title("Function Test")
root.geometry("200x150")

def change():
    if clicks:
        print("Updated...")
        return click_count.config(text="Updated...")
    
def update():        
    while user_input.get():
        print("User typing...")
     
def grab():
    while num_input.get() == int():   
        get_num in num_input.get()
        if get_num in num_input.get() == False:
            print("That is not a valid number")
#String test function
click_count = tkinter.Label(root, text="String Test")
click_count.pack()

detect_typing = tkinter.Button(root, text="Detect User Typing...", command=update)
detect_typing.pack()
 
#Label Update function   
clicks = tkinter.Button(root, text="Clicks", command=change)
clicks.pack()

user_input = tkinter.Entry(root)
user_input.pack()

#Num detection function
num_input = tkinter.Entry(root)
num_input.pack()

get_num = tkinter.Button(root, text="Get Number", command=grab)
get_num.pack()

root.mainloop()