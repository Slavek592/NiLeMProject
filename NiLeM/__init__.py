#!/usr/bin/python3
from tkinter import *
from . import Settings


class NiLeM:
    def __init__(self):
        self.language = Settings.get_setting("language")
        self.root = Tk()
        self.root.iconphoto(False, PhotoImage("Pictures/Physics.png"))
        language_list = ["english", "czech", "russian", "german", "french", "spanish"]
        self.language_images = []
        for i in range(len(language_list)):
            self.language_images.append(
                PhotoImage(file="Pictures/" + language_list[i].capitalize() + ".png"))
        self.language_bw_images = []
        for i in range(len(language_list)):
            self.language_bw_images.append(
                PhotoImage(file="Pictures/" + language_list[i].capitalize() + "-BW.png"))
        self.about_image = PhotoImage(file="Pictures/About.png")
        mode_list = ["dark", "light", "fire", "water", "grass"]
        self.mode_images = []
        for i in range(len(mode_list)):
            self.mode_images.append(
                PhotoImage(file="Pictures/" + mode_list[i].capitalize() + ".png"))
        subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                        "english", "czech", "russian", "german", "french", "spanish",
                        "literature", "music", "art", "informatics"]
        self.subject_images = []
        for i in range(len(subject_list)):
            self.subject_images.append(
                PhotoImage(file="Pictures/" + subject_list[i].capitalize() + ".png"))
        self.root.attributes("-fullscreen", True)
        self.root.title("NiLeM")
        self.root.configure(background="black")
        self.text_color = "#fff"
        self.background_color = "#000"
        self.change_mode(Settings.get_setting("mode"))
        self.root.mainloop()

    def turn_off(self):
        self.root.destroy()

    def erase(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    from .GraphicalNiLeM import nilem_menu, subject_menu, lesson
    from .GraphicalMain import main_menu, info, change_mode, change_language
    from .GraphicalNiLeSh import nilesh_main, nilesh_file_explorer, nilesh_databases_worker
    from .GraphicalIDE import ide
