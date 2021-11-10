#!/usr/bin/python3
from tkinter import *
from . import Settings
from . import ReadDatabase
from . import Translations
import math


def nilem(superior):
    def main_menu(language):
        def turn_off():
            way.append(["exit", []])
            root.destroy()

        def open_subject(subject):
            way.append(["subject", [language, subject]])
            root.destroy()

        def open_language(new_language):
            way.append(["main", [new_language]])
            root.destroy()

        def open_info():
            way.append(["about", [language]])
            root.destroy()

        def change_mode(new_mode):
            Settings.change_mode(new_mode)
            way.append(["main", [language]])
            root.destroy()

        root = Tk()
        root.attributes("-fullscreen", True)
        mode = Settings.get_mode()
        if mode == "dark":
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        elif mode == "light":
            root.configure(background="white")
            text_color = "#000"
            background_color = "#fff"
        elif mode == "fire":
            root.configure(background="red")
            text_color = "#000"
            background_color = "#f00"
        elif mode == "water":
            root.configure(background="blue")
            text_color = "#000"
            background_color = "#00f"
        elif mode == "grass":
            root.configure(background="green")
            text_color = "#000"
            background_color = "#0f0"
        else:
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        root.title("NiLeM")
        Label(root, text=Translations.main(language), font=("Lucida Sans", 60),
              bg=background_color, fg=text_color).pack()
        main_part = Frame(root, bg=background_color)
        left = Frame(main_part, bg=background_color)
        right = Frame(main_part, bg=background_color)
        Label(left, text=Translations.languages(language), font=("Lucida Sans", 40),
              bg=background_color, fg=text_color).pack()
        languages = Frame(left, bg=background_color)
        language_list = ["english", "czech", "russian", "german", "french", "spanish"]
        language_images = []
        language_buttons = []
        for i in range(len(language_list)):
            language_images.append(PhotoImage(file="Pictures/" + language_list[i].capitalize() + ".png"))
            language_buttons.append(Button(languages, image=language_images[i],
                                           command=lambda action=language_list[i]: open_language(action),
                                           bg=background_color, fg=text_color))
            language_buttons[i].grid(row=0, column=i)
        languages.pack()
        Label(left, text=Translations.about(language), font=("Lucida Sans", 40),
              bg=background_color, fg=text_color).pack()
        about_image = PhotoImage(file="Pictures/About.png")
        about_button = Button(left, image=about_image, command=lambda: open_info(),
                              bg=background_color, fg=text_color)
        about_button.pack()
        Label(left, text=Translations.mode(language), font=("Lucida Sans", 40),
              bg=background_color, fg=text_color).pack()
        modes = Frame(left, bg=background_color)
        mode_list = ["dark", "light", "fire", "water", "grass"]
        mode_images = []
        mode_buttons = []
        for i in range(len(mode_list)):
            mode_images.append(PhotoImage(file="Pictures/" + mode_list[i].capitalize() + ".png"))
            mode_buttons.append(Button(modes, image=mode_images[i],
                                       command=lambda action=mode_list[i]: change_mode(action),
                                       bg=background_color, fg=text_color))
            mode_buttons[i].grid(row=0, column=i)
        modes.pack()
        Label(right, text=Translations.subjects(language), font=("Lucida Sans", 40),
              bg=background_color, fg=text_color).pack()
        subjects = Frame(right, bg=background_color)
        subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                        "english", "czech", "russian", "german", "french", "spanish",
                        "literature", "music", "art", "informatics"]
        subject_images = []
        subject_buttons = []
        for i in range(len(subject_list)):
            subject_images.append(PhotoImage(file="Pictures/" + subject_list[i].capitalize() + ".png"))
            subject_buttons.append(Button(subjects, image=subject_images[i],
                                          command=lambda action=subject_list[i]: open_subject(action),
                                          bg=background_color, fg=text_color))
            subject_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
        subjects.pack()
        left.grid(row=0, column=0)
        right.grid(row=0, column=1)
        main_part.pack()
        turn_off_button = Button(root, text=Translations.turn_off(language), command=lambda: turn_off(),
                                 bg=background_color, fg=text_color)
        turn_off_button.pack()
        root.mainloop()

    def subject_menu(language, subject):
        def turn_off():
            way.append(["exit", []])
            root.destroy()

        def back():
            way.pop(-1)
            root.destroy()

        def open_lesson(lesson_id, lesson_name):
            way.append(["lesson", [language, subject, lesson_id, lesson_name]])
            root.destroy()

        root = Tk()
        root.attributes("-fullscreen", True)
        mode = Settings.get_mode()
        if mode == "dark":
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        elif mode == "light":
            root.configure(background="white")
            text_color = "#000"
            background_color = "#fff"
        elif mode == "fire":
            root.configure(background="red")
            text_color = "#000"
            background_color = "#f00"
        elif mode == "water":
            root.configure(background="blue")
            text_color = "#000"
            background_color = "#00f"
        elif mode == "grass":
            root.configure(background="green")
            text_color = "#000"
            background_color = "#0f0"
        else:
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        root.title("NiLeM")
        Label(root, text=Translations.subject_name(subject, language), font=("Lucida Sans", 60),
              bg=background_color, fg=text_color).pack()
        [lesson_list, lesson_ids] = ReadDatabase.get_subject_lessons(subject, language)
        lesson_buttons = []
        lessons = Frame(root, bg=background_color)
        for i in range(len(lesson_list)):
            lesson_buttons.append(Button(lessons, text=lesson_list[i],
                                         command=lambda action_id=lesson_ids[i], action_name=lesson_list[i]:
                                         open_lesson(action_id, action_name),
                                         bg=background_color, fg=text_color))
            lesson_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
        lessons.pack()
        exit_buttons = Frame(root, bg=background_color)
        turn_off_button = Button(exit_buttons, text=Translations.turn_off(language),
                                 command=lambda: turn_off(),
                                 bg=background_color, fg=text_color)
        turn_off_button.grid(row=0, column=0)
        back_button = Button(exit_buttons, text=Translations.to_main(language), command=lambda: back(),
                             bg=background_color, fg=text_color)
        back_button.grid(row=0, column=1)
        exit_buttons.pack()
        root.mainloop()

    def lesson(language, subject, lesson_id, lesson_name):
        def turn_off():
            way.append(["exit", []])
            root.destroy()

        def back():
            way.pop(-1)
            root.destroy()

        def check_action():
            actual_question = questions[int(question_number["text"])-1]
            if actual_question[0] == "enter":
                for widget in answer_place.winfo_children():
                    if widget.get() == actual_question[2]:
                        result.configure(text=Translations.good(language))
                    else:
                        result.configure(text=Translations.bad(language))
                    break
            elif actual_question[0] == "radio":
                if var.get() == actual_question[3]:
                    result.configure(text=Translations.good(language))
                else:
                    result.configure(text=Translations.bad(language))

        def next_action():
            result.configure(text=Translations.no_checked_answer(language))
            for widget in answer_place.winfo_children():
                widget.destroy()
            for widget in question.winfo_children():
                widget.destroy()
            if question_number["text"] != question_max["text"]:
                new_question = questions[int(question_number["text"])]
                lines = new_question[1].split("\\n")
                for line in lines:
                    Label(question, text=line, bg=background_color, fg=text_color).pack()
                if new_question[0] == "explain":
                    hint.configure(text=Translations.read_info(language))
                elif new_question[0] == "enter":
                    hint.configure(text=Translations.enter_answer(language))
                    Entry(answer_place, bg=background_color, fg=text_color).pack()
                elif new_question[0] == "radio":
                    hint.configure(text=Translations.choose_answer(language))
                    answers = new_question[2].split("|")
                    for i in range(len(answers)):
                        Radiobutton(answer_place, text=answers[i], variable=var, value=i,
                                    bg=background_color, fg=text_color,
                                    selectcolor=background_color).pack()
                question_number.configure(text=str(int(question_number["text"]) + 1))
            else:
                hint.configure(text=Translations.congrats(language))

        root = Tk()
        root.attributes("-fullscreen", True)
        mode = Settings.get_mode()
        if mode == "dark":
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        elif mode == "light":
            root.configure(background="white")
            text_color = "#000"
            background_color = "#fff"
        elif mode == "fire":
            root.configure(background="red")
            text_color = "#000"
            background_color = "#f00"
        elif mode == "water":
            root.configure(background="blue")
            text_color = "#000"
            background_color = "#00f"
        elif mode == "grass":
            root.configure(background="green")
            text_color = "#000"
            background_color = "#0f0"
        else:
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        root.title("NiLeM")
        Label(root, text=lesson_name.capitalize(), font=("Lucida Sans", 60),
              bg=background_color, fg=text_color).pack()
        questions = ReadDatabase.get_lesson_questions(language, lesson_id)
        lesson_place = Frame(root, bg=background_color)
        question_data = Frame(lesson_place, bg=background_color)
        Label(question_data, text="Your question:", bg=background_color, fg=text_color)\
            .grid(row=0, column=0)
        question_number = Label(question_data, text="0", bg=background_color, fg=text_color)
        question_number.grid(row=0, column=1)
        Label(question_data, text="Total questions:", bg=background_color, fg=text_color)\
            .grid(row=1, column=0)
        question_max = Label(question_data, text=str(len(questions)), bg=background_color, fg=text_color)
        question_max.grid(row=1, column=1)
        question_data.pack()
        hint = Label(lesson_place, text=Translations.click_on_next(language),
                     bg=background_color, fg=text_color)
        hint.pack()
        question = Frame(lesson_place, bg=background_color)
        question.pack()
        answer_place = Frame(lesson_place, bg=background_color)
        answer_place.pack()
        result = Label(lesson_place, text=Translations.no_checked_answer(language),
                       bg=background_color, fg=text_color)
        result.pack()
        buttons = Frame(lesson_place, bg=background_color)
        check_button = Button(buttons, text=Translations.button_check(language),
                              command=lambda: check_action(),
                              bg=background_color, fg=text_color)
        check_button.grid(row=0, column=0)
        next_button = Button(buttons, text=Translations.button_next(language),
                             command=lambda: next_action(),
                             bg=background_color, fg=text_color)
        next_button.grid(row=0, column=1)
        buttons.pack()
        lesson_place.pack()
        var = IntVar()
        exit_buttons = Frame(root, bg=background_color)
        turn_off_button = Button(exit_buttons, text=Translations.turn_off(language),
                                 command=lambda: turn_off(),
                                 bg=background_color, fg=text_color)
        turn_off_button.grid(row=0, column=0)
        back_button = Button(exit_buttons, text=Translations.on_subject_menu(subject, language),
                             command=lambda: back(), bg=background_color, fg=text_color)
        back_button.grid(row=0, column=1)
        exit_buttons.pack()
        root.mainloop()

    def about(language):
        def turn_off():
            way.append(["exit", []])
            root.destroy()

        def back():
            way.pop(-1)
            root.destroy()

        root = Tk()
        root.attributes("-fullscreen", True)
        mode = Settings.get_mode()
        if mode == "dark":
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        elif mode == "light":
            root.configure(background="white")
            text_color = "#000"
            background_color = "#fff"
        elif mode == "fire":
            root.configure(background="red")
            text_color = "#000"
            background_color = "#f00"
        elif mode == "water":
            root.configure(background="blue")
            text_color = "#000"
            background_color = "#00f"
        elif mode == "grass":
            root.configure(background="green")
            text_color = "#000"
            background_color = "#0f0"
        else:
            root.configure(background="black")
            text_color = "#fff"
            background_color = "#000"
        root.title("NiLeM")
        Label(root, text=Translations.about(language), font=("Lucida Sans", 60),
              bg=background_color, fg=text_color).pack()
        for i in range(4):
            Label(root, text=Translations.about_string(language, i),
                  bg=background_color, fg=text_color).pack()
        exit_buttons = Frame(root, bg=background_color)
        turn_off_button = Button(exit_buttons, text=Translations.turn_off(language),
                                 command=lambda: turn_off(),
                                 bg=background_color, fg=text_color)
        turn_off_button.grid(row=0, column=0)
        back_button = Button(exit_buttons, text=Translations.to_main(language), command=lambda: back(),
                             bg=background_color, fg=text_color)
        back_button.grid(row=0, column=1)
        exit_buttons.pack()
        root.mainloop()

    way = [["main", ["english"]]]
    length = 0
    while True:
        if len(way) == length:
            break
        length = len(way)
        if way[len(way) - 1][0] == "main":
            main_menu(way[len(way) - 1][1][0])
        elif way[len(way) - 1][0] == "subject":
            subject_menu(way[len(way) - 1][1][0], way[len(way) - 1][1][1])
        elif way[len(way) - 1][0] == "lesson":
            lesson(way[len(way) - 1][1][0], way[len(way) - 1][1][1],
                   way[len(way) - 1][1][2], way[len(way) - 1][1][3])
        elif way[len(way) - 1][0] == "about":
            about(way[len(way) - 1][1][0])
        elif way[len(way) - 1][0] == "exit":
            break
