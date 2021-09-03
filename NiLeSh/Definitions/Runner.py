#!/usr/bin/python3
from . import Errors
import os
from . import Printing


def run_from_file(file_name):
    if run_file(file_name, "check"):
        print(file_name + ": Your code seems good. I am starting executing it.")
        if run_file(file_name, "execute"):
            print(file_name + ": Your code was executed.")


def run_file(file_name, mode):
    read_file = open(file_name, "r")
    args = [True, 0, "", "", "", 1, 0, False, 0, "", file_name]
    #   Arguments:
    #   [NoError, TypeOfExecutedLine,
    #   Subject, Language, NameOfFile,
    #   Line, NumberOfQuestions, End,
    #   LengthOfPath, Case, FileName]
    for line in read_file:
        args = read_line(mode, line, args)
        if not args[0]:
            if os.path.isfile(args[4] + ".change"):
                os.remove(args[4] + ".change")
                os.remove(args[4] + ".check")
            read_file.close()
            return False
        elif args[7]:
            if args[9] == "test" and mode == "execute":
                os.remove(args[4] + ".change")
                os.remove(args[4] + ".check")
            read_file.close()
            return True
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
            args[9] = "codes"
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
        elif words[0] == "end":
            args[7] = True
        elif words[0] == "menu":
            args[9] = "menu"
            if mode == "execute":
                name = ""
                if os.path.isfile("NiLeM/Main.html"):
                    path = "NiLeM/" + args[2].capitalize() + "/" + args[2].capitalize()
                else:
                    Errors.nilem_not_found_error(line, args[5])
                    args[0] = False
                    return args
                if args[3] == "english":
                    path += ".html"
                else:
                    path += "-" + args[3] + ".html"
                args[4] = path
                try:
                    Printing.print_header(open(args[4], "w"), 1)
                except FileNotFoundError:
                    Errors.directory_does_not_exist_error(line, args[5], args[4])
                    args[0] = False
                    return args
                Printing.print_start_of_body(open(args[4], "a"), name, args[3], args[2], args[8], args[9])
        elif mode == "execute":
            args[9] = "test"
            if os.path.isfile("NiLeM/Main.html"):
                path = "NiLeM/" + args[2].capitalize() + "/" + args[3].capitalize() + "/" + words[0] + ".html"
                args[4] = path
            else:
                Errors.nilem_not_found_error(line, args[5])
                args[0] = False
                return args
            path = words[0].split("/")
            args[8] = len(path)
            try:
                Printing.print_header(open(args[4], "w"), args[8] + 1)
            except FileNotFoundError:
                Errors.directory_does_not_exist_error(line, args[5], args[4])
                args[0] = False
                return args
            Printing.print_start_of_body(open(args[4], "a"), path[len(path) - 1], args[3], args[2], args[8], args[9])
            Printing.create_storing_files(args[4], args[3])
        else:
            args[9] = "test"
        args[1] = 2
    elif args[1] == 2:
        if words not in [["{"]]:
            Errors.file_start_error(line, args[5])
            args[0] = False
            return args
        args[1] = 3
    elif args[1] == 3:
        if words[0] == "}":
            args[1] = 1
            if args[9] == "menu" and mode == "execute":
                search_for_files(args[4], args[3])
                Printing.print_end_of_body(open(args[4], "a"))
            elif args[9] == "test" and mode == "execute":
                Printing.print_start_of_script(open(args[4], "a"), args[8] + 1, args[3])
                Printing.add_closings_to_storing_files(args[4], args[3])
                Printing.print_from_storing_files_to_the_main_one(args[4])
                Printing.print_end_of_script(open(args[4], "a"))
                Printing.print_end_of_body(open(args[4], "a"))
        else:
            if words[0] == "enter":
                if len(words) != 3:
                    Errors.wrong_count_of_words_error(line, args[5], 3)
                    args[0] = False
                    return args
                elif args[9] != "test":
                    Errors.wrong_case_error(line, args[5], args[9], words[0])
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.store_enter(args[4], words[1], words[2], args[6], args[3])
                    args[6] += 1
            elif words[0] == "radio":
                if len(words) != 4:
                    Errors.wrong_count_of_words_error(line, args[5], 4)
                    args[0] = False
                    return args
                elif args[9] != "test":
                    Errors.wrong_case_error(line, args[5], args[9], words[0])
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.store_radio(args[4], words[1], words[2], words[3], args[6], args[3])
                    args[6] += 1
            elif words[0] == "update":
                if len(words) != 1:
                    Errors.wrong_count_of_words_error(line, args[5], 1)
                    args[0] = False
                    return args
                elif args[9] != "menu":
                    Errors.wrong_case_error(line, args[5], args[9], words[0])
                    args[0] = False
                    return args
            elif words[0] == "explain":
                if len(words) != 2:
                    Errors.wrong_count_of_words_error(line, args[5], 2)
                    args[0] = False
                    return args
                elif args[9] != "test":
                    Errors.wrong_case_error(line, args[5], args[9], words[0])
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.store_explain(args[4], words[1], args[6])
                    args[6] += 1
            elif words[0] == "run":
                if len(words) != 2:
                    Errors.wrong_count_of_words_error(line, args[5], 2)
                    args[0] = False
                    return args
                elif mode == "execute":
                    file_name = get_path(args[10]) + words[1]
                    if os.path.isfile(file_name):
                        run_from_file(file_name)
                    else:
                        Errors.missing_file_error(line, args[5], file_name)
            else:
                Errors.file_middle_error(line, args[5])
    return args


def run_from_console():
    while True:
        args = [True, 0, "", "", "", 1, 0, False, 0, ""]
        while True:
            args = read_line("execute", str(input("NiLeSh# ")), args)
            if args[0] == "False":
                if os.path.isfile(args[4] + ".change"):
                    os.remove(args[4] + ".change")
                    os.remove(args[4] + ".check")
                return
            elif args[7]:
                print("Your code was executed.")
                os.remove(args[4] + ".change")
                os.remove(args[4] + ".check")
                break
            else:
                args[5] += 1
        if y_or_n("Do You want to end?"):
            break


def search_for_files(file_name, language):
    path = get_path(file_name) + language.capitalize() + "/"
    results = []
    results.extend(os.walk(path))
    for directory in results:
        Printing.print_tests_to_menu(directory, file_name)


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


def get_path(file_name):
    path = file_name.split("/")
    if len(path) == 1:
        return
    else:
        result = ""
        for i in range(len(path) - 1):
            result += path[i] + "/"
    return result
