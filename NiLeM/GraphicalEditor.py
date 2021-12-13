#!/usr/bin/python3
from tkinter import *
import math
from . import Translations
from . import ReadDatabase
from . import Printing
from . import Runner


def editor_main_menu(self):
    self.erase()
    Label(self.root, text="Editor", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    subjects = Frame(self.root, bg=self.background_color)
    subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                    "english", "czech", "russian", "german", "french", "spanish",
                    "literature", "music", "art", "informatics"]
    subject_buttons = []
    for i in range(len(subject_list)):
        subject_buttons.append(Button(subjects, image=self.subject_images[i],
                                      command=lambda action=subject_list[i]:
                                      self.editor_subject_menu(action),
                                      bg=self.background_color, fg=self.text_color))
        subject_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
    subjects.pack()
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


def editor_subject_menu(self, subject):
    self.erase()
    Label(self.root, text="Editor", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    [lesson_list, lesson_ids] = ReadDatabase.get_subject_lessons(subject, self.language)
    lesson_buttons = []
    lessons = Frame(self.root, bg=self.background_color)
    i = -1
    for i in range(len(lesson_list)):
        lesson_buttons.append(Button(lessons, text=lesson_list[i],
                                     command=lambda action_id=lesson_ids[i],
                                     action_name=lesson_list[i]:
                                     self.editor(subject, action_id, action_name),
                                     bg=self.background_color, fg=self.text_color))
        lesson_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
    i += 1
    lesson_buttons.append(Button(lessons, text="New",
                                 command=lambda:
                                 self.editor(subject, -1, ""),
                                 bg=self.background_color, fg=self.text_color))
    lesson_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
    lessons.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.editor_main_menu(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()


def editor(self, subject, lesson_id, lesson_name):
    def save():
        Printing.delete_lesson(self.language, lesson_id)
        strings = field.get(1.0, "end").split("\n")
        if Runner.run_strings(strings, "check"):
            Runner.run_strings(strings, "execute")
        self.editor_subject_menu(subject)

    def delete():
        Printing.delete_lesson(self.language, lesson_id)
        self.editor_subject_menu(subject)

    self.erase()
    Label(self.root, text="Editor", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    questions = ReadDatabase.get_lesson_questions(self.language, lesson_id)
    for question in range(len(questions)):
        if questions[question][0] == "radio":
            questions[question][3] = str(questions[question][3])
    field = Text(self.root, bg=self.background_color, fg=self.text_color)
    field.pack()
    if lesson_id != -1:
        field.insert(END,
                     subject + "//" + self.language + "\n" +
                     lesson_name + "\n" +
                     "{\n")
        for question in range(len(questions)):
            field.insert(END, "//".join(questions[question]) + "\n")
        field.insert(END, "{\nend\n")
    save_buttons = Frame(self.root, bg=self.background_color)
    save_button = Button(save_buttons, text="Save & Exit",
                         command=lambda: save(),
                         bg=self.background_color, fg=self.text_color)
    save_button.grid(row=0, column=0)
    delete_button = Button(save_buttons, text="Delete & Exit",
                           command=lambda: delete(),
                           bg=self.background_color, fg=self.text_color)
    delete_button.grid(row=0, column=1)
    save_buttons.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.on_subject_menu(subject, self.language),
                         command=lambda: self.editor_subject_menu(subject),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()
