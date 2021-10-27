#!/usr/bin/python3
from tkinter import *
from Definitions import Printing


def databases(superior):
    def database_window(language):
        def turn_off():
            way.append(["exit"])
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
        turn_off_button = Button(root, text="Turn off", command=turn_off)
        turn_off_button.pack()
        comment = Label(root, text="")
        comment.pack()
        comment.configure(text="Welcome, user!")
        root.mainloop()

    way = [["database", "english"]]
    length = 0
    while True:
        if len(way) == length:
            break
        length = len(way)
        if way[len(way) - 1][0] == "database":
            database_window(way[len(way) - 1][1])
        elif way[len(way) - 1][0] == "exit":
            break
