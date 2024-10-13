#Welcoome too a simple clicker, I start with importing tkinter for our app
import tkinter
root = tkinter.Tk()
#I add a title and name it
root.title("Just a Clicker")
#I set our window dimensions
root.geometry("200x65")
#I set num as 0 for our click counter to update {num}
num = 0
#I add a label to display the number of clicks with the push of a button
label = tkinter.Label(root, text="0")
label.pack()
#I create a function that counts and grabs the {num} of clicks using global
def count_clicks():
    global num
    num += 1
    label.config(text=f"{num}")

#I create a button that prompts the user to click the button, which will update
#the clicks every time it's pressed
button = tkinter.Button(root, text="Click", command=count_clicks)
button.config(foreground="red")
button.pack()
root.mainloop()