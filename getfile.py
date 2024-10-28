#I import tkinter to create ooutr window
import tkinter as tk
#I import zipfile too get oour zip file ready for download
import zipfile
from tkinter import filedialog
from tkinter import *
#I create the parameters for our window using Root tk.Tk()
root = tk.Tk()
#I add a simple title foor this window
root.title("Skull Dev-Ops")
#I create a function to get the file using filedialog and askopenfilename from my computer
def download_files():
    files = []
    file1 = filedialog.askopenfilename(initialdir="/Users/user/Desktop/Portfolio/Fusion.zip", filetypes="Text Files" ["*.zip"])
    zip_filename = "Fusion.zip"
    zip_file = zipfile.ZipFile(zip_filename, "w")

#I create a label for readability so you know what you're downloading
label = tk.Label(root, text="Download Fusion Project Pack>>>")
label.config(foreground="green")
label.pack(side="left")

#I add a button so when the user clicks the button can be ready for download
download = tk.Button(root, text="Download")
download.config(foreground="green")
download.pack(side="right")
#Never foroget the root.mainloop() too close our parameters for this window
root.mainloop()