#Adding my imports
import tkinter as tk
import time
from datetime import datetime
from time import strftime

#Root window and dimensions
root = tk.Tk()
root.title("Dev Clock")
root.geometry("300x200")
root.config(background="grey")
#This label will display what Today's day is
title_label = tk.Label(root, text="Today's Date Is", font=("Arial", 12))
title_label.pack(fill="x", expand=1)

day_label = tk.Label(root, font=("Arial", 12),text=strftime("%A"))
day_label.pack(fill="x", expand=1)

#Date label
date_label = tk.Label(root, padx=1, pady=1, text=strftime("%B %d, %Y"), font=("Arial", 12))
date_label.pack(fill="x", expand=1)

#Clock label
clock_label = tk.Label(root, font=("Arial", 12), text=datetime.now())
clock_label.pack(fill="x", expand=1)

#While true loop for updated time function
while True:
    #New time update
    root.update()
    new_time = datetime.now()
#Current date label
    date_label["text"] = strftime("%B %d, %Y")
#Current day label
    day_label["text"] = strftime("%A")
#Current time label
    clock_label["text"] = strftime("%H:%M:%S")
    
    hour = str(new_time.hour)
    minute = str(new_time.minute)
    second = str(new_time.second)
    am_pm = "AM" "PM"
#Terminal Print if clock is running
#Time sleep to update time regularly
    time.sleep(1)
#End the application with root.mainloop()
root.mainloop()
