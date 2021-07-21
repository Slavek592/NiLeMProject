#!/usr/bin/python3
import os
from . import Runner


def run_ide():
    print("Welcome to program helping writing NiLeSh scripts.")
    while True:
        file_name = str(input("Enter the name of Your Nilesh file (without .nls and .nilesh). "))
        if Runner.y_or_n("Do You wish to change an old file (otherwise to create a new one)?"):
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
        if not Runner.y_or_n("Do You wish to run it again?"):
            break


def write_nilesh(file_name):
    file = open(file_name, "w")
    file.close()
    file = open(file_name, "a")
    language = choose_language()
    subject = choose_subject()
    file.write(subject + "//" + language + "\n")
    if Runner.y_or_n("Is the goal to change a menu?"):
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
            if Runner.y_or_n("Do You wish to append a new partition to the lesson?"):
                file.write(add_partition())
            else:
                file.write(
                    "}\n"
                    "end\n"
                )
                break
    file.close()


def update_nilesh(file_name):
    print("I am checking this file.")
    if Runner.run_file(file_name, "check"):
        print("Code seems good, I am starting working with it.")
        file = open(file_name, "r")
        counter = 0
        string = ""
        for line in file:
            if counter == 0:
                if line == "nilesh codes":
                    print("I am sorry, this is a file with an array of other files to run. "
                          "It is not supported by the IDE for now.")
                    return
                words = line.replace("\n", "").split("//")
                print("Language is " + words[1] + ".")
                if change():
                    language = choose_language()
                else:
                    language = words[1]
                print("Subject is " + words[0] + ".")
                if change():
                    subject = choose_subject()
                else:
                    subject = words[0]
                string += subject + "//" + language + "\n"
                counter = 1
            elif counter == 1:
                print("Filename is now " + line.replace("\n", "") + ".")
                if change():
                    if Runner.y_or_n("Is the goal to change a menu?"):
                        string += "menu\n{\nupdate\n}\nend\n"
                        break
                    else:
                        string += str(input("Enter the name of HTML file, in which to convert this code"
                                            " (without .html). ")) + "\n"
                else:
                    string += line
                counter = 2
            elif counter == 2:
                string += "{\n"
                while True:
                    if Runner.y_or_n("Do You wish to append a new partition to the beginning of the lesson?"):
                        string += add_partition()
                    else:
                        break
                counter = 3
            elif counter == 3 and line != "}\n":
                words = line.replace("\n", "").split("//")
                if words[0] == "explain":
                    print("The command is: explain.\nThe string to write is:\n" + words[1])
                elif words[0] == "enter":
                    print("The command is: enter.\nThe question is: " + words[1] + "\nThe correct answer is: "
                          + words[2])
                elif words[0] == "radio":
                    print("The command is: radio.\nThe question is: " + words[1] + "\nThe possible answers are: "
                          + words[2] + "\nThe correct answer is the answer number (numbering from 0):" + words[3])
                elif words[0] == "update":
                    print("The command is: update.\nIt is only for updating menus, "
                          "You need to do something with it here.")
                elif words[0] == "run":
                    print("The command is: run.\nThe file to run is: " + words[1])
                if change():
                    if not Runner.y_or_n("Do You want to delete it (otherwise to change)?"):
                        string += add_partition()
                else:
                    string += line
                while True:
                    if Runner.y_or_n("Do You wish to append a new partition of the lesson?"):
                        string += add_partition()
                    else:
                        break
            elif counter == 3 and line == "}\n":
                string += "}\nend\n"
                break
        file.close()
        file = open(file_name, "w")
        file.close()
        file = open(file_name, "a")
        file.write(string)
        file.close()
    else:
        print("I am sorry, the code is broken. Open with a text editor and fix it, or remake this file.")


def choose_language():
    while True:
        language = str(input("Enter the language. "
                             "Possible languages are: english, czech, russian, german, french, spanish. "))
        if language in ["c", "e", "r", "g", "f", "s", "C", "E", "R", "G", "F", "S",
                        "czech", "english", "russian", "german", "french", "spanish",
                        "Czech", "English", "Russian", "German", "French", "Spanish"]:
            break
        else:
            print("Unknown language.")
    if language in ["e", "E", "english", "English"]:
        return "english"
    elif language in ["c", "C", "czech", "Czech"]:
        return "czech"
    elif language in ["r", "R", "russian", "Russian"]:
        return "russian"
    elif language in ["g", "G", "german", "German"]:
        return "german"
    elif language in ["f", "F", "french", "French"]:
        return "french"
    elif language in ["s", "S", "spanish", "Spanish"]:
        return "spanish"


def choose_subject():
    while True:
        subject = str(input("Enter the subject. Possible subjects are: "
                            "english, czech, russian, german, french, spanish, "
                            "math, physics, chemistry, biology, geography, history. "))
        if subject in ["czech", "english", "russian", "german", "french", "spanish",
                       "Czech", "English", "Russian", "German", "French", "Spanish",
                       "math", "physics", "chemistry", "biology", "geography", "history",
                       "Math", "Physics", "Chemistry", "Biology", "Geography", "History"]:
            break
        else:
            print("Unknown subject.")
    return subject.lower()


def add_partition():
    while True:
        action = str(input("Choose the action. Possible ones are: "
                           "enter, radio, explain, run. "))
        if action in ["enter", "Enter", "radio", "Radio", "explain", "Explain", "run", "Run"]:
            break
        else:
            print("Unknown action.")
    if action in ["explain", "Explain"]:
        question = str(input("Enter the explanation (use \"\\n\" as a new line sign): "))
        string = "explain//" + question + "\n"
        return string
    elif action in ["enter", "Enter", "radio", "Radio"]:
        question = str(input("Enter the question: "))
        if action in ["enter", "Enter"]:
            answer = str(input("Enter the correct answer (only one): "))
            string = "enter//" + question + "//" + answer + "\n"
            return string
        elif action in ["radio", "Radio"]:
            answers = str(input("Enter the first possible answer: "))
            while True:
                if Runner.y_or_n("Do You wish to append a new possible answer?"):
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
            string = "radio//" + question + "//" + answers + "//" + correct_answer + "\n"
            return string
    elif action in ["run", "Run"]:
        question = str(input("Enter the name of the file: "))
        string = "run//" + question + "\n"
        return string


def change():
    return Runner.y_or_n("Do You want to change anything?")
