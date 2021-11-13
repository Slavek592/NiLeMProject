#!/usr/bin/python3
from tkinter import *
from . import Translations
import math
from . import Printing


def ide(self):
    def set_language(language):
        selected_language.set(Translations.subject_name(language, self.language))
        selected_language_english.set(language)

    def set_subject(subject):
        selected_subject.set(Translations.subject_name(subject, self.language))
        selected_subject_english.set(subject)

    def set_name():
        selected_name.set(name_input.get())

    def add_question():
        if question_done.get():
            Label(question_creating, text=str(question_number.get()),
                  bg=self.background_color, fg=self.text_color).pack()
            questions.append([])
            Button(instruments, text=Translations.enter_word(self.language),
                   bg=self.background_color, fg=self.text_color,
                   command=lambda: set_question_type("enter")).pack()
            Button(instruments, text=Translations.radio_word(self.language),
                   bg=self.background_color, fg=self.text_color,
                   command=lambda: set_question_type("radio")).pack()
            Button(instruments, text=Translations.explain_word(self.language),
                   bg=self.background_color, fg=self.text_color,
                   command=lambda: set_question_type("explain")).pack()
            question_done.set(False)

    def set_question_type(type_of_question):
        for widget in instruments.winfo_children():
            widget.destroy()
        question_creating.winfo_children()[len(question_creating.winfo_children()) - 1]\
            .configure(text=str(question_number.get()) + ": " + type_of_question)
        question_type.set(type_of_question)
        questions[len(questions) - 1].append(type_of_question)
        Entry(instruments, bg=self.background_color, fg=self.text_color).pack()
        Label(instruments, text=Translations.enter_question(self.language),
              bg=self.background_color, fg=self.text_color).pack()
        Button(instruments, text=Translations.button_next(self.language),
               bg=self.background_color, fg=self.text_color,
               command=lambda: set_question()).pack()

    def set_question():
        question_string = instruments.winfo_children()[0].get()
        for widget in instruments.winfo_children():
            widget.destroy()
        questions[len(questions) - 1].append(question_string)
        if question_type.get() == "explain":
            question_creating.winfo_children()[len(question_creating.winfo_children()) - 1]\
                .configure(text=str(question_number.get()) + ": explain, done")
            question_done.set(True)
            question_number.set(question_number.get() + 1)
        elif question_type.get() == "enter":
            Entry(instruments, bg=self.background_color, fg=self.text_color).pack()
            Label(instruments, text=Translations.enter_answer(self.language),
                  bg=self.background_color, fg=self.text_color).pack()
            Button(instruments, text=Translations.button_next(self.language),
                   bg=self.background_color, fg=self.text_color,
                   command=lambda: set_right_answer()).pack()
        elif question_type.get() == "radio":
            Frame(instruments, bg=self.background_color)
            Button(instruments, text="+",
                   bg=self.background_color, fg=self.text_color,
                   command=lambda: new_possible_answer()).pack()
            Label(instruments, text=Translations.enter_answer(self.language),
                  bg=self.background_color, fg=self.text_color).pack()
            Button(instruments, text=Translations.button_next(self.language),
                   bg=self.background_color, fg=self.text_color,
                   command=lambda: set_possible_answers()).pack()

    def new_possible_answer():
        Entry(instruments.winfo_children()[0],
              bg=self.background_color, fg=self.text_color).pack()
        instruments.winfo_children()[0].pack()

    def set_possible_answers():
        answers = []
        for entry in instruments.winfo_children()[0].winfo_children():
            answers.append(entry.get())
        for widget in instruments.winfo_children():
            widget.destroy()
        questions[len(questions) - 1].append(answers)
        Entry(instruments, bg=self.background_color, fg=self.text_color).pack()
        Label(instruments, text=Translations.enter_answer(self.language),
              bg=self.background_color, fg=self.text_color).pack()
        Button(instruments, text=Translations.button_next(self.language),
               bg=self.background_color, fg=self.text_color,
               command=lambda: set_right_answer()).pack()

    def set_right_answer():
        answer_string = instruments.winfo_children()[0].get()
        for widget in instruments.winfo_children():
            widget.destroy()
        questions[len(questions) - 1].append(answer_string)
        question_creating.winfo_children()[len(question_creating.winfo_children()) - 1]\
            .configure(text=str(question_number.get()) + ": " + question_type.get() + ", done")
        question_done.set(True)
        question_number.set(question_number.get() + 1)

    def save_to_database():
        if not written.get():
            written.set(True)
            language = selected_language_english.get()
            subject = selected_subject_english.get()
            new_lesson_id = Printing.add_lesson(language, subject, selected_name.get())
            for j in range(len(questions)):
                question = questions[j]
                if question[0] == "explain":
                    Printing.add_explain(language, new_lesson_id, j, question[1])
                elif question[0] == "enter":
                    Printing.add_enter(language, new_lesson_id, j, question[1], question[2])
                elif question[0] == "radio":
                    answers = ""
                    for k in range(len(question[2])):
                        if k != 0:
                            answers += "|"
                        answers += question[2][k]
                    Printing.add_radio(language, new_lesson_id, j,
                                       question[1], answers, question[3])

    self.erase()
    Label(self.root, text="IDE", font=("Lucida Sans", 60),
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
        language_buttons.append(
            Button(languages, text=Translations.subject_name(language_list[i], self.language),
                   command=lambda action=language_list[i]: set_language(action),
                   bg=self.background_color, fg=self.text_color)
        )
        language_buttons[i].grid(row=math.floor(i / 3), column=i % 3)
    languages.pack()
    selected_language = StringVar()
    selected_language.set("-")
    selected_language_english = StringVar()
    selected_language_english.set("none")
    Label(left, textvariable=selected_language, bg=self.background_color, fg=self.text_color).pack()
    Label(left, text=Translations.subjects(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    subjects = Frame(left, bg=self.background_color)
    subject_list = ["math", "physics", "chemistry", "biology", "geography", "history",
                    "english", "czech", "russian", "german", "french", "spanish",
                    "literature", "music", "art", "informatics"]
    subject_buttons = []
    for i in range(len(subject_list)):
        subject_buttons.append(
            Button(subjects, text=Translations.subject_name(subject_list[i], self.language),
                   command=lambda action=subject_list[i]: set_subject(action),
                   bg=self.background_color, fg=self.text_color)
        )
        subject_buttons[i].grid(row=math.floor(i / 4), column=i % 4)
    subjects.pack()
    selected_subject = StringVar()
    selected_subject.set("-")
    selected_subject_english = StringVar()
    selected_subject_english.set("none")
    Label(left, textvariable=selected_subject,
          bg=self.background_color, fg=self.text_color).pack()
    Label(left, text=Translations.name(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    name_input = Entry(left, bg=self.background_color, fg=self.text_color)
    name_input.pack()
    Button(left, text=Translations.word_set(self.language), bg=self.background_color,
           fg=self.text_color, command=lambda: set_name()).pack()
    selected_name = StringVar()
    selected_name.set("-")
    Label(left, textvariable=selected_name,
          bg=self.background_color, fg=self.text_color).pack()
    Label(right, text=Translations.questions(self.language), font=("Lucida Sans", 40),
          bg=self.background_color, fg=self.text_color).pack()
    question_creating = Frame(right, bg=self.background_color)
    question_creating.pack()
    questions = []
    question_done = BooleanVar()
    question_done.set(True)
    question_type = StringVar()
    question_number = IntVar()
    question_number.set(0)
    instruments = Frame(right, bg=self.background_color)
    instruments.pack()
    Button(right, text=Translations.new_question(self.language),
           command=lambda: add_question(),
           bg=self.background_color, fg=self.text_color).pack()
    Button(right, text="Save to database",
           command=lambda: save_to_database(),
           bg=self.background_color, fg=self.text_color).pack()
    written = BooleanVar()
    written.set(False)
    left.grid(row=0, column=0)
    right.grid(row=0, column=1)
    main_part.pack()
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
