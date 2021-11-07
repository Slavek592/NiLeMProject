#!/usr/bin/python3
import os
from . import Runner
from tkinter import *
from . import GraphicalDatabases


def nilesh(superior):
    def nilesh_window():
        def walker(location):
            comment.configure(text="")
            back_button.configure(command=lambda action=Runner.get_outer_path(location, 2): walker(action))
            for widget in frame.winfo_children():
                widget.destroy()
            directories = [f for f in os.listdir(location) if not os.path.isfile(os.path.join(location, f))]
            i = 0
            for directory in directories:
                Button(frame, text=directory + "/",
                       command=lambda action=location + directory + "/": walker(action)).grid(row=i, column=0)
                i += 1
            files = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
            i = 0
            for file in files:
                Button(frame, text=file,
                       command=lambda action=location + file: interactive_run(action)).grid(row=i, column=1)
                i += 1
            comment.configure(text="Entered into")

        def interactive_run(file_name):
            comment.configure(text="")
            if Runner.run_from_file(file_name):
                comment.configure(text="Done")
            else:
                comment.configure(text="Error")

        def turn_off():
            way.append(["exit"])
            root.destroy()

        def to_databases():
            way.append(["databases"])
            root.destroy()

        root = Tk()
        root.title("NiLeSh")
        back_button = Button(root, text="../", command=None)
        back_button.pack()
        frame = Frame(root)
        frame.pack()
        exit_buttons = Frame(root)
        turn_off_button = Button(exit_buttons, text="Turn off", command=turn_off)
        turn_off_button.grid(row=0, column=0)
        databases_button = Button(exit_buttons, text="To databases", command=to_databases)
        databases_button.grid(row=0, column=1)
        exit_buttons.pack()
        comment = Label(root, text="")
        comment.pack()
        walker("NileshScripts/")
        comment.configure(text="Welcome, user!")
        root.mainloop()

    way = [["nilesh"]]
    length = 0
    while True:
        if len(way) == length:
            return False
        length = len(way)
        if way[len(way) - 1][0] == "nilesh":
            nilesh_window()
        elif way[len(way) - 1][0] == "databases":
            if superior != "databases":
                if GraphicalDatabases.databases("nilesh"):
                    way.append(["nilesh"])
            else:
                return True
        elif way[len(way) - 1][0] == "exit":
            return False
