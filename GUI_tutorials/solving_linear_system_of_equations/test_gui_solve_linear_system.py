import tkinter as tk  
import speech_recognition as sr 
import pyaudio
import os , shutil , sys
import webbrowser
from tkinter import ttk , messagebox as m_box , font , filedialog

win = tk.Tk()
win.title("Equation Solver")

# 2 EQUATION 2 SOLVER

# LINKS 

facebook_link = "https://www.facebook.com/aryan.shridhar.1"
instagram_link = "https://www.instagram.com/aryanshridhar_007/"
twitter_link = "https://twitter.com/ShridharAryan"
gmail_link = "https://mail.google.com/mail/u/0/#inbox"

# FILE 

# PWD 

with open(os.getcwd() + r"\History.txt" , "a") as f:
    f.close()

with open(os.getcwd() + r"\Help.txt" , "w") as f:
    f.write('''Developed by - Aryan Shridhar\nVIT University\nEmail :- aryanshridhar7@gmailcom\n\nEquation solver is a application which helps us to solve 2 equation in 2 variable or\n3 equation in 3 variable in just a click.\n\nAbout Speech Recognition : \n\nThis brand new feature can solve equations based on your voice \nPrerequisites : \n1.Make sure you are connected to internet\n2.Make sure your microphone is turned on\n3.Make sure there no background voice\n\nFor 2 equation 2 variable  :-\n\nEquation 1 - a1x + b1y = c1\nEquation 2 - a2x + b2y = c2\n\nSpeak in the format - \n\nFirst equation A is \"Your number\" ,B is \"Your number\" , C is \"Your number\"\nSecond Equation A is \"Your number\" , B is \"Your number\" , C is \"Your number\"\n\nFor 3 equation 3 variable :- \n\nEquation 1 - a1x + b1y + c1z = d1\nEquation 2 - a2x + b2y + c2z = d2\nEquation 3 - a3x + b3y + c3z = d3\n\nSpeak in format of :- \n\nFirst equation A is \"Your number\" , B is \"Your number\" , C is \"Your number\" , D is \"Your number\"\nSecond Equation A is \"Your number\" , B is \"Your number\" , C is \"Your number\" , D is \"Your number\"\nThird Equation A is \"Your number\" , B is \"Your number\" , C is \"Your number\" , D is \"Your number\"\n\nEdit :- Speech recognition may take some time depending upon the clarity with which you speak\n\nSorry for the inconvenience causing , we are trying to upgrade\n\n\n\n**time to code ~ 20 hours**''')


# ICONS 

insta_icon = tk.PhotoImage(file = r"E:\Python Projects\Equation Solver\icons\instagram7.png")
face_icon = tk.PhotoImage(file  = r"E:\Python Projects\Equation Solver\icons\facebook4.png")
twitter_icon = tk.PhotoImage(file = r"E:\Python Projects\Equation Solver\icons\twitter1.png")


# FUNCTIONS

# THEME 

def func_black():
    page1.config(background = "Black")
    page2.config(background = "Black")
def func_red():
    page1.config(background = "Red")
    page2.config(background = "Red")    
def func_default():
    page1.config(background = "SystemButtonFace")
    page2.config(background = "SystemButtonFace")  
def func_blue():
    page1.config(background = "Blue")
    page2.config(background = "Blue")
def func_grey():
    page1.config(background = "Grey")
    page2.config(background = "Grey")      
def func1():
    m_box.showinfo("Histroy location" , f"{os.getcwd()}")      
def func2(event = ""):
    pass
    entry_eqn1a.delete(0,tk.END)
    entry_eqn1b.delete(0,tk.END)
    entry_eqn1c.delete(0,tk.END)
    entry_eqn2a.delete(0,tk.END)
    entry_eqn2b.delete(0,tk.END)
    entry_eqn2c.delete(0,tk.END)
    entry_eqn3a.delete(0,tk.END)
    entry_eqn3b.delete(0,tk.END)
    entry_eqn3c.delete(0,tk.END)
    entry_eqn3d.delete(0,tk.END)
    entry_eqn4a.delete(0,tk.END)
    entry_eqn4b.delete(0,tk.END)
    entry_eqn4c.delete(0,tk.END)
    entry_eqn4d.delete(0,tk.END)
    entry_eqn5a.delete(0,tk.END)
    entry_eqn5b.delete(0,tk.END)
    entry_eqn5c.delete(0,tk.END)
    entry_eqn5d.delete(0,tk.END)

def func3(event = ""):
    os.startfile(os.getcwd() + r"\History.txt")
def func4(event = ""):
    if os.stat(os.getcwd() + r"\History.txt").st_size == 0:
        m_box.showerror("Error" , "Nothing to clear")
    else:
        with open(os.getcwd() + r"\History.txt","w") as f:
            f.close()
        m_box.showinfo("History" , "Cleared")         
