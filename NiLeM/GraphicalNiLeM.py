#!/usr/bin/python3
from tkinter import *
from . import ReadDatabase
from . import Translations
import math


def nilem_menu(self):
    self.erase()
    Label(self.root, text="NiLeM", font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    Label(self.root, text=Translations.subjects(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    subjects = Frame(self.root, bg=self.background_color)
    subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                    "english", "czech", "russian", "german", "french", "spanish",
                    "literature", "music", "art", "informatics"]
    subject_buttons = []
    for i in range(len(subject_list)):
        subject_buttons.append(Button(subjects, image=self.subject_images[i],
                                      command=lambda action=subject_list[i]:
                                      self.subject_menu(action),
                                      bg=self.background_color, fg=self.text_color))
        subject_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
    subjects.pack()
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


def subject_menu(self, subject):
    self.erase()
    Label(self.root, text=Translations.subject_name(subject, self.language),
          font=("Lucida Sans", 60), bg=self.background_color, fg=self.text_color).pack()
    [lesson_list, lesson_ids] = ReadDatabase.get_subject_lessons(subject, self.language)
    lesson_buttons = []
    lessons = Frame(self.root, bg=self.background_color)
    for i in range(len(lesson_list)):
        lesson_buttons.append(Button(lessons, text=lesson_list[i],
                                     command=lambda action_subject=subject,
                                                    action_id=lesson_ids[i],
                                                    action_name=lesson_list[i]:
                                     self.lesson(action_subject, action_id, action_name),
                                     bg=self.background_color, fg=self.text_color))
        lesson_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
    lessons.pack()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.to_main(self.language),
                         command=lambda: self.nilem_menu(),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()


def lesson(self, subject, lesson_id, lesson_name):
    def check_action():
        actual_question = questions[int(question_number["text"])-1]
        if actual_question[0] == "enter":
            if answer_place.winfo_children()[0].get() == actual_question[2]:
                result.configure(text=Translations.good(self.language))
            else:
                result.configure(text=Translations.bad(self.language))
        elif actual_question[0] == "radio":
            if var.get() == actual_question[3]:
                result.configure(text=Translations.good(self.language))
            else:
                result.configure(text=Translations.bad(self.language))

    def next_action():
        result.configure(text=Translations.no_checked_answer(self.language))
        for widget in answer_place.winfo_children():
            widget.destroy()
        for widget in question.winfo_children():
            widget.destroy()
        if question_number["text"] != question_max["text"]:
            new_question = questions[int(question_number["text"])]
            lines = new_question[1].split("\\n")
            for line in lines:
                Label(question, text=line, bg=self.background_color, fg=self.text_color).pack()
            if new_question[0] == "explain":
                hint.configure(text=Translations.read_info(self.language))
            elif new_question[0] == "enter":
                hint.configure(text=Translations.enter_answer(self.language))
                Entry(answer_place, bg=self.background_color, fg=self.text_color).pack()
            elif new_question[0] == "radio":
                hint.configure(text=Translations.choose_answer(self.language))
                answers = new_question[2].split("|")
                for i in range(len(answers)):
                    Radiobutton(answer_place, text=answers[i], variable=var, value=i,
                                bg=self.background_color, fg=self.text_color,
                                selectcolor=self.background_color).pack()
            question_number.configure(text=str(int(question_number["text"]) + 1))
        else:
            hint.configure(text=Translations.congrats(self.language))

    self.erase()
    Label(self.root, text=lesson_name.capitalize(), font=("Lucida Sans", 60),
          bg=self.background_color, fg=self.text_color).pack()
    questions = ReadDatabase.get_lesson_questions(self.language, lesson_id)
    lesson_place = Frame(self.root, bg=self.background_color)
    question_data = Frame(lesson_place, bg=self.background_color)
    Label(question_data, text=Translations.your_question(self.language), bg=self.background_color,
          fg=self.text_color).grid(row=0, column=0)
    question_number = Label(question_data, text="0", bg=self.background_color,
                            fg=self.text_color)
    question_number.grid(row=0, column=1)
    Label(question_data, text=Translations.total_questions(self.language), bg=self.background_color,
          fg=self.text_color).grid(row=1, column=0)
    question_max = Label(question_data, text=str(len(questions)),
                         bg=self.background_color, fg=self.text_color)
    question_max.grid(row=1, column=1)
    question_data.pack()
    hint = Label(lesson_place, text=Translations.click_on_next(self.language),
                 bg=self.background_color, fg=self.text_color)
    hint.pack()
    question = Frame(lesson_place, bg=self.background_color)
    question.pack()
    answer_place = Frame(lesson_place, bg=self.background_color)
    answer_place.pack()
    result = Label(lesson_place, text=Translations.no_checked_answer(self.language),
                   bg=self.background_color, fg=self.text_color)
    result.pack()
    buttons = Frame(lesson_place, bg=self.background_color)
    check_button = Button(buttons, text=Translations.button_check(self.language),
                          command=lambda: check_action(),
                          bg=self.background_color, fg=self.text_color)
    check_button.grid(row=0, column=0)
    next_button = Button(buttons, text=Translations.button_next(self.language),
                         command=lambda: next_action(),
                         bg=self.background_color, fg=self.text_color)
    next_button.grid(row=0, column=1)
    buttons.pack()
    lesson_place.pack()
    var = IntVar()
    exit_buttons = Frame(self.root, bg=self.background_color)
    turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                             command=lambda: self.turn_off(),
                             bg=self.background_color, fg=self.text_color)
    turn_off_button.grid(row=0, column=0)
    back_button = Button(exit_buttons, text=Translations.on_subject_menu(subject, self.language),
                         command=lambda action=subject: self.subject_menu(action),
                         bg=self.background_color, fg=self.text_color)
    back_button.grid(row=0, column=1)
    exit_buttons.pack()
