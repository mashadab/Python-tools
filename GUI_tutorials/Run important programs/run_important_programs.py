# Creating a GUI from Python program
# Run important programs
# author: Mohammad Afzal Shadab
# email: mashadab@utexas.edu
# date: 14 February 2021
# $ pip install tk
# $ pip install TCL

import tkinter as tk  #for creating the GUI
from tkinter import filedialog, Text 
import os             #allows to run the apps

# Initializing a root
root = tk.Tk()  #holds the app like a body like HTML
apps = []       #placeholder for all files that we are adding

# Defining a function to add the apps to a list
def addApp():
    #widget which attaches to everything in the frame
    for widget in frame.winfo_children(): #to delete information in the frame everytime
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/",title="Select File",
    filetypes=(("executables","*.exe"), ("all files", "."))) #allow us to initiliaze app attributes
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# Defining a function to run the apps in the list
def runApps():
    for app in apps:
        os.startfile(app)

# Printing the earlier saved files in save.txt
if os.path.isfile('save.txt'): #checking if the file exists
    with open('save.txt', 'r') as tempfile:
        tempApps = tempfile.read()
        tempApps = tempApps.split(',')
        apps     = [x for x in tempApps if x.strip()] #strip all the empty spaces

# Adding a canvas
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

# Adding a frame    
frame = tk.Frame(root, bg ="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)   

# Adding buttons
openFile = tk.Button(root, text="Open File", padx=10, 
                     pady=5, fg="white", bg="#263D42", command=addApp)  
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, 
                     pady=5, fg="white", bg="#263D42", command=runApps)  
runApps.pack()

# Printing the saved apps
for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()

# Saving the list as text file when exitting
with open('save.txt','w') as savefile:
    for app in apps:
        savefile.write(app + ',')
        
        
        