def func5(event = ""):
    os.startfile(os.getcwd() + r"\Help.txt")
def func6():
    m_box.showinfo("Feedback" , "Email your feedback at:\naryanshridhar7@gmail.com")
    webbrowser.open_new(gmail_link)   
def func7(event = ""):
    webbrowser.open_new(facebook_link) 
def func8(event = ""):
    webbrowser.open_new(instagram_link)    
def func9(event = ""):
    webbrowser.open_new(twitter_link)
def func10():
    command = radio_var.get()
    a1= eqn1_a_var.get()
    b1 = eqn1_b_var.get()
    c1 = eqn1_c_var.get()
    a2 = eqn2_a_var.get()
    b2 = eqn2_b_var.get()
    c2 = eqn2_c_var.get()
    if command == 'Text':
        try:
            if "." in a1:
                a1= float(a1)
            else:
                a1= int(a1)
            if "." in b1:
                b1= float(b1)
            else:
                b1= int(b1) 
            if "." in c1:
                c1= float(c1)
            else:
                c1= int(c1)     
            if "." in a2:
                a2= float(a2)
            else:
                a2= int(a2)     
            if "." in b2:
                b2= float(b2)
            else:
                b2= int(b2)
            if "." in c2:
                c2= float(c2)
            else:
                c2= int(c2)    
        except ValueError:
            m_box.showerror("Error" , "Enter data in integer only")    
        else:
            try:
                num = 5/((a1*b2) - (a2*b1))
            except ZeroDivisionError:
                m_box.showerror("Error" , "Division by zero error")    
            else:    
                x = ((c1*b2) - (c2*b1))*num/5
                y = ((c2*a1) - (a2*c1))*num/5
                m_box.showinfo("Result" , f"x = {x} and y = {y}")

                with open(os.getcwd() + r"\History.txt" , "a") as f:
                    f.write(f"Equations:\n{a1}x + {b1}y = {c1},{a2}x + {b2}y ={c2}\nSolution - x = {x} , y = {y}\n")

    elif command == "":
        m_box.showerror("Error" , "Select any command")

def func11():
    pass
    entry_eqn1a.delete( 0 ,tk.END)
    entry_eqn1b.delete( 0 ,tk.END)
    entry_eqn1c.delete( 0 ,tk.END)
    entry_eqn2a.delete( 0 ,tk.END)
    entry_eqn2b.delete( 0 ,tk.END)
    entry_eqn2c.delete( 0 ,tk.END)

