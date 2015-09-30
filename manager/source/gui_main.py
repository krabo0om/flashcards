#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.5
# In conjunction with Tcl version 8.6
#    Jul 25, 2015 04:14:43 PM
from source import gui_support

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = 0
except ImportError:
    import tkinter.ttk as ttk

    py3 = 1


def vp_start_gui(api):
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('Flashcards_Manager')
    geom = "545x435+839+164"
    root.geometry(geom)
    gui_support.set_Tk_var()
    w = Flashcards_Manager(root)
    gui_support.init(root, w, arg=api)
    root.mainloop()


w = None


def create_Flashcards_Manager(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    w.title('Flashcards_Manager')
    geom = "545x435+839+164"
    w.geometry(geom)
    gui_support.set_Tk_var()
    w_win = Flashcards_Manager(w)
    gui_support.init(w, w_win, param)
    return w_win


def destroy_Flashcards_Manager():
    global w
    w.destroy()
    w = None


def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return "break"


class Flashcards_Manager:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d8d8d8'  # Closest X11 color: 'gray85'
        _ana1color = '#d8d8d8'  # Closest X11 color: 'gray85'
        _ana2color = '#d8d8d8'  # Closest X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size -12 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans Mono} -size -12 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"

        self.list_set = Listbox(master)
        self.list_set.place(relx=0.02, rely=0.07, relheight=0.84, relwidth=0.3)
        self.list_set.configure(background="white")
        self.list_set.configure(font=font11)
        self.list_set.configure(width=164)
        self.list_set.configure(listvariable=gui_support.list_set_var)
        self.list_set.bind('<<ListboxSelect>>', lambda e: gui_support.list_sel_update(e))

        self.Label1 = Label(master)
        self.Label1.place(relx=0.02, rely=0.02, height=19, width=87)
        self.Label1.configure(text='''Available Sets''')

        self.Label2 = Label(master)
        self.Label2.place(relx=0.35, rely=0.02, height=19, width=80)
        self.Label2.configure(text='''Selected Set''')

        self.Label3 = Label(master)
        self.Label3.place(relx=0.35, rely=0.14, height=19, width=57)
        self.Label3.configure(text='''Question''')

        self.Label4 = Label(master)
        self.Label4.place(relx=0.35, rely=0.87, height=19, width=29)
        self.Label4.configure(text='''Hint''')

        self.edit_set = Entry(master)
        self.edit_set.place(relx=0.35, rely=0.07, relheight=0.05, relwidth=0.27)
        self.edit_set.configure(background="white")
        self.edit_set.configure(font=font11)
        self.edit_set.configure(textvariable=gui_support.edit_set_var)

        self.txt_question = Text(master)
        self.txt_question.place(relx=0.35, rely=0.18, relheight=0.31, relwidth=0.63)
        self.txt_question.configure(background="white")
        self.txt_question.configure(font=font10)
        self.txt_question.configure(selectbackground="#c4c4c4")
        self.txt_question.configure(width=346)
        self.txt_question.configure(wrap=WORD)
        self.txt_question.bind("<Tab>", focus_next_window)

        self.txt_answer = Text(master)
        self.txt_answer.place(relx=0.35, rely=0.55, relheight=0.31, relwidth=0.63)
        self.txt_answer.configure(background="white")
        self.txt_answer.configure(font=font10)
        self.txt_answer.configure(selectbackground="#c4c4c4")
        self.txt_answer.configure(width=346)
        self.txt_answer.configure(wrap=WORD)
        self.txt_answer.bind("<Tab>", focus_next_window)

        self.edit_hint = Entry(master)
        self.edit_hint.place(relx=0.35, rely=0.92, relheight=0.05, relwidth=0.27)
        self.edit_hint.configure(background="white")
        self.edit_hint.configure(font=font11)
        self.edit_hint.configure(textvariable=gui_support.edit_hint_var)

        self.Label5 = Label(master)
        self.Label5.place(relx=0.35, rely=0.5, height=19, width=48)
        self.Label5.configure(text='''Answer''')

        self.btn_commit = Button(master)
        self.btn_commit.place(relx=0.02, rely=0.92, height=27, width=167)
        self.btn_commit.configure(activebackground="#d9d9d9")
        self.btn_commit.configure(text='''commit''')
        self.btn_commit.configure(width=167)
        self.btn_commit.bind('<Button-1>',lambda e:gui_support.commit(e))
        self.btn_commit.bind('<Enter>', lambda e: gui_support.commit(e))
