#!/usr/bin/python3
from tkinter import *
from tkinter.filedialog import asksaveasfile
from . import ReadDatabase
from . import Translations
from . import Exporting
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
        if hint["text"] != Translations.congrats(self.language):
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

    def export_lesson():
        file_name = asksaveasfile(initialfile=lesson_name+".html",
                                  defaultextension=".html",
                                  filetypes=[("All Files", "*.*"),
                                             ("Text Documents", "*.txt"),
                                             ("HTML Documents", "*.html")]).name
        Exporting.print_header(file_name)
        Exporting.print_start_of_body(file_name, lesson_name, self.language)
        Exporting.print_start_of_script(file_name, self.language)
        Exporting.create_storing_files(file_name, self.language)
        for i in range(len(questions)):
            if questions[i][0] == "explain":
                Exporting.store_explain(file_name, questions[i][1], i,
                                        self.language)
            elif questions[i][0] == "enter":
                Exporting.store_enter(file_name, questions[i][1], questions[i][2],
                                      i, self.language)
            elif questions[i][0] == "radio":
                Exporting.store_radio(file_name, questions[i][1], questions[i][2],
                                      questions[i][3], i, self.language)
        Exporting.add_closings_to_storing_files(file_name, self.language)
        Exporting.print_from_storing_files_to_the_main_one(file_name)
        Exporting.print_end_of_script(file_name)
        Exporting.print_end_of_body(file_name)
        Exporting.delete_storing_files(file_name)

    def export_text():
        file_name = asksaveasfile(initialfile=lesson_name + ".txt",
                                  defaultextension=".txt",
                                  filetypes=[("All Files", "*.*"),
                                             ("Text Documents", "*.txt")]).name
        file = open(file_name, "w")
        file.write(
            lesson_name + "\n\n"
        )
        for i in range(len(questions)):
            file.write(
                str(i + 1) + ":\n"
            )
            if questions[i][0] == "explain":
                file.write(
                    questions[i][1] + "\n\n"
                )
            elif questions[i][0] == "enter":
                file.write(
                    questions[i][1] + "\n" +
                    questions[i][2] + "\n\n"
                )
            elif questions[i][0] == "radio":
                file.write(
                    questions[i][1] + "\n" +
                    questions[i][2].split("|")[int(questions[i][3])] + "\n\n"
                )

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
    export_buttons = Frame(self.root, bg=self.background_color)
    export_lesson_button = Button(export_buttons, text=Translations.export_lesson(self.language),
                                  command=lambda: export_lesson(),
                                  bg=self.background_color, fg=self.text_color)
    export_text_button = Button(export_buttons, text=Translations.export_text(self.language),
                                command=lambda: export_text(),
                                bg=self.background_color, fg=self.text_color)
    export_lesson_button.grid(row=0, column=0)
    export_text_button.grid(row=0, column=1)
    export_buttons.pack()
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
