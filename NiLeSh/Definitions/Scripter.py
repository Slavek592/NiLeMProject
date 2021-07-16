#!/usr/bin/python3
import os


def run_ide():
    print("Welcome to program helping writing NiLeSh scripts.")
    while True:
        while True:
            print("Do You wish to change an old file (otherwise to create a new one)?")
            command = str(input("y/n "))
            if command in ["y", "n", "Y", "N", "yes", "no", "Yes", "No"]:
                break
            else:
                print("Unknown command.")
        file_name = str(input("Enter the name of Your Nilesh file (without .nls and .nilesh). "))
        if command in ["y", "Y", "yes", "Yes"]:
            if os.path.isfile(file_name):
                update_nilesh(file_name)
            elif os.path.isfile(file_name + ".nls"):
                update_nilesh(file_name + ".nls")
            elif os.path.isfile(file_name + ".nilesh"):
                update_nilesh(file_name + ".nilesh")
            elif os.path.isfile("NileshScripts/" + file_name):
                update_nilesh("NileshScripts/" + file_name)
            elif os.path.isfile("NileshScripts/" + file_name + ".nls"):
                update_nilesh("NileshScripts/" + file_name + ".nls")
            elif os.path.isfile("NileshScripts/" + file_name + ".nilesh"):
                update_nilesh("NileshScripts/" + file_name + ".nilesh")
            else:
                print("It does not exist, I am sorry.")
        else:
            if os.path.isfile("NileshScripts/MathMenu.nls"):
                write_nilesh("NileshScripts/" + file_name + ".nls")
            else:
                write_nilesh(file_name + ".nls")
        while True:
            print("Do You wish to run it again?")
            command = str(input("y/n "))
            if command in ["y", "n", "Y", "N", "yes", "no", "Yes", "No"]:
                break
            else:
                print("Unknown command.")
        if command in ["n", "N", "no", "No"]:
            break


def write_nilesh(file_name):
    file = open(file_name, "w")
    file.close()
    file = open(file_name, "a")
    while True:
        language = str(input("Enter the language. "
                             "Possible languages are: english, czech, russian, german, french, spanish. "))
        if language in ["c", "e", "r", "g", "f", "s", "C", "E", "R", "G", "F", "S",
                        "czech", "english", "russian", "german", "french", "spanish",
                        "Czech", "English", "Russian", "German", "French", "Spanish"]:
            break
    if language in ["e", "E", "english", "English"]:
        language = "english"
    elif language in ["c", "C", "czech", "Czech"]:
        language = "czech"
    elif language in ["r", "R", "russian", "Russian"]:
        language = "russian"
    elif language in ["g", "G", "german", "German"]:
        language = "german"
    elif language in ["f", "F", "french", "French"]:
        language = "french"
    elif language in ["s", "S", "spanish", "Spanish"]:
        language = "spanish"
    while True:
        subject = str(input("Enter the language. Possible subjects are: "
                            "english, czech, russian, german, french, spanish, "
                            "math, physics, chemistry, biology, geography, history. "))
        if subject in ["czech", "english", "russian", "german", "french", "spanish",
                       "Czech", "English", "Russian", "German", "French", "Spanish",
                       "math", "physics", "chemistry", "biology", "geography", "history",
                       "Math", "Physics", "Chemistry", "Biology", "Geography", "History"]:
            break
    subject = subject.lower()
    file.write(subject + "//" + language + "\n")
    while True:
        print("Is the goal to change a menu?")
        menu = str(input("y/n "))
        if menu in ["y", "n", "Y", "N", "yes", "no", "Yes", "No"]:
            break
        else:
            print("Unknown command.")
    if menu in ["y", "Y", "yes", "Yes"]:
        file.write(
            "menu\n"
            "{\n"
            "update\n"
            "}\n"
            "end\n"
        )
    else:
        name = str(input("Enter the name of HTML file, in which to convert this code (without .html). "))
        file.write(name + "\n")
        file.write("{\n")
        while True:
            while True:
                print("Do You wish to append a new partition of the lesson?")
                command = str(input("y/n "))
                if command in ["y", "n", "Y", "N", "yes", "no", "Yes", "No"]:
                    break
                else:
                    print("Unknown command.")
            if command in ["y", "Y", "yes", "Yes"]:
                while True:
                    action = str(input("Choose the action. Possible ones are: "
                                       "enter, radio, explain. "))
                    if action in ["enter", "Enter", "radio", "Radio", "explain", "Explain"]:
                        break
                    else:
                        print("Unknown action.")
                if action in ["explain", "Explain"]:
                    question = str(input("Enter the explanation (use \"\\n\" as a new line sign): "))
                    file.write("explain//" + question + "\n")
                elif action in ["enter", "Enter", "radio", "Radio"]:
                    question = str(input("Enter the question: "))
                    if action in ["enter", "Enter"]:
                        answer = str(input("Enter the correct answer (only one): "))
                        file.write("enter//" + question + "//" + answer + "\n")
                    elif action in ["radio", "Radio"]:
                        answers = str(input("Enter the first possible answer: "))
                        while True:
                            while True:
                                print("Do You wish to append a new possible answer?")
                                command = str(input("y/n "))
                                if command in ["y", "n", "Y", "N", "yes", "no", "Yes", "No"]:
                                    break
                                else:
                                    print("Unknown command.")
                            if command in ["y", "Y", "yes", "Yes"]:
                                possible_answer = str(input("Enter the possible answer: "))
                                answers = answers + "|" + possible_answer
                            else:
                                break
                        while True:
                            correct_answer = str(input("Enter the number of the correct answer "
                                                       "(numbering starts with 0): "))
                            correct = True
                            for letter in correct_answer:
                                if letter not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                    correct = False
                                    print("Incorrect input.")
                                    break
                            if correct:
                                break
                        file.write("radio//" + question + "//" + answers + "//" + correct_answer + "\n")
            else:
                file.write(
                    "}\n"
                    "end\n"
                )
                break
    file.close()


def update_nilesh(file_name):
    pass
