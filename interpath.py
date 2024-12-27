#Welcome to InterPath My own Community app  for deep web searching. - Rose
import time

#Rose Parker - GitHub Link
my_website = "http://github.com/skulldevops/"

slice = slice(7, -1)

print("...")

print(my_website[slice])

for seconds in range(5, 0, -1):
    print(seconds)
    time.sleep(1)
print("Continue...")

#Imports
#--------#
import tkinter as tk
from tkinter import *

#InterPath User Introduction Page
#----------#
root = tk.Tk()
root.title("InterPath")
root.geometry("800x500")
root.config()

text_title = Label(root, text="InterPath", fg="green", bg="white")
text_title.config(font=("Ariel Bold", 23), width=500, height=1)
text_title.pack()

entry3 = Message(root, text="Welcome to InterPath Search! An innerdimensional portal search tool for ancient text and scripture.")
entry3.config(font=("Ariel Bold", 14), width=500)
entry3.pack()

email_entry = Entry(root)
email_entry.bind()
email_entry.pack()

password_entry = Entry(root)
password_entry.bind()
password_entry.pack()

entry6 = Checkbutton(root, text="I agree to the Terms of Service")
entry6.pack()

#End of Login and Terms Page
#------------#

#------------#
#InterPath User Submit
def submit_form():
    email_entry = email_entry.get()
    password_entry = password_entry.get()
    #User Submit 
    #>>>> 
    #Access to IP Community Page
#-----------#

#-----------#
#Community Access
def ip_page_open():
    ip_page = Toplevel()
    ip_page.title("InterPath")
    ip_page.config(background="beige")
    ip_page.geometry("640x480")
    
    frame = Frame(ip_page)
    frame.pack()
    
    text_title = Label(ip_page, text="InterPath", fg="green", bg="white")
    text_title.config(font=("Ariel Bold", 23), width=500, height=1)
    text_title.pack()
    
    community_page = Message(ip_page, text="Community Page")
    community_page.config(background= "beige", font=("Ariel Bold", 14), width=500)
    community_page.pack()
    
    community_page_announcement = Message(ip_page, text="Welcome to the Community! Please keep our community safe and friendly")
    community_page_announcement.config(background= "beige", font=("Ariel Bold", 8), width=500)
    community_page_announcement.pack()
    
    #Community Header
    #-----------#
    
    #-----------#
    #Community User / Age Form
    def submit_form():
        name_entry = name_entry.get()
        age_entry = age_entry.get()
        
    explore_button = Button(ip_page, text="Explore",command=submit_form)
    explore_button.config(command=ip_page_open_wp)
    explore_button.bind()
    explore_button.pack()
    
    name_entry = Entry(ip_page)
    name_entry.config(background="white")
    name_entry.pack()
    
    age_entry = Entry(ip_page)
    age_entry.config(background="white")
    age_entry.pack()
    
    #End of Community Page
    #---------------------#
    
    #---------------------#
    #IP World Page  
    def ip_page_open_wp():
        ip_page_wp = Toplevel()
        ip_page_wp.title("InterPath")
        ip_page_wp.config(background="beige")
        ip_page_wp.geometry("640x480")
    
        frame_wp = Frame(ip_page_wp)
        frame_wp.pack()
    
        text_title_wp = Label(ip_page_wp, text="InterPath", fg="green", bg="white")
        text_title_wp.config(font=("Ariel Bold", 23), width=500, height=1)
        text_title_wp.pack()
    
        world_page = Message(ip_page_wp, text="World Explorer")
        world_page.config(background= "beige", font=("Ariel Bold", 14), width=500)
        world_page.pack()   
        
        entry_post2 = Text(ip_page_wp)
        entry_post2.config(background="beige")
        entry_post2.pack()
        
        ip_page_wp.mainloop()
       
        #End of World Page
        #----------------#
        
#----------------#     
#IP Portal Submit Access Button   
submit_button = tk.Button(root, text="Enter", fg="blue",command=submit_form)
submit_button.configure(command=ip_page_open)
submit_button.bind()
submit_button.pack()

#End of Code
#-----------#
root.mainloop()