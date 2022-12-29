#!/usr/bin/python3
from . import Errors
import os
from . import Printing


def run_from_file(file_name):
    if run_file(file_name, "check"):
        print(file_name + ": Your code seems good. I am starting executing it.")
        if run_file(file_name, "execute"):
            print(file_name + ": Your code was executed.")
            return True
    return False


def run_file(file_name, mode):
    read_file = open(file_name, "r")
    args = [True, 0, "", "", file_name, 1, 0, False, -1]
    #   Arguments:
    #   [NoError, TypeOfExecutedLine,
    #   Subject, Language, FileName,
    #   Line, NumberOfQuestions, End,
    #   LessonNumber]
    for line in read_file:
        args = read_line(mode, line, args)
        if not args[0]:
            read_file.close()
            return False
        elif args[7]:
            read_file.close()
            return True
        else:
            args[5] += 1
    if not args[7]:
        Errors.missing_end_error()
        return False


def run_from_console():
    while True:
        args = [True, 0, "", "", "", 1, 0, False, -1]
        while True:
            data = str(input("NiLeSh# "))
            if data == "":
                continue
            args = read_line("execute", data, args)
            if args[0] == "False":
                return
            elif args[7]:
                print("Your code was executed.")
                break
            else:
                args[5] += 1
        if y_or_n("Do You want to end?"):
            break


def run_strings(strings, mode):
    args = [True, 0, "", "", "", 1, 0, False, -1]
    #   Arguments:
    #   [NoError, TypeOfExecutedLine,
    #   Subject, Language, FileName,
    #   Line, NumberOfQuestions, End,
    #   LessonNumber]
    for line in strings:
        args = read_line(mode, line, args)
        if not args[0]:
            return False
        elif args[7]:
            if mode == "check":
                return True
            else:
                return args[8]
        else:
            args[5] += 1
    if not args[7]:
        Errors.missing_end_error()
        return False


def read_line(mode, line, args):
    if line in ["\n", " \n"]:
        return args
    line = line.replace("\n", "")
    words = line.split("//")
    if args[1] == 0:
        if words[0] == "nilesh codes":
            args[1] = 2
        else:
            if words[0] not in ["math", "physics", "chemistry", "biology", "geography", "history",
                                "english", "german", "czech", "russian", "french", "spanish",
                                "literature", "music", "art", "informatics"]:
                Errors.first_line_error(line, args[5])
                args[0] = False
                return args
            elif words[1] not in ["english", "czech", "russian", "german", "french", "spanish"]:
                Errors.first_line_error(line, args[5])
                args[0] = False
                return args
            elif mode == "execute":
                args[2] = words[0]
                args[3] = words[1]
            args[1] = 1
    elif args[1] == 1:
        if (len(words) > 1) or (words[0] in ["{", "}"]):
            Errors.file_choosing_error(line, args[5])
            args[0] = False
            return args
        elif words[0] == "menu":
            Errors.new_nilem_error(line, args[5])
            args[0] = False
            return args
        elif mode == "execute":
            path = words[0].split("/")
            args[8] = Printing.add_lesson(args[3], args[2], path[len(path) - 1])
        args[1] = 2
    elif args[1] == 2:
        if words not in [["{"]]:
            Errors.file_start_error(line, args[5])
            args[0] = False
            return args
        args[1] = 3
    elif args[1] == 3:
        if words[0] == "}":
            args[1] = 4
        else:
            if words[0] == "enter":
                if len(words) != 3:
                    Errors.wrong_count_of_words_error(line, args[5], 3)
                    args[0] = False
                    return args
                elif (args[2] == "") & (mode == "execute"):
                    Errors.wrong_case_error(line, args[5], words[0])
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.add_enter(args[3], args[8], args[6], words[1], words[2])
                    args[6] += 1
            elif words[0] == "radio":
                if len(words) != 4:
                    Errors.wrong_count_of_words_error(line, args[5], 4)
                    args[0] = False
                    return args
                elif (args[2] == "") & (mode == "execute"):
                    Errors.wrong_case_error(line, args[5], words[0])
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.add_radio(args[3], args[8], args[6], words[1], words[2], words[3])
                    args[6] += 1
            elif words[0] == "update":
                Errors.new_nilem_error(line, args[5])
                args[0] = False
                return args
            elif words[0] == "explain":
                if len(words) != 2:
                    Errors.wrong_count_of_words_error(line, args[5], 2)
                    args[0] = False
                    return args
                elif (args[2] == "") & (mode == "execute"):
                    Errors.wrong_case_error(line, args[5], words[0])
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.add_explain(args[3], args[8], args[6], words[1])
                    args[6] += 1
            elif words[0] == "run":
                if len(words) != 2:
                    Errors.wrong_count_of_words_error(line, args[5], 2)
                    args[0] = False
                    return args
                elif mode == "execute":
                    file_name = get_outer_path(args[4], 1) + words[1]
                    if os.path.isfile(file_name):
                        run_from_file(file_name)
                    else:
                        Errors.missing_file_error(line, args[5], file_name)
            else:
                Errors.file_middle_error(line, args[5])
    elif (args[1] == 4) & (words[0] == "end"):
        args[7] = True
        return args
    return args


def get_outer_path(file_name, steps):
    path = file_name.split("/")
    result = ""
    for i in range(len(path) - steps):
        result += path[i] + "/"
    return result


def y_or_n(string):
    while True:
        print(string)
        answer = str(input("y/n "))
        if answer in ["y", "n", "Y", "N", "yes", "no", "Yes", "No"]:
            break
        else:
            print("Unknown answer.")
    if answer in ["y", "Y", "yes", "Yes"]:
        return True
    else:
        return False
