#!/usr/bin/python3
from tkinter import *
from . import Settings
from . import ReadDatabase
from . import Translations
import math


class NiLeM:
    def __init__(self):
        self.language = Settings.get_setting("language")
        self.root = Tk()
        language_list = ["english", "czech", "russian", "german", "french", "spanish"]
        self.language_images = []
        for i in range(len(language_list)):
            self.language_images.append(PhotoImage(file="Pictures/" + language_list[i].capitalize() + ".png"))
        self.about_image = PhotoImage(file="Pictures/About.png")
        mode_list = ["dark", "light", "fire", "water", "grass"]
        self.mode_images = []
        for i in range(len(mode_list)):
            self.mode_images.append(PhotoImage(file="Pictures/" + mode_list[i].capitalize() + ".png"))
        subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                        "english", "czech", "russian", "german", "french", "spanish",
                        "literature", "music", "art", "informatics"]
        self.subject_images = []
        for i in range(len(subject_list)):
            self.subject_images.append(PhotoImage(file="Pictures/" + subject_list[i].capitalize() + ".png"))
        self.root.attributes("-fullscreen", True)
        self.root.title("NiLeM")
        self.root.configure(background="black")
        self.text_color = "#fff"
        self.background_color = "#000"
        self.change_mode(Settings.get_setting("mode"))
        self.root.mainloop()

    def turn_off(self):
        self.root.destroy()

    def change_mode(self, mode):
        Settings.change_setting("mode", mode)
        if mode == "dark":
            self.root.configure(background="black")
            self.text_color = "#fff"
            self.background_color = "#000"
        elif mode == "light":
            self.root.configure(background="white")
            self.text_color = "#000"
            self.background_color = "#fff"
        elif mode == "fire":
            self.root.configure(background="red")
            self.text_color = "#000"
            self.background_color = "#f00"
        elif mode == "water":
            self.root.configure(background="blue")
            self.text_color = "#000"
            self.background_color = "#00f"
        elif mode == "grass":
            self.root.configure(background="green")
            self.text_color = "#000"
            self.background_color = "#0f0"
        self.main_menu()

    def erase(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def change_language(self, language):
        self.language = language
        Settings.change_setting("language", language)
        self.main_menu()

    def main_menu(self):
        self.erase()
        Label(self.root, text=Translations.main(self.language), font=("Lucida Sans", 60),
              bg=self.background_color, fg=self.text_color).pack()
        main_part = Frame(self.root, bg=self.background_color)
        left = Frame(main_part, bg=self.background_color)
        right = Frame(main_part, bg=self.background_color)
        Label(left, text=Translations.languages(self.language), font=("Lucida Sans", 40),
              bg=self.background_color, fg=self.text_color).pack()
        languages = Frame(left, bg=self.background_color)
        language_list = ["english", "czech", "russian", "german", "french", "spanish"]
        language_buttons = []
        for i in range(len(language_list)):
            language_buttons.append(Button(languages, image=self.language_images[i],
                                           command=lambda action=language_list[i]: self.change_language(action),
                                           bg=self.background_color, fg=self.text_color))
            language_buttons[i].grid(row=0, column=i)
        languages.pack()
        Label(left, text=Translations.about(self.language), font=("Lucida Sans", 40),
              bg=self.background_color, fg=self.text_color).pack()
        about_button = Button(left, image=self.about_image, command=lambda: self.info(),
                              bg=self.background_color, fg=self.text_color)
        about_button.pack()
        Label(left, text=Translations.mode(self.language), font=("Lucida Sans", 40),
              bg=self.background_color, fg=self.text_color).pack()
        modes = Frame(left, bg=self.background_color)
        mode_list = ["dark", "light", "fire", "water", "grass"]
        mode_buttons = []
        for i in range(len(mode_list)):
            mode_buttons.append(Button(modes, image=self.mode_images[i],
                                       command=lambda action=mode_list[i]: self.change_mode(action),
                                       bg=self.background_color, fg=self.text_color))
            mode_buttons[i].grid(row=0, column=i)
        modes.pack()
        Label(right, text=Translations.subjects(self.language), font=("Lucida Sans", 40),
              bg=self.background_color, fg=self.text_color).pack()
        subjects = Frame(right, bg=self.background_color)
        subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                        "english", "czech", "russian", "german", "french", "spanish",
                        "literature", "music", "art", "informatics"]
        subject_buttons = []
        for i in range(len(subject_list)):
            subject_buttons.append(Button(subjects, image=self.subject_images[i],
                                          command=lambda action=subject_list[i]: self.subject_menu(action),
                                          bg=self.background_color, fg=self.text_color))
            subject_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
        subjects.pack()
        left.grid(row=0, column=0)
        right.grid(row=0, column=1)
        main_part.pack()
        turn_off_button = Button(self.root, text=Translations.turn_off(self.language),
                                 command=lambda: self.turn_off(),
                                 bg=self.background_color, fg=self.text_color)
        turn_off_button.pack()

    def subject_menu(self, subject):
        self.erase()
        Label(self.root, text=Translations.subject_name(subject, self.language), font=("Lucida Sans", 60),
              bg=self.background_color, fg=self.text_color).pack()
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
                             command=lambda: self.main_menu(),
                             bg=self.background_color, fg=self.text_color)
        back_button.grid(row=0, column=1)
        exit_buttons.pack()

    def lesson(self, subject, lesson_id, lesson_name):
        def check_action():
            actual_question = questions[int(question_number["text"])-1]
            if actual_question[0] == "enter":
                for widget in answer_place.winfo_children():
                    if widget.get() == actual_question[2]:
                        result.configure(text=Translations.good(self.language))
                    else:
                        result.configure(text=Translations.bad(self.language))
                    break
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
        Label(question_data, text="Your question:", bg=self.background_color, fg=self.text_color) \
            .grid(row=0, column=0)
        question_number = Label(question_data, text="0", bg=self.background_color, fg=self.text_color)
        question_number.grid(row=0, column=1)
        Label(question_data, text="Total questions:", bg=self.background_color, fg=self.text_color) \
            .grid(row=1, column=0)
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

    def info(self):
        self.erase()
        Label(self.root, text=Translations.about(self.language), font=("Lucida Sans", 60),
              bg=self.background_color, fg=self.text_color).pack()
        for i in range(4):
            Label(self.root, text=Translations.about_string(self.language, i),
                  bg=self.background_color, fg=self.text_color).pack()
        exit_buttons = Frame(self.root, bg=self.background_color)
        turn_off_button = Button(exit_buttons, text=Translations.turn_off(self.language),
                                 command=lambda: self.turn_off(),
                                 bg=self.background_color, fg=self.text_color)
        turn_off_button.grid(row=0, column=0)
        back_button = Button(exit_buttons, text=Translations.to_main(self.language), command=lambda: self.main_menu(),
                             bg=self.background_color, fg=self.text_color)
        back_button.grid(row=0, column=1)
        exit_buttons.pack()
