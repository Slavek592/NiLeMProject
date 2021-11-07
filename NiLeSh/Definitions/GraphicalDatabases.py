#!/usr/bin/python3
from tkinter import *
from . import Printing
from . import GraphicalNiLeSh


def databases(superior):
    def database_window():
        def turn_off():
            way.append(["exit"])
            root.destroy()

        def to_nilesh():
            way.append(["nilesh"])
            root.destroy()

        root = Tk()
        root.title("NiLeSh-databases")
        buttons = Frame(root)
        Label(buttons, text="Delete").grid(row=0, column=0)
        Label(buttons, text="Create").grid(row=0, column=1)
        languages = ["english", "czech", "russian", "german", "french", "spanish"]
        delete_buttons = []
        create_buttons = []
        for i in range(len(languages)):
            delete_buttons.append(Button(buttons, text=languages[i].capitalize(),
                                         command=lambda action=languages[i].capitalize():
                                         Printing.delete_database(action)))
            delete_buttons[i].grid(row=i+1, column=0)
            create_buttons.append(Button(buttons, text=languages[i].capitalize(),
                                         command=lambda action=languages[i].capitalize():
                                         Printing.create_database(action)))
            create_buttons[i].grid(row=i+1, column=1)
        buttons.pack()
        exit_buttons = Frame(root)
        turn_off_button = Button(exit_buttons, text="Turn off", command=turn_off)
        turn_off_button.grid(row=0, column=0)
        nilesh_button = Button(exit_buttons, text="To NiLeSh", command=to_nilesh)
        nilesh_button.grid(row=0, column=1)
        exit_buttons.pack()
        comment = Label(root, text="")
        comment.pack()
        comment.configure(text="Welcome, user!")
        root.mainloop()

    way = [["database"]]
    length = 0
    while True:
        if len(way) == length:
            return False
        length = len(way)
        if way[len(way) - 1][0] == "database":
            database_window()
        elif way[len(way) - 1][0] == "nilesh":
            if superior != "nilesh":
                if GraphicalNiLeSh.nilesh("databases"):
                    way.append(["database"])
            else:
                return True
        elif way[len(way) - 1][0] == "exit":
            return False
