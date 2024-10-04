#Adding my imports
import tkinter as tk
import time
from datetime import datetime
from time import strftime

#Root window and dimensions
root = tk.Tk()
root.title("Dev Clock")
root.geometry("300x200")
root.config(background="orange")
#This label will display what Today's day is
title_label = tk.Label(root, text="Today's Date Is")
title_label.pack(fill="x", expand=1)

#Date label
date_label = tk.Label(root, padx=15, pady=5, text=strftime("%B %d, %Y"))
date_label.pack(fill="x", expand=1)

#Clock label
clock_label = tk.Label(root, font=("Arial"), text=datetime.now())
clock_label.pack(fill="x", expand=1)

#While true loop for updated time function
while True:
    #New time update
    root.update()
    new_time = datetime.now()
#Current date label
    date_label["text"] = strftime("%B %d, %Y")
#Current day label
    current_day = str(new_time.strftime("%A"))
    day_label = tk.Label(root, text=current_day)
    day_label.pack(fill="x", expand=1)
#Current time label
    clock_label["text"] = strftime("%H:%M %p")
    hour = str(new_time.hour)
    minute = str(new_time.minute)
    am_pm = "AM" "PM"
#Terminal Print if clock is running
    print("Clock updated...")
#Time sleep to update time regularly
    time.sleep(1)
#End the application with root.mainloop()
    root.mainloop()