def func12():
    n_list = []
    m_box.showinfo("Speech" , "Make sure Your microphone is turned on and you are connected to internet")
    m_box.showinfo("Speech" , "Speak in format : First equation A is equal to 'Your number' ,B is equal to 'Your number' ,C is equal to 'Your number'\nSecond equation A is equal to 'Your number' ,B is equal to 'Your number' ,C is equal to 'Your number' ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        m_box.showinfo("Speech" , "Speak after pressing OK \nEvaluting the results may take some time")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:    
            m_box.showerror("Error" , "Could not recognize your voice")
        else:
            text = text.replace("to", "2")
            text = text.replace("minus " , "-")
            text = text.replace("- " , "-")
            print(text)
            for i in text.split(" "):
                try:
                    i = int(i)
                except ValueError:
                    pass    
                else:
                    n_list.append(i)
            try:        
                a1,b1,c1,a2,b2,c2 = tuple(n_list)
            except ValueError:
                m_box.showerror("Error" , "Invalid Speech")    
            else:    
                try:
                    num = 5/((a1*b2) - (a2*b1))
                except ZeroDivisionError:
                    m_box.showerror("Error" , "Division by zero error")    
                else:    
                    x = ((c1*b2) - (c2*b1))*num/5
                    y = ((c2*a1) - (a2*c1))*num/5
                    m_box.showinfo("Result" , f"x = {x} and y = {y}")

                    with open(os.getcwd() + r"\History.txt" , "a") as f:
                        f.write(f"Equations:\n{a1}x + {b1}y = {c1},{a2}x + {b2}y ={c2}\nSolution - x = {x} , y = {y}\n")


def func13(event = ""):
    win.destroy()            

def askopen():
    global result 
    result = filedialog.askdirectory(parent = win , initialdir = r"E:\Python Projects\Equation Solver" , title = "Select a Folder")
    try:
        shutil.move(os.getcwd() + r"\History.txt" , result + r"\History.txt")
        shutil.move(os.getcwd() + r"\Help.txt" , result + r"\Help.txt")
    except FileNotFoundError:
        pass  
    except PermissionError:
        m_box.showerror("Error" , "Permission Error") 
    else:
        try:
            os.chdir(result)
        except OSError:
            pass

# BINDINGS

win.bind("<Control_L><c>" ,func2)
win.bind("<Control_L><C>" ,func2)
win.bind("<Control_L><h>" , func3)
win.bind("<Control_L><H>" , func3)
win.bind("<Control_L><d>" , func4)
win.bind("<Control_L><D>" , func4)
win.bind("<Control_L><f>" , func7)
win.bind("<Control_L><F>" , func7)
win.bind("<Control_L><i>" , func8)
win.bind("<Control_L><I>" , func8)
win.bind("<Control_L><t>" , func9)
win.bind("<Control_L><T>" , func9)
win.bind("<Control_L><A>" , func5)
win.bind("<Control_L><a>" , func5)
win.bind("<Control_L><e>" , func13)
win.bind("<Control_L><E>" , func13)

# MAIN MENU 

main_menu = tk.Menu(win)

# FILE MENU 

file_menu = tk.Menu(main_menu , tearoff = 0)
main_menu.add_cascade(label = "File" , menu = file_menu)
file_menu.add_command(label = "Histroy location" , command = func1)
file_menu.add_command(label = "Change Histroy location" , command = askopen)
file_menu.add_command(label = "Exit" , command = func13 , accelerator = "Ctrl+E")

# EDIT MENU 

edit_menu = tk.Menu(main_menu , tearoff = 0)
main_menu.add_cascade(label = "Edit" , menu = edit_menu)
edit_menu.add_command(label = " Clear All" , command = func2 , accelerator = "Ctrl+C")
edit_menu.add_separator()
edit_menu.add_command(label = "Show History" , command = func3 , accelerator="Ctrl+H")
edit_menu.add_command(label = "Clear Histroy" , command = func4 , accelerator= "Ctrl+D") 

# THEME MENU 

theme_menu = tk.Menu(edit_menu , tearoff = 0)
edit_menu.add_cascade(label = 'Background Colour' , menu = theme_menu)
theme_menu.add_command(label = "Black" , command = func_black)
theme_menu.add_command(label = "Red" , command = func_red)
theme_menu.add_command(label = "Blue" , command = func_blue)
theme_menu.add_command(label = "Grey" , command = func_grey) 
theme_menu.add_command(label = "Default" , command = func_default)


# HELP MENU

help_menu = tk.Menu(main_menu , tearoff = 0)
main_menu.add_cascade(label = "Help" , menu = help_menu)
help_menu.add_command(label = "Help" , command = func5 , accelerator = "Ctrl+A" )

# FEEDBACK MENU

feedback_menu = tk.Menu(main_menu , tearoff = 0)
main_menu.add_cascade(label = "Feedback" , menu = feedback_menu)
feedback_menu.add_command(label = "Send Feedback" , command = func6)


# DEV MENU

dev_menu = tk.Menu(main_menu , tearoff = 0)
main_menu.add_cascade(label = "Developer" , menu = dev_menu)
dev_menu.add_command(label = "Facebook" , command = func7 , accelerator = "Ctrl+F" , image = face_icon , compound = tk.LEFT)
dev_menu.add_separator()
dev_menu.add_command(label = "Instagram" , command = func8, accelerator = "Ctrl+I" , image = insta_icon , compound = tk.LEFT)
dev_menu.add_separator()
dev_menu.add_command(label = "Twitter" , command = func9, accelerator = "Ctrl+T" , image = twitter_icon , compound = tk.LEFT)


# CONFIGURE 

win.config(menu = main_menu)

# NOTEBOOK

nb = ttk.Notebook(win)
page1 = tk.Frame()
page2= tk.Frame()
nb.add(page1 , text = "2 Equation 2 variable")
nb.add(page2 , text = "3 Equation 3 variable")
nb.pack(expand = True , fill = "both")

# LABELFRAME 

label_frame1 = tk.LabelFrame(page1 , text = "2 Equation 2 variable")
label_frame1.grid(row = 0 , column = 0 , padx = 80 , pady = 40)



# LABELS 

for i in range(0,36):
    label = "label" + str(i)
    label = ttk.Label(label_frame1 , text = " ")
    label.grid(row = 0 , column = i)

for j in range(0,19):
    label_new = "label_new" + str(j)
    label = ttk.Label(label_frame1 , text = "")
    label.grid(row = j , column = 0)


label_intro1 = ttk.Label(label_frame1 , text = "Input must be in this manner :    Ax + By = C" , foreground = "#000066")
label_intro1.grid(row = 0 , column = 0 , columnspan = 40 , sticky = tk.W)

label_exa = ttk.Label(label_frame1 , text = "EXAMPLE - " , foreground = "#D03928")
label_exa.grid(row = 2 , column = 0 , columnspan = 10 , sticky = tk.W)

label_exa1 = ttk.Label(label_frame1 , text = "For the equations :- " , foreground = "#000066")
label_exa1.grid(row = 3 , column = 0 , columnspan = 20 , sticky = tk.W)

label_exa2 = ttk.Label(label_frame1 , text = "2x + 3y = 12" , foreground = "#000066")
label_exa2.grid(row = 4 , column = 5 , columnspan = 12 , sticky = tk.W)

label_exa3 = ttk.Label(label_frame1 , text = "3x - 4y = 1" , foreground = "#000066")
label_exa3.grid(row = 5 , column = 5 , columnspan = 10 , sticky = tk.W )

label_exa4 = ttk.Label(label_frame1 , text = "You would enter - " , foreground = "#000066")
label_exa4.grid(row = 6 , column = 0 , columnspan = 16 , sticky = tk.W)

label_exa5 = ttk.Label(label_frame1 , text = "Equation 1 -   2   3   12" , foreground = "#000066")
label_exa5.grid(row = 7 , column = 2, columnspan = 17 , sticky = tk.W)

label_exa6 = ttk.Label(label_frame1 , text = "Equation 2 -   3   -4   1" , foreground = "#000066")
label_exa6.grid(row = 8 , column = 2 , columnspan = 18 , sticky = tk.W)

label_exa7 = ttk.Label(label_frame1 , text = "Click SOLVE for the answers :-" , foreground = "#000066")
label_exa7.grid(row = 10 , column = 0 , columnspan = 28 , sticky = tk.W)

label_exa8 = ttk.Label(label_frame1 , text = "x = 3" , foreground = "#000066")
label_exa8.grid(row = 11 , column = 7, columnspan = 5 , sticky = tk.W)

label_exa9 = ttk.Label(label_frame1 , text = "y = 2" , foreground = "#000066")
label_exa9.grid(row = 11 , column = 13 , columnspan = 5 , sticky = tk.W)

label_eqn1 = ttk.Label(label_frame1 , text = "Equation  1 - " , foreground = "#D03928")
label_eqn1.grid(row = 15 , column = 0 , columnspan = 14 , sticky = tk.W)

label_eqn1a = ttk.Label(label_frame1 , text = "A = ", foreground = "#000066")
label_eqn1a.grid(row = 15 , column = 12 , columnspan = 6 ,sticky = tk.W)

label_eqn1b = ttk.Label(label_frame1 , text = "B = ", foreground = "#000066")
label_eqn1b.grid(row = 15 , column = 18 ,columnspan = 6 , sticky = tk.W)

label_eqn1c = ttk.Label(label_frame1 , text = "C = ", foreground = "#000066")
label_eqn1c.grid(row = 15 , column = 24 , columnspan =6 , sticky = tk.W)

label_eqn2 = ttk.Label(label_frame1 , text = "Equation  2 - " , foreground = "#D03928")
label_eqn2.grid(row = 17, column = 0  , columnspan = 14 , sticky = tk.W)

label_eqn2a = ttk.Label(label_frame1 , text = "A = ", foreground = "#000066")
label_eqn2a.grid(row = 17 , column = 12 ,columnspan = 6 , sticky = tk.W)

label_eqn2a = ttk.Label(label_frame1 , text = "B = ", foreground = "#000066")
label_eqn2a.grid(row = 17 , column = 18 ,columnspan = 6 , sticky = tk.W)

label_eqn2a = ttk.Label(label_frame1 , text = "C = ", foreground = "#000066")
label_eqn2a.grid(row = 17 , column = 24 ,columnspan = 6 , sticky = tk.W)

label_radio = ttk.Label(label_frame1 , text = "Select Your Command : " , foreground = "#D03928")
label_radio.grid(row = 13 , column = 0 , columnspan = 21 ,sticky = tk.W)

# VARIABLES
 

# EQUATION 1

eqn1_a_var = tk.StringVar()
eqn1_b_var = tk.StringVar()
eqn1_c_var = tk.StringVar()

# EQUATION 2

eqn2_a_var = tk.StringVar()
eqn2_b_var = tk.StringVar()
eqn2_c_var = tk.StringVar()

# RADIOBUTTON 

radio_var = tk.StringVar()

# ENTRY 

entry_eqn1a = ttk.Entry(label_frame1 , width = 5 , textvariable = eqn1_a_var)
entry_eqn1a.grid(row = 15, column = 16)

entry_eqn1b = ttk.Entry(label_frame1 , width = 5, textvariable = eqn1_b_var)
entry_eqn1b.grid(row = 15 , column = 22)

entry_eqn1c = ttk.Entry(label_frame1 , width = 5, textvariable = eqn1_c_var)
entry_eqn1c.grid(row = 15 , column = 28)

entry_eqn2a = ttk.Entry(label_frame1 , width = 5 , textvariable = eqn2_a_var)
entry_eqn2a.grid(row = 17 ,column = 16)

entry_eqn2b = ttk.Entry(label_frame1 , width = 5, textvariable = eqn2_b_var)
entry_eqn2b.grid(row =17,column = 22)

entry_eqn2c = ttk.Entry(label_frame1 , width = 5, textvariable = eqn2_c_var)
entry_eqn2c.grid(row = 17, column = 28 )

# RADIOBUTTON

radio_text = ttk.Radiobutton(label_frame1 , text = "Text" , value = "Text" , variable = radio_var)
radio_text.grid(row = 13 , column = 17 , columnspan = 7)

radio_speech = ttk.Radiobutton(label_frame1 , text = "Speech" , value = "Speech" , variable = radio_var , command = func12)
radio_speech.grid(row = 13, column = 19 , columnspan = 18)

# SOLVE BUTTON  

solve_button = ttk.Button(page1 , text = "SOLVE" , width = 12 , command = func10)
solve_button.grid(row = 1 , column = 0)

# CLEAR BUTTON 

clear_button = ttk.Button(page1 , text = "RESET" , width = 12 , command = func11)
clear_button.grid(row = 2 , column = 0)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3 EQUATION 3 SOLVER

# FUNCTIONS 

def func14():
    n_list = []
    m_box.showinfo("Speech" , "Make sure Your microphone is turned on and you are connected to internet")
    m_box.showinfo("Speech" , "Speak in format : \nFirst equation A is \"Your number\" , B is \"Your number\" , C \"Your number\" , D \"Your number\"\nSecond Equation A is \"Your number\" , B is \"Your number\" , C is \"Your number\" , D is \"Your number\"\nThird Equation A is \"Your number\" , B is \"Your number\" , C is \"Your number\" , D is \"Your number\" ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        m_box.showinfo("Speech" , "Speak after pressing OK \nEvaluting the results may take some time")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:    
            m_box.showerror("Error" , "Could not recognize your voice")
        else:
            text = text.replace("to", "2")
            text = text.replace("minus " , "-")
            text = text.replace("- " , "-")
            print(text)
            for i in text.split(" "):
                try:
                    i = int(i)
                except ValueError:
                    pass    
                else:
                    n_list.append(i)
            try:        
                a1,b1,c1,d1,a2,b2,c2,d2,a3,b3,c3,d3 = tuple(n_list)
            except ValueError:
                m_box.showerror("Error" , "Invalid Speech") 
            else:
                try:
                    num = 5/((a1*b2*c3) - (a1*b3*c2) - (b1*a2*c3) + (b1*a3*c2) + (c1*a2*b3) - (c1*a3*b2))
                except ZeroDivisionError:
                    m_box.showerror("Error" , "Division by zero occured")    
                else:
                    x = (((d1*b2*c3) - (d1*b3*c2) - (b1*d2*c3) + (b1*d3*c2) + (c1*d2*b3) - (c1*d3*b2))*num)/5
                    y = (((a1*d2*c3) - (a1*d3*c2) - (d1*a2*c3) + (d1*a3*c2) + (c1*a2*d3) - (c1*a3*d2))*num)/5
                    z = (((a1*b2*d3) - (a1*b3*d2) - (b1*a2*d3) + (b1*a3*d2) + (d1*a2*b3) - (d1*a3*b2))*num)/5 

                    m_box.showinfo("Result" , f"x = {x}\ny = {y}\nz = {z}")
                    with open(os.getcwd() + r"\History.txt" , "a") as f:
                        f.write(f"Equations : \n{a1}x + {b1}y + {c1}z = {d1} , {a2}x + {b2}y + {c2}z = {d2} , {a3}x + {b3}y + {c3}z = {d3}\nSolution - x = {x} , y = {y} , z = {z}")                

    
def func15():
    command1 = radio_var1.get()
    a1= eqn3_a_var.get()
    b1 = eqn3_b_var.get()
    c1 = eqn3_c_var.get()
    d1 = eqn3_d_var.get()
    a2 = eqn4_a_var.get()
    b2 = eqn4_b_var.get()
    c2 = eqn4_c_var.get()
    d2 = eqn4_d_var.get()
    a3=  eqn5_a_var.get()
    b3 = eqn5_b_var.get()
    c3 = eqn5_c_var.get()
    d3 = eqn5_d_var.get() 
    if command1 == 'Text':
        try:
            if "." in a1:
                a1 = float(a1)
            else:
                a1 = int(a1)
            if "." in b1:
                b1= float(b1)
            else:
                b1 = int(b1)
            if "." in c1:
                c1 = float(c1)
            else:
                c1 = int(c1)
            if "." in d1:
                d1 = float(d1)
            else:
                d1 = int(d1)    
            if "." in a2:
                a2 = float(a2)
            else:
                a2 = int(a2)
            if "." in b2:
                b2 = float(b2)
            else:
                b2 = int(b2)
            if "." in c2:
                c2 = float(c2)
            else:
                c2 = int(c2)
            if "." in d2:
                d2 = float(d2)
            else:
                d2 = int(d2)    
            if "." in a3:
                a3 = float(a3)
            else:
                a3 = int(a3)
            if "." in b3:
                b3 = float(b3)
            else:
                b3 = int(b3)
            if "." in c3:
                c3 = float(c3)
            else:
                c3 = int(c3)
            if "." in d3:
                d3 = float(d3)
            else:
                d3 = int(d3)    
        except ValueError:
            m_box.showerror("Error" , "Enter data in integer only")    
        else:
            try:
                num = 5/((a1*b2*c3) - (a1*b3*c2) - (b1*a2*c3) + (b1*a3*c2) + (c1*a2*b3) - (c1*a3*b2))
            except ZeroDivisionError:
                m_box.showerror("Error" , "Division by zero occured")    
            else:
                x = (((d1*b2*c3) - (d1*b3*c2) - (b1*d2*c3) + (b1*d3*c2) + (c1*d2*b3) - (c1*d3*b2))*num)/5
                y = (((a1*d2*c3) - (a1*d3*c2) - (d1*a2*c3) + (d1*a3*c2) + (c1*a2*d3) - (c1*a3*d2))*num)/5
                z = (((a1*b2*d3) - (a1*b3*d2) - (b1*a2*d3) + (b1*a3*d2) + (d1*a2*b3) - (d1*a3*b2))*num)/5 

                m_box.showinfo("Result" , f"x = {x}\ny = {y}\nz = {z}")

                with open(os.getcwd() + r"\History.txt" , "a") as f:
                    f.write(f"Equations : \n{a1}x + {b1}y + {c1}z = {d1} , {a2}x + {b2}y + {c2}z = {d2} , {a3}x + {b3}y + {c3}z = {d3}\nSolution - x = {x} , y = {y} , z = {z}")

    elif command1 == "":
        m_box.showerror("Error" , "Select any command")

def func16():
    pass
    entry_eqn3a.delete( 0 ,tk.END)
    entry_eqn3b.delete( 0 ,tk.END)
    entry_eqn3c.delete( 0 ,tk.END)
    entry_eqn3d.delete( 0 ,tk.END)
    entry_eqn4a.delete( 0 ,tk.END)
    entry_eqn4b.delete( 0 ,tk.END)
    entry_eqn4c.delete( 0 ,tk.END)
    entry_eqn4d.delete( 0 ,tk.END)
    entry_eqn5a.delete( 0 ,tk.END)
    entry_eqn5b.delete( 0 ,tk.END)
    entry_eqn5c.delete( 0 ,tk.END)
    entry_eqn5d.delete( 0 ,tk.END)

           

# LABELFRAME 

label_frame2 = ttk.LabelFrame(page2 , text = "3 Equation 3 variable")
label_frame2.grid(row = 0 , column = 0 , padx = 80 , pady = 40)

for i in range(0,60):
    page_2label = "label1" + str(i)
    page_2label = ttk.Label(label_frame2 , text = " ")
    page_2label.grid(row = 0 , column = i)

for j in range(0,23):
    page_2label_new = "label_new1" + str(j)
    page_2label = ttk.Label(label_frame2 , text = " ")
    page_2label.grid(row = j , column = 0)



# LABELS 

label_intro3 = ttk.Label(label_frame2 , text = "Input must be in this manner :    Ax + By + Cz = D" , foreground = "#000066")
label_intro3.grid(row = 0 , column = 0 ,columnspan = 190 , sticky = tk.W)

label2_exa1 = ttk.Label(label_frame2 , text = "EXAMPLE - " , foreground = "#D03928")
label2_exa1.grid(row = 2, column = 0 , columnspan = 12, sticky  = tk.W)

label2_exa2 = ttk.Label(label_frame2 , text = "For the Equations : " , foreground = "#000066")
label2_exa2.grid(row = 3, column = 0 , columnspan = 18, sticky  = tk.W)

label2_exa3 = ttk.Label(label_frame2 , text = "2x + 3y + 4z = 119" , foreground = "#000066")
label2_exa3.grid(row = 4, column = 0 , columnspan = 18, sticky  = tk.W)

label2_exa4 = ttk.Label(label_frame2 , text = "5x - 6y + 7z = 80" , foreground = "#000066")
label2_exa4.grid(row = 5, column = 0 , columnspan = 18, sticky  = tk.W)

label2_exa5 = ttk.Label(label_frame2 , text = "8x + 9y + 10z = 353" , foreground = "#000066")
label2_exa5.grid(row = 6, column = 0 , columnspan = 18 , sticky  = tk.W)

label2_exa6 = ttk.Label(label_frame2 , text = "You would enter : " , foreground = "#000066")
label2_exa6.grid(row = 7, column = 0 , columnspan = 16, sticky  = tk.W)

label2_exa7 = ttk.Label(label_frame2 , text = "Equation 1 -   2    3    4    119" , foreground = "#000066")
label2_exa7.grid(row = 8, column = 6 , columnspan = 23, sticky  = tk.W)

label2_exa7 = ttk.Label(label_frame2 , text = "Equation 2 -   5   -6    7    80" , foreground = "#000066")
label2_exa7.grid(row = 9, column = 6 , columnspan = 24, sticky  = tk.W)

label2_exa7 = ttk.Label(label_frame2 , text = "Equation 3 -   8    9    10   353" , foreground = "#000066")
label2_exa7.grid(row = 10, column = 6 , columnspan = 24, sticky  = tk.W)

label2_exa8 = ttk.Label(label_frame2 , text = "Click SOLVE for the answers :" , foreground = "#000066")
label2_exa8.grid(row = 12, column = 0 , columnspan = 25, sticky  = tk.W)

label2_exa9 = ttk.Label(label_frame2 , text = "x = 12 " , foreground = "#000066")
label2_exa9.grid(row = 13, column = 8 , columnspan = 7, sticky  = tk.W)

label2_exa10 = ttk.Label(label_frame2 , text = "y = 13 " , foreground = "#000066")
label2_exa10.grid(row = 13, column = 15 , columnspan = 7, sticky  = tk.W)

label2_exa11 = ttk.Label(label_frame2 , text = "z = 14 " , foreground = "#000066")
label2_exa11.grid(row = 13, column = 22 , columnspan = 7, sticky  = tk.W)

label_eqn3 = ttk.Label(label_frame2 , text = "Equation  1 - " , foreground = "#D03928")
label_eqn3.grid(row = 17 , column = 0 , columnspan = 13 , sticky = tk.W)

label_eqn3a = ttk.Label(label_frame2 , text = "A = ", foreground = "#000066")
label_eqn3a.grid(row = 17 , column = 13 , columnspan = 6 , sticky = tk.W)

label_eqn3b = ttk.Label(label_frame2 , text = "B = ", foreground = "#000066")
label_eqn3b.grid(row = 17 , column = 23 , columnspan = 6 , sticky = tk.W)

label_eqn3c = ttk.Label(label_frame2 , text = "C = ", foreground = "#000066")
label_eqn3c.grid(row = 17 , column = 34 , columnspan = 6 , sticky = tk.W)

label_eqn3d = ttk.Label(label_frame2 , text = "D = ", foreground = "#000066")
label_eqn3d.grid(row = 17 , column = 45 , columnspan = 6 , sticky = tk.W)

label_eqn4 = ttk.Label(label_frame2 , text = "Equation  2 - " , foreground = "#D03928")
label_eqn4.grid(row = 19, column = 0 , columnspan = 12  , sticky = tk.W)

label_eqn4a = ttk.Label(label_frame2 , text = "A = ", foreground = "#000066")
label_eqn4a.grid(row =19  , column =13 , columnspan = 6 , sticky = tk.W)

label_eqn4b = ttk.Label(label_frame2 , text = "B = ", foreground = "#000066")
label_eqn4b.grid(row =19 , column =23  , columnspan = 6, sticky = tk.W)

label_eqn4c = ttk.Label(label_frame2 , text = "C = ", foreground = "#000066")
label_eqn4c.grid(row =19  , column = 34 , columnspan = 6, sticky = tk.W)

label_eqn4d = ttk.Label(label_frame2 , text = "D = ", foreground = "#000066")
label_eqn4d.grid(row =19 , column = 45 , columnspan = 6, sticky = tk.W)

label_eqn5 = ttk.Label(label_frame2 , text = "Equation  3 - " , foreground = "#D03928")
label_eqn5.grid(row = 21 , column = 0 , columnspan = 12 , sticky = tk.W)

label_eqn5a = ttk.Label(label_frame2 , text = "A = ", foreground = "#000066")
label_eqn5a.grid(row = 21 , column = 13 , columnspan = 6 , sticky = tk.W)

label_eqn5b = ttk.Label(label_frame2 , text = "B = ", foreground = "#000066")
label_eqn5b.grid(row = 21 , column = 23, columnspan = 6 , sticky = tk.W)

label_eqn5c = ttk.Label(label_frame2 , text = "C = ", foreground = "#000066")
label_eqn5c.grid(row = 21 , column = 34 , columnspan = 6 , sticky = tk.W)

label_eqn5d = ttk.Label(label_frame2 , text = "D = ", foreground = "#000066")
label_eqn5d.grid(row = 21 , column = 45 , columnspan = 6 , sticky = tk.W)

label_radio1 = ttk.Label(label_frame2 , text = "Select Your Command : " , foreground = "#D03928")
label_radio1.grid(row =15 , column = 0  , columnspan = 21 , sticky = tk.W)

# VARIABLES
 

# EQUATION 1

eqn3_a_var = tk.StringVar()
eqn3_b_var = tk.StringVar()
eqn3_c_var = tk.StringVar()
eqn3_d_var = tk.StringVar()

# EQUATION 2

eqn4_a_var = tk.StringVar()
eqn4_b_var = tk.StringVar()
eqn4_c_var = tk.StringVar()
eqn4_d_var = tk.StringVar()

# EQUATION 3

eqn5_a_var = tk.StringVar()
eqn5_b_var = tk.StringVar()
eqn5_c_var = tk.StringVar()
eqn5_d_var = tk.StringVar()


# RADIOBUTTON 

radio_var1 = tk.StringVar()

# ENTRY 

entry_eqn3a = ttk.Entry(label_frame2 , width = 5 , textvariable = eqn3_a_var)
entry_eqn3a.grid(row = 17 , column = 16 , columnspan = 6)

entry_eqn3b = ttk.Entry(label_frame2 , width = 5, textvariable = eqn3_b_var)
entry_eqn3b.grid(row = 17 , column = 26 , columnspan = 6 )

entry_eqn3c = ttk.Entry(label_frame2 , width = 5, textvariable = eqn3_c_var)
entry_eqn3c.grid(row = 17 , column = 38 , columnspan = 6)

entry_eqn3d = ttk.Entry(label_frame2 , width = 5, textvariable = eqn3_d_var)
entry_eqn3d.grid(row =17 , column = 50 , columnspan =6 )

entry_eqn4a = ttk.Entry(label_frame2 , width = 5 , textvariable = eqn4_a_var)
entry_eqn4a.grid(row = 19 , column = 16 , columnspan = 6)

entry_eqn4b = ttk.Entry(label_frame2 , width = 5, textvariable = eqn4_b_var)
entry_eqn4b.grid(row = 19 , column = 26 , columnspan = 6 )

entry_eqn4c = ttk.Entry(label_frame2 , width = 5, textvariable = eqn4_c_var)
entry_eqn4c.grid(row = 19 , column = 38 , columnspan = 6)

entry_eqn4d = ttk.Entry(label_frame2 , width = 5, textvariable = eqn4_d_var)
entry_eqn4d.grid(row = 19 , column = 50 , columnspan = 6)

entry_eqn5a = ttk.Entry(label_frame2 , width = 5 , textvariable = eqn5_a_var)
entry_eqn5a.grid(row = 21 , column = 16 , columnspan = 6)

entry_eqn5b = ttk.Entry(label_frame2 , width = 5, textvariable = eqn5_b_var)
entry_eqn5b.grid(row = 21, column = 26 , columnspan = 6)

entry_eqn5c = ttk.Entry(label_frame2 , width = 5, textvariable = eqn5_c_var)
entry_eqn5c.grid(row = 21, column = 38 , columnspan = 6)

entry_eqn5d = ttk.Entry(label_frame2 , width = 5, textvariable = eqn5_d_var)
entry_eqn5d.grid(row = 21, column = 50 , columnspan = 6)

# RADIOBUTTON

radio_text1 = ttk.Radiobutton(label_frame2 , text = "Text" , value = "Text" , variable = radio_var1)
radio_text1.grid(row = 15  , column = 22, columnspan = 7)

radio_speech1 = ttk.Radiobutton(label_frame2 , text = "Speech" , value = "Speech" , variable = radio_var1 , command = func14)
radio_speech1.grid(row = 15 , column =28 , columnspan = 18 )


# SOLVE BUTTON  

solve_button1 = ttk.Button(page2 , text = "SOLVE" , width = 12 , command = func15)
solve_button1.grid(row = 1 , column = 0)

# CLEAR BUTTON 

clear_button1 = ttk.Button(page2 , text = "RESET" , width = 12 , command = func16)
clear_button1.grid(row = 2 , column = 0)

win.mainloop()