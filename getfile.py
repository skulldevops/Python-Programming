import tkinter as tk
import zipfile
from tkinter import filedialog
from tkinter import *
root = tk.Tk()
root.title("Skull Dev-Ops")

def download_files():
    files = []
    file1 = filedialog.askopenfilename(initialdir="/Users/user/Desktop/Portfolio/Fusion.zip", filetypes="Text Files" ["*.zip"])
    zip_filename = "Fusion.zip"
    zip_file = zipfile.ZipFile(zip_filename, "w")

label = tk.Label(root, text="Download Fusion Project Pack>>>")
label.config(foreground="green")
label.pack(side="left")

download = tk.Button(root, text="Download")
download.config(foreground="green")
download.pack(side="right")

root.mainloop()