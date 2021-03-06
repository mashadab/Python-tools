#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Feb 15, 2021 07:45:06 PM CST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import solve_lin_sys_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    solve_lin_sys_support.set_Tk_var()
    top = Made_by_Mohammad_Afzal_Shadab (root)
    solve_lin_sys_support.init(root, top)
    root.mainloop()

w = None
def create_Made_by_Mohammad_Afzal_Shadab(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Made_by_Mohammad_Afzal_Shadab(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    solve_lin_sys_support.set_Tk_var()
    top = Made_by_Mohammad_Afzal_Shadab (w)
    solve_lin_sys_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Made_by_Mohammad_Afzal_Shadab():
    global w
    w.destroy()
    w = None

class Made_by_Mohammad_Afzal_Shadab:
    def doRefresh(self):
        self.Var1.delete(0, 'end')
        self.Var2.delete(0, 'end')
        self.Var3.delete(0, 'end')
        self.Var4.delete(0, 'end')
        self.Var5.delete(0, 'end')

        self.M1.delete(0, 'end')
        self.M2.delete(0, 'end')
        self.M3.delete(0, 'end')
        self.M4.delete(0, 'end')
        self.M5.delete(0, 'end')

        self.L1.delete(0, 'end')
        self.L2.delete(0, 'end')
        self.L3.delete(0, 'end')
        self.L4.delete(0, 'end')
        self.L5.delete(0, 'end')

        self.T1.delete(0, 'end')
        self.T2.delete(0, 'end')
        self.T3.delete(0, 'end')
        self.T4.delete(0, 'end')
        self.T5.delete(0, 'end')
        return        
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1200x700+253+37")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Made by Mohammad Afzal Shadab")
        top.configure(background="#263D42")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.104, rely=0.1, relheight=0.793, relwidth=0.82)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.M1 = tk.Entry(self.Frame1)
        self.M1.place(relx=0.447, rely=0.342, height=40, relwidth=0.045)
        self.M1.configure(background="white")
        self.M1.configure(cursor="fleur")
        self.M1.configure(disabledforeground="#a3a3a3")
        self.M1.configure(font="TkFixedFont")
        self.M1.configure(foreground="#000000")
        self.M1.configure(highlightbackground="#d9d9d9")
        self.M1.configure(highlightcolor="black")
        self.M1.configure(insertbackground="black")
        self.M1.configure(selectbackground="blue")
        self.M1.configure(selectforeground="white")

        self.depvar1 = tk.Checkbutton(self.Frame1)
        self.depvar1.place(relx=1.118, rely=0.306, relheight=0.054
                , relwidth=0.036)
        self.depvar1.configure(activebackground="#ececec")
        self.depvar1.configure(activeforeground="#000000")
        self.depvar1.configure(background="#ffffff")
        self.depvar1.configure(disabledforeground="#a3a3a3")
        self.depvar1.configure(foreground="#000000")
        self.depvar1.configure(highlightbackground="#d9d9d9")
        self.depvar1.configure(highlightcolor="black")
        self.depvar1.configure(justify='left')
        self.depvar1.configure(variable=solve_lin_sys_support.che61)

        self.Message2 = tk.Message(self.Frame1)
        self.Message2.place(relx=0.681, rely=0.162, relheight=0.076
                , relwidth=0.14)
        self.Message2.configure(background="#ffffff")
        self.Message2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#ffffff")
        self.Message2.configure(highlightcolor="black")
        self.Message2.configure(justify='center')
        self.Message2.configure(text='''Dependent Variable''')
        self.Message2.configure(width=138)

        self.Message3 = tk.Message(self.Frame1)
        self.Message3.place(relx=0.112, rely=0.054, relheight=0.095
                , relwidth=0.764)
        self.Message3.configure(background="#ffffff")
        self.Message3.configure(font="-family {Segoe UI Symbol} -size 22 -weight bold")
        self.Message3.configure(foreground="#000000")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="black")
        self.Message3.configure(text='''Dimensional analysis using Pi theorem''')
        self.Message3.configure(width=756)

        self.L1 = tk.Entry(self.Frame1)
        self.L1.place(relx=0.52, rely=0.342, height=40, relwidth=0.045)
        self.L1.configure(background="white")
        self.L1.configure(disabledforeground="#a3a3a3")
        self.L1.configure(font="TkFixedFont")
        self.L1.configure(foreground="#000000")
        self.L1.configure(highlightbackground="#d9d9d9")
        self.L1.configure(highlightcolor="black")
        self.L1.configure(insertbackground="black")
        self.L1.configure(selectbackground="blue")
        self.L1.configure(selectforeground="white")

        self.T1 = tk.Entry(self.Frame1)
        self.T1.place(relx=0.589, rely=0.342, height=40, relwidth=0.045)
        self.T1.configure(background="white")
        self.T1.configure(disabledforeground="#a3a3a3")
        self.T1.configure(font="TkFixedFont")
        self.T1.configure(foreground="#000000")
        self.T1.configure(highlightbackground="#d9d9d9")
        self.T1.configure(highlightcolor="black")
        self.T1.configure(insertbackground="black")
        self.T1.configure(selectbackground="blue")
        self.T1.configure(selectforeground="white")

        self.Message2_1 = tk.Message(self.Frame1)
        self.Message2_1.place(relx=0.091, rely=0.162, relheight=0.076
                , relwidth=0.127)
        self.Message2_1.configure(background="#ffffff")
        self.Message2_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message2_1.configure(foreground="#000000")
        self.Message2_1.configure(highlightbackground="#ffffff")
        self.Message2_1.configure(highlightcolor="black")
        self.Message2_1.configure(justify='center')
        self.Message2_1.configure(text='''Variable Name''')
        self.Message2_1.configure(width=127)

        self.Message2_1_1 = tk.Message(self.Frame1)
        self.Message2_1_1.place(relx=0.264, rely=0.162, relheight=0.076
                , relwidth=0.129)
        self.Message2_1_1.configure(background="#ffffff")
        self.Message2_1_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message2_1_1.configure(foreground="#000000")
        self.Message2_1_1.configure(highlightbackground="#ffffff")
        self.Message2_1_1.configure(highlightcolor="black")
        self.Message2_1_1.configure(justify='center')
        self.Message2_1_1.configure(text='''Symbols''')
        self.Message2_1_1.configure(width=127)

        self.Message2_1_1_1 = tk.Message(self.Frame1)
        self.Message2_1_1_1.place(relx=0.478, rely=0.162, relheight=0.076
                , relwidth=0.129)
        self.Message2_1_1_1.configure(background="#ffffff")
        self.Message2_1_1_1.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message2_1_1_1.configure(foreground="#000000")
        self.Message2_1_1_1.configure(highlightbackground="#ffffff")
        self.Message2_1_1_1.configure(highlightcolor="black")
        self.Message2_1_1_1.configure(justify='center')
        self.Message2_1_1_1.configure(text='''Dimensions''')
        self.Message2_1_1_1.configure(width=127)

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.056, rely=0.241,  relwidth=0.912)

        self.Var1 = tk.Entry(self.Frame1)
        self.Var1.place(relx=0.059, rely=0.341, height=40, relwidth=0.177)
        self.Var1.configure(background="white")
        self.Var1.configure(disabledforeground="#a3a3a3")
        self.Var1.configure(font="TkFixedFont")
        self.Var1.configure(foreground="#000000")
        self.Var1.configure(highlightbackground="#d9d9d9")
        self.Var1.configure(highlightcolor="black")
        self.Var1.configure(insertbackground="black")
        self.Var1.configure(selectbackground="blue")
        self.Var1.configure(selectforeground="white")

        self.Sym1 = tk.Entry(self.Frame1)
        self.Sym1.place(relx=0.295, rely=0.342, height=40, relwidth=0.075)
        self.Sym1.configure(background="white")
        self.Sym1.configure(disabledforeground="#a3a3a3")
        self.Sym1.configure(font="TkFixedFont")
        self.Sym1.configure(foreground="#000000")
        self.Sym1.configure(highlightbackground="#d9d9d9")
        self.Sym1.configure(highlightcolor="black")
        self.Sym1.configure(insertbackground="black")
        self.Sym1.configure(selectbackground="blue")
        self.Sym1.configure(selectforeground="white")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.864, rely=0.919, height=24, width=100)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add another row''')

        self.Message1 = tk.Message(self.Frame1)
        self.Message1.place(relx=0.437, rely=0.27, relheight=0.041
                , relwidth=0.061)
        self.Message1.configure(background="#ffffff")
        self.Message1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''M''')
        self.Message1.configure(width=60)

        self.Message1_1 = tk.Message(self.Frame1)
        self.Message1_1.place(relx=0.508, rely=0.27, relheight=0.041
                , relwidth=0.061)
        self.Message1_1.configure(background="#ffffff")
        self.Message1_1.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Message1_1.configure(foreground="#000000")
        self.Message1_1.configure(highlightbackground="#d9d9d9")
        self.Message1_1.configure(highlightcolor="black")
        self.Message1_1.configure(text='''L''')
        self.Message1_1.configure(width=60)

        self.Message1_2 = tk.Message(self.Frame1)
        self.Message1_2.place(relx=0.579, rely=0.27, relheight=0.041
                , relwidth=0.061)
        self.Message1_2.configure(background="#ffffff")
        self.Message1_2.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Message1_2.configure(foreground="#000000")
        self.Message1_2.configure(highlightbackground="#d9d9d9")
        self.Message1_2.configure(highlightcolor="black")
        self.Message1_2.configure(text='''T''')
        self.Message1_2.configure(width=60)

        self.Var2 = tk.Entry(self.Frame1)
        self.Var2.place(relx=0.062, rely=0.458, height=40, relwidth=0.177)
        self.Var2.configure(background="white")
        self.Var2.configure(disabledforeground="#a3a3a3")
        self.Var2.configure(font="TkFixedFont")
        self.Var2.configure(foreground="#000000")
        self.Var2.configure(highlightbackground="#d9d9d9")
        self.Var2.configure(highlightcolor="black")
        self.Var2.configure(insertbackground="black")
        self.Var2.configure(selectbackground="blue")
        self.Var2.configure(selectforeground="white")

        self.Sym2 = tk.Entry(self.Frame1)
        self.Sym2.place(relx=0.295, rely=0.45, height=40, relwidth=0.075)
        self.Sym2.configure(background="white")
        self.Sym2.configure(disabledforeground="#a3a3a3")
        self.Sym2.configure(font="TkFixedFont")
        self.Sym2.configure(foreground="#000000")
        self.Sym2.configure(highlightbackground="#d9d9d9")
        self.Sym2.configure(highlightcolor="black")
        self.Sym2.configure(insertbackground="black")
        self.Sym2.configure(selectbackground="blue")
        self.Sym2.configure(selectforeground="white")

        self.M2 = tk.Entry(self.Frame1)
        self.M2.place(relx=0.447, rely=0.45, height=40, relwidth=0.045)
        self.M2.configure(background="white")
        self.M2.configure(disabledforeground="#a3a3a3")
        self.M2.configure(font="TkFixedFont")
        self.M2.configure(foreground="#000000")
        self.M2.configure(highlightbackground="#d9d9d9")
        self.M2.configure(highlightcolor="black")
        self.M2.configure(insertbackground="black")
        self.M2.configure(selectbackground="blue")
        self.M2.configure(selectforeground="white")

        self.L2 = tk.Entry(self.Frame1)
        self.L2.place(relx=0.518, rely=0.45, height=40, relwidth=0.045)
        self.L2.configure(background="white")
        self.L2.configure(disabledforeground="#a3a3a3")
        self.L2.configure(font="TkFixedFont")
        self.L2.configure(foreground="#000000")
        self.L2.configure(highlightbackground="#d9d9d9")
        self.L2.configure(highlightcolor="black")
        self.L2.configure(insertbackground="black")
        self.L2.configure(selectbackground="blue")
        self.L2.configure(selectforeground="white")

        self.T2 = tk.Entry(self.Frame1)
        self.T2.place(relx=0.589, rely=0.45, height=40, relwidth=0.045)
        self.T2.configure(background="white")
        self.T2.configure(disabledforeground="#a3a3a3")
        self.T2.configure(font="TkFixedFont")
        self.T2.configure(foreground="#000000")
        self.T2.configure(highlightbackground="#d9d9d9")
        self.T2.configure(highlightcolor="black")
        self.T2.configure(insertbackground="black")
        self.T2.configure(selectbackground="blue")
        self.T2.configure(selectforeground="white")

        self.Var3 = tk.Entry(self.Frame1)
        self.Var3.place(relx=0.061, rely=0.577, height=40, relwidth=0.177)
        self.Var3.configure(background="white")
        self.Var3.configure(disabledforeground="#a3a3a3")
        self.Var3.configure(font="TkFixedFont")
        self.Var3.configure(foreground="#000000")
        self.Var3.configure(highlightbackground="#d9d9d9")
        self.Var3.configure(highlightcolor="black")
        self.Var3.configure(insertbackground="black")
        self.Var3.configure(selectbackground="blue")
        self.Var3.configure(selectforeground="white")

        self.Var4 = tk.Entry(self.Frame1)
        self.Var4.place(relx=0.061, rely=0.685, height=40, relwidth=0.177)
        self.Var4.configure(background="white")
        self.Var4.configure(disabledforeground="#a3a3a3")
        self.Var4.configure(font="TkFixedFont")
        self.Var4.configure(foreground="#000000")
        self.Var4.configure(highlightbackground="#d9d9d9")
        self.Var4.configure(highlightcolor="black")
        self.Var4.configure(insertbackground="black")
        self.Var4.configure(selectbackground="blue")
        self.Var4.configure(selectforeground="white")

        self.Var5 = tk.Entry(self.Frame1)
        self.Var5.place(relx=0.061, rely=0.793, height=40, relwidth=0.177)
        self.Var5.configure(background="white")
        self.Var5.configure(disabledforeground="#a3a3a3")
        self.Var5.configure(font="TkFixedFont")
        self.Var5.configure(foreground="#000000")
        self.Var5.configure(highlightbackground="#d9d9d9")
        self.Var5.configure(highlightcolor="black")
        self.Var5.configure(insertbackground="black")
        self.Var5.configure(selectbackground="blue")
        self.Var5.configure(selectforeground="white")

        self.Sym3 = tk.Entry(self.Frame1)
        self.Sym3.place(relx=0.295, rely=0.577, height=40, relwidth=0.075)
        self.Sym3.configure(background="white")
        self.Sym3.configure(disabledforeground="#a3a3a3")
        self.Sym3.configure(font="TkFixedFont")
        self.Sym3.configure(foreground="#000000")
        self.Sym3.configure(highlightbackground="#d9d9d9")
        self.Sym3.configure(highlightcolor="black")
        self.Sym3.configure(insertbackground="black")
        self.Sym3.configure(selectbackground="blue")
        self.Sym3.configure(selectforeground="white")

        self.Sym4 = tk.Entry(self.Frame1)
        self.Sym4.place(relx=0.295, rely=0.685, height=40, relwidth=0.075)
        self.Sym4.configure(background="white")
        self.Sym4.configure(disabledforeground="#a3a3a3")
        self.Sym4.configure(font="TkFixedFont")
        self.Sym4.configure(foreground="#000000")
        self.Sym4.configure(highlightbackground="#d9d9d9")
        self.Sym4.configure(highlightcolor="black")
        self.Sym4.configure(insertbackground="black")
        self.Sym4.configure(selectbackground="blue")
        self.Sym4.configure(selectforeground="white")

        self.Sym5 = tk.Entry(self.Frame1)
        self.Sym5.place(relx=0.294, rely=0.796, height=40, relwidth=0.075)
        self.Sym5.configure(background="white")
        self.Sym5.configure(disabledforeground="#a3a3a3")
        self.Sym5.configure(font="TkFixedFont")
        self.Sym5.configure(foreground="#000000")
        self.Sym5.configure(highlightbackground="#d9d9d9")
        self.Sym5.configure(highlightcolor="black")
        self.Sym5.configure(insertbackground="black")
        self.Sym5.configure(selectbackground="blue")
        self.Sym5.configure(selectforeground="white")

        self.M3 = tk.Entry(self.Frame1)
        self.M3.place(relx=0.448, rely=0.571, height=40, relwidth=0.045)
        self.M3.configure(background="white")
        self.M3.configure(disabledforeground="#a3a3a3")
        self.M3.configure(font="TkFixedFont")
        self.M3.configure(foreground="#000000")
        self.M3.configure(highlightbackground="#d9d9d9")
        self.M3.configure(highlightcolor="black")
        self.M3.configure(insertbackground="black")
        self.M3.configure(selectbackground="blue")
        self.M3.configure(selectforeground="white")

        self.M4 = tk.Entry(self.Frame1)
        self.M4.place(relx=0.447, rely=0.679, height=40, relwidth=0.045)
        self.M4.configure(background="white")
        self.M4.configure(disabledforeground="#a3a3a3")
        self.M4.configure(font="TkFixedFont")
        self.M4.configure(foreground="#000000")
        self.M4.configure(highlightbackground="#d9d9d9")
        self.M4.configure(highlightcolor="black")
        self.M4.configure(insertbackground="black")
        self.M4.configure(selectbackground="blue")
        self.M4.configure(selectforeground="white")

        self.M5 = tk.Entry(self.Frame1)
        self.M5.place(relx=0.447, rely=0.793, height=40, relwidth=0.045)
        self.M5.configure(background="white")
        self.M5.configure(disabledforeground="#a3a3a3")
        self.M5.configure(font="TkFixedFont")
        self.M5.configure(foreground="#000000")
        self.M5.configure(highlightbackground="#d9d9d9")
        self.M5.configure(highlightcolor="black")
        self.M5.configure(insertbackground="black")
        self.M5.configure(selectbackground="blue")
        self.M5.configure(selectforeground="white")

        self.L3 = tk.Entry(self.Frame1)
        self.L3.place(relx=0.521, rely=0.568, height=40, relwidth=0.045)
        self.L3.configure(background="white")
        self.L3.configure(disabledforeground="#a3a3a3")
        self.L3.configure(font="TkFixedFont")
        self.L3.configure(foreground="#000000")
        self.L3.configure(highlightbackground="#d9d9d9")
        self.L3.configure(highlightcolor="black")
        self.L3.configure(insertbackground="black")
        self.L3.configure(selectbackground="blue")
        self.L3.configure(selectforeground="white")

        self.L4 = tk.Entry(self.Frame1)
        self.L4.place(relx=0.521, rely=0.677, height=40, relwidth=0.045)
        self.L4.configure(background="white")
        self.L4.configure(disabledforeground="#a3a3a3")
        self.L4.configure(font="TkFixedFont")
        self.L4.configure(foreground="#000000")
        self.L4.configure(highlightbackground="#d9d9d9")
        self.L4.configure(highlightcolor="black")
        self.L4.configure(insertbackground="black")
        self.L4.configure(selectbackground="blue")
        self.L4.configure(selectforeground="white")

        self.L5 = tk.Entry(self.Frame1)
        self.L5.place(relx=0.518, rely=0.793, height=40, relwidth=0.045)
        self.L5.configure(background="white")
        self.L5.configure(disabledforeground="#a3a3a3")
        self.L5.configure(font="TkFixedFont")
        self.L5.configure(foreground="#000000")
        self.L5.configure(highlightbackground="#d9d9d9")
        self.L5.configure(highlightcolor="black")
        self.L5.configure(insertbackground="black")
        self.L5.configure(selectbackground="blue")
        self.L5.configure(selectforeground="white")

        self.T3 = tk.Entry(self.Frame1)
        self.T3.place(relx=0.592, rely=0.569, height=40, relwidth=0.045)
        self.T3.configure(background="white")
        self.T3.configure(disabledforeground="#a3a3a3")
        self.T3.configure(font="TkFixedFont")
        self.T3.configure(foreground="#000000")
        self.T3.configure(highlightbackground="#d9d9d9")
        self.T3.configure(highlightcolor="black")
        self.T3.configure(insertbackground="black")
        self.T3.configure(selectbackground="blue")
        self.T3.configure(selectforeground="white")

        self.T4 = tk.Entry(self.Frame1)
        self.T4.place(relx=0.593, rely=0.681, height=40, relwidth=0.045)
        self.T4.configure(background="white")
        self.T4.configure(disabledforeground="#a3a3a3")
        self.T4.configure(font="TkFixedFont")
        self.T4.configure(foreground="#000000")
        self.T4.configure(highlightbackground="#d9d9d9")
        self.T4.configure(highlightcolor="black")
        self.T4.configure(insertbackground="black")
        self.T4.configure(selectbackground="blue")
        self.T4.configure(selectforeground="white")

        self.T5 = tk.Entry(self.Frame1)
        self.T5.place(relx=0.596, rely=0.793, height=40, relwidth=0.045)
        self.T5.configure(background="white")
        self.T5.configure(disabledforeground="#a3a3a3")
        self.T5.configure(font="TkFixedFont")
        self.T5.configure(foreground="#000000")
        self.T5.configure(highlightbackground="#d9d9d9")
        self.T5.configure(highlightcolor="black")
        self.T5.configure(insertbackground="black")
        self.T5.configure(selectbackground="blue")
        self.T5.configure(selectforeground="white")

        self.depvar2 = tk.Checkbutton(self.Frame1)
        self.depvar2.place(relx=0.731, rely=0.458, relheight=0.054
                , relwidth=0.038)
        self.depvar2.configure(activebackground="#ececec")
        self.depvar2.configure(activeforeground="#000000")
        self.depvar2.configure(background="#ffffff")
        self.depvar2.configure(disabledforeground="#a3a3a3")
        self.depvar2.configure(foreground="#000000")
        self.depvar2.configure(highlightbackground="#d9d9d9")
        self.depvar2.configure(highlightcolor="black")
        self.depvar2.configure(justify='left')
        self.depvar2.configure(variable=solve_lin_sys_support.che62)

        self.depvar3 = tk.Checkbutton(self.Frame1)
        self.depvar3.place(relx=0.732, rely=0.577, relheight=0.054
                , relwidth=0.037)
        self.depvar3.configure(activebackground="#ececec")
        self.depvar3.configure(activeforeground="#000000")
        self.depvar3.configure(background="#ffffff")
        self.depvar3.configure(disabledforeground="#a3a3a3")
        self.depvar3.configure(foreground="#000000")
        self.depvar3.configure(highlightbackground="#d9d9d9")
        self.depvar3.configure(highlightcolor="black")
        self.depvar3.configure(justify='left')
        self.depvar3.configure(variable=solve_lin_sys_support.che63)

        self.depvar4 = tk.Checkbutton(self.Frame1)
        self.depvar4.place(relx=0.732, rely=0.685, relheight=0.054
                , relwidth=0.037)
        self.depvar4.configure(activebackground="#ececec")
        self.depvar4.configure(activeforeground="#000000")
        self.depvar4.configure(background="#ffffff")
        self.depvar4.configure(disabledforeground="#a3a3a3")
        self.depvar4.configure(foreground="#000000")
        self.depvar4.configure(highlightbackground="#d9d9d9")
        self.depvar4.configure(highlightcolor="black")
        self.depvar4.configure(justify='left')
        self.depvar4.configure(variable=solve_lin_sys_support.che64)

        self.depvar5 = tk.Checkbutton(self.Frame1)
        self.depvar5.place(relx=0.732, rely=0.793, relheight=0.054
                , relwidth=0.037)
        self.depvar5.configure(activebackground="#ececec")
        self.depvar5.configure(activeforeground="#000000")
        self.depvar5.configure(background="#ffffff")
        self.depvar5.configure(disabledforeground="#a3a3a3")
        self.depvar5.configure(foreground="#000000")
        self.depvar5.configure(highlightbackground="#d9d9d9")
        self.depvar5.configure(highlightcolor="black")
        self.depvar5.configure(justify='left')
        self.depvar5.configure(variable=solve_lin_sys_support.che65)

        self.Message2_2 = tk.Message(self.Frame1)
        self.Message2_2.place(relx=0.823, rely=0.162, relheight=0.076
                , relwidth=0.14)
        self.Message2_2.configure(background="#ffffff")
        self.Message2_2.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Message2_2.configure(foreground="#000000")
        self.Message2_2.configure(highlightbackground="#ffffff")
        self.Message2_2.configure(highlightcolor="black")
        self.Message2_2.configure(justify='center')
        self.Message2_2.configure(text='''Repeating Variables''')
        self.Message2_2.configure(width=138)

        self.repvar1 = tk.Checkbutton(self.Frame1)
        self.repvar1.place(relx=0.884, rely=0.335, relheight=0.054
                , relwidth=0.036)
        self.repvar1.configure(activebackground="#ececec")
        self.repvar1.configure(activeforeground="#000000")
        self.repvar1.configure(background="#ffffff")
        self.repvar1.configure(disabledforeground="#a3a3a3")
        self.repvar1.configure(foreground="#000000")
        self.repvar1.configure(highlightbackground="#d9d9d9")
        self.repvar1.configure(highlightcolor="black")
        self.repvar1.configure(justify='left')
        self.repvar1.configure(variable=solve_lin_sys_support.che66)

        self.repvar2 = tk.Checkbutton(self.Frame1)
        self.repvar2.place(relx=0.884, rely=0.45, relheight=0.054
                , relwidth=0.036)
        self.repvar2.configure(activebackground="#ececec")
        self.repvar2.configure(activeforeground="#000000")
        self.repvar2.configure(background="#ffffff")
        self.repvar2.configure(disabledforeground="#a3a3a3")
        self.repvar2.configure(foreground="#000000")
        self.repvar2.configure(highlightbackground="#d9d9d9")
        self.repvar2.configure(highlightcolor="black")
        self.repvar2.configure(justify='left')
        self.repvar2.configure(variable=solve_lin_sys_support.che67)

        self.repvar3 = tk.Checkbutton(self.Frame1)
        self.repvar3.place(relx=0.884, rely=0.577, relheight=0.054
                , relwidth=0.036)
        self.repvar3.configure(activebackground="#ececec")
        self.repvar3.configure(activeforeground="#000000")
        self.repvar3.configure(background="#ffffff")
        self.repvar3.configure(disabledforeground="#a3a3a3")
        self.repvar3.configure(foreground="#000000")
        self.repvar3.configure(highlightbackground="#d9d9d9")
        self.repvar3.configure(highlightcolor="black")
        self.repvar3.configure(justify='left')
        self.repvar3.configure(variable=solve_lin_sys_support.che68)

        self.repvar4 = tk.Checkbutton(self.Frame1)
        self.repvar4.place(relx=0.884, rely=0.685, relheight=0.054
                , relwidth=0.036)
        self.repvar4.configure(activebackground="#ececec")
        self.repvar4.configure(activeforeground="#000000")
        self.repvar4.configure(background="#ffffff")
        self.repvar4.configure(disabledforeground="#a3a3a3")
        self.repvar4.configure(foreground="#000000")
        self.repvar4.configure(highlightbackground="#d9d9d9")
        self.repvar4.configure(highlightcolor="black")
        self.repvar4.configure(justify='left')
        self.repvar4.configure(variable=solve_lin_sys_support.che69)

        self.repvar5 = tk.Checkbutton(self.Frame1)
        self.repvar5.place(relx=0.884, rely=0.793, relheight=0.054
                , relwidth=0.036)
        self.repvar5.configure(activebackground="#ececec")
        self.repvar5.configure(activeforeground="#000000")
        self.repvar5.configure(background="#ffffff")
        self.repvar5.configure(disabledforeground="#a3a3a3")
        self.repvar5.configure(foreground="#000000")
        self.repvar5.configure(highlightbackground="#d9d9d9")
        self.repvar5.configure(highlightcolor="black")
        self.repvar5.configure(justify='left')
        self.repvar5.configure(variable=solve_lin_sys_support.che70)

        self.Button1_1 = tk.Button(self.Frame1)
        self.Button1_1.place(relx=0.582, rely=1.178, height=24, width=100)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Add another row''')

        self.Checkbutton1 = tk.Checkbutton(self.Frame1)
        self.Checkbutton1.place(relx=0.718, rely=0.346, relheight=0.047
                , relwidth=0.064)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#ffffff")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(variable=solve_lin_sys_support.che71)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.6, rely=0.914, height=50, width=100)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 14 -weight bold -slant italic")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Calculate!''')
        
        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.4, rely=0.914, height=50, width=100)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 14 -weight bold -slant italic")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Refresh''', command=self.doRefresh)        


if __name__ == '__main__':
    vp_start_gui()





