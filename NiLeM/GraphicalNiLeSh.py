#!/usr/bin/python3
import os
from . import Runner
from tkinter import *
from . import Translations
from . import Printing
from . import Settings


def nilesh_main(self):
    self.erase()
    Label(self.root, text="NiLeSh", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    nilesh_buttons = Frame(self.root, bg=self.background_color)
    explorer_button = Button(nilesh_buttons, text=Translations.file_runner(self.language),
                             command=lambda: self.nilesh_file_explorer(),
                             bg=self.background_color, fg=self.text_color)
    explorer_button.grid(row=0, column=0)
    databases_button = Button(nilesh_buttons, text=Translations.databases(self.language),
                              command=lambda: self.nilesh_databases_worker(),
                              bg=self.background_color, fg=self.text_color)
    databases_button.grid(row=0, column=1)
    ide_button = Button(nilesh_buttons, text="IDE", command=lambda: self.ide(),
                        bg=self.background_color, fg=self.text_color)
    ide_button.grid(row=0, column=2)
    editor_button = Button(nilesh_buttons, text="Editor", command=lambda:
                           self.editor_main_menu(),
                           bg=self.background_color, fg=self.text_color)
    editor_button.grid(row=0, column=3)
    nilesh_buttons.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.main_menu(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()


def nilesh_file_explorer(self):
    def walker(location):
        comment.configure(text="")
        if Runner.get_outer_path(location, 2) != "":
            out_button.configure(command=lambda action=Runner.get_outer_path(location, 2):
                                 walker(action))
        else:
            out_button.configure(command=lambda: comment.configure(text="Can not exit."))
        for widget in frame.winfo_children():
            widget.destroy()
        directories = [f for f in os.listdir(location) if not
                       os.path.isfile(os.path.join(location, f))]
        i = 0
        for directory in directories:
            Button(frame, text=directory + "/",
                   command=lambda action=location + directory + "/": walker(action),
                   bg=self.background_color, fg=self.text_color).grid(row=i, column=0)
            i += 1
        files = [f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))]
        i = 0
        for file in files:
            Button(frame, text=file,
                   command=lambda action=location + file: interactive_run(action),
                   bg=self.background_color, fg=self.text_color).grid(row=i, column=1)
            i += 1

    def interactive_run(file_name):
        comment.configure(text="")
        if Runner.run_from_file(file_name):
            comment.configure(text="Done")
        else:
            comment.configure(text="Error")

    self.erase()
    Label(self.root, text="NiLeSh", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    out_button = Button(self.root, text="../", command=None,
                        bg=self.background_color, fg=self.text_color)
    out_button.pack()
    frame = Frame(self.root, bg=self.background_color)
    frame.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.nilesh_main(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()
    comment = Label(self.root, text="", bg=self.background_color, fg=self.text_color)
    comment.pack()
    walker("NileshScripts/")


def nilesh_databases_worker(self):
    self.erase()
    Label(self.root, text="NiLeSh", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    buttons = Frame(self.root, bg=self.background_color)
    Label(buttons, text=Translations.delete(self.language), bg=self.background_color,
          fg=self.text_color).grid(row=0, column=0)
    Label(buttons, text=Translations.create(self.language), bg=self.background_color,
          fg=self.text_color).grid(row=0, column=1)
    Button(buttons, text=Translations.local(self.language),
           command=lambda: Printing.delete_database("local"),
           bg=self.background_color, fg=self.text_color).grid(row=1, column=0)
    Button(buttons, text=Translations.local(self.language),
           command=lambda: Settings.create_database(),
           bg=self.background_color, fg=self.text_color).grid(row=1, column=1)
    languages = ["english", "czech", "russian", "german", "french", "spanish"]
    delete_buttons = []
    create_buttons = []
    for i in range(len(languages)):
        delete_buttons.append(Button(buttons, text=Translations.subject_name(languages[i], self.language),
                                     command=lambda action=languages[i].capitalize():
                                     Printing.delete_database(action),
                                     bg=self.background_color, fg=self.text_color))
        delete_buttons[i].grid(row=i + 2, column=0)
        create_buttons.append(Button(buttons, text=Translations.subject_name(languages[i], self.language),
                                     command=lambda action=languages[i].capitalize():
                                     Printing.create_database(action),
                                     bg=self.background_color, fg=self.text_color))
        create_buttons[i].grid(row=i + 2, column=1)
    buttons.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.nilesh_main(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()
