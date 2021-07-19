#!/usr/bin/python3
from . import Errors
import os
from . import Printing


def run_from_file(file_name):
    if run_file(file_name, "check"):
        print("Your code seems good. I am starting executing it.")
        if run_file(file_name, "execute"):
            print("Your code was executed.")


def run_file(file_name, mode):
    read_file = open(file_name, "r")
    args = [True, 0, "", "", "", 1, 0, False, 0, ""]
    #   Arguments:
    #   [NoError, TypeOfExecutedLine,
    #   Subject, Language, NameOfFile,
    #   Line, NumberOfQuestions, End,
    #   LengthOfPath, Case]
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


def read_line(mode, line, args):
    if line in ["\n", " \n"]:
        return args
    line = line.replace("\n", "")
    words = line.split("//")
    if args[1] == 0:
        if words[0] not in ["math", "physics", "chemistry", "biology", "geography", "history",
                            "english", "german", "czech", "russian", "french", "spanish"]:
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
        elif words[0] == "menu" and mode == "execute":
            args[9] = "menu"
            name = ""
            if os.path.isfile("NiLeM/Main.html"):
                path = "NiLeM/" + args[2].capitalize() + "/" + args[2].capitalize()
            else:
                path = args[2].capitalize()
            if args[3] == "english":
                path += ".html"
                name = args[2].capitalize()
            elif args[3] == "czech":
                path += "-czech.html"
                if args[2] == "math":
                    name = "Matematika"
                elif args[2] == "physics":
                    name = "Fyzika"
                elif args[2] == "chemistry":
                    name = "Chemie"
                elif args[2] == "biology":
                    name = "Biologie"
                elif args[2] == "geography":
                    name = "Zeměpis"
                elif args[2] == "history":
                    name = "Dějepis"
                elif args[2] == "english":
                    name = "Angličtina"
                elif args[2] == "german":
                    name = "Němčina"
                elif args[2] == "czech":
                    name = "Čeština"
                elif args[2] == "russian":
                    name = "Ruština"
                elif args[2] == "french":
                    name = "Francouzština"
                elif args[2] == "spanish":
                    name = "Španělština"
            elif args[3] == "russian":
                path += "-russian.html"
                if args[2] == "math":
                    name = "Математика"
                elif args[2] == "physics":
                    name = "Физика"
                elif args[2] == "chemistry":
                    name = "Химия"
                elif args[2] == "biology":
                    name = "Биология"
                elif args[2] == "geography":
                    name = "География"
                elif args[2] == "history":
                    name = "История"
                elif args[2] == "english":
                    name = "Английский"
                elif args[2] == "german":
                    name = "Немецкий"
                elif args[2] == "czech":
                    name = "Чешский"
                elif args[2] == "russian":
                    name = "Русский"
                elif args[2] == "french":
                    name = "Французский"
                elif args[2] == "spanish":
                    name = "Испанский"
            elif args[3] == "german":
                path += "-german.html"
                if args[2] == "math":
                    name = "Mathe"
                elif args[2] == "physics":
                    name = "Physik"
                elif args[2] == "chemistry":
                    name = "Chemie"
                elif args[2] == "biology":
                    name = "Biologie"
                elif args[2] == "geography":
                    name = "Geografie"
                elif args[2] == "history":
                    name = "Geschichte"
                elif args[2] == "english":
                    name = "Englisch"
                elif args[2] == "german":
                    name = "Deutsch"
                elif args[2] == "czech":
                    name = "Tschechisch"
                elif args[2] == "russian":
                    name = "Russisch"
                elif args[2] == "french":
                    name = "Französisch"
                elif args[2] == "spanish":
                    name = "Spanisch"
            elif args[3] == "french":
                path += "-french.html"
                if args[2] == "math":
                    name = "Mathématique"
                elif args[2] == "physics":
                    name = "Physique"
                elif args[2] == "chemistry":
                    name = "Chimie"
                elif args[2] == "biology":
                    name = "Biologie"
                elif args[2] == "geography":
                    name = "Géographie"
                elif args[2] == "history":
                    name = "Historique"
                elif args[2] == "english":
                    name = "Anglais"
                elif args[2] == "german":
                    name = "Allemand"
                elif args[2] == "czech":
                    name = "Tchèque"
                elif args[2] == "russian":
                    name = "Russe"
                elif args[2] == "french":
                    name = "Français"
                elif args[2] == "spanish":
                    name = "Espagnol"
            elif args[3] == "spanish":
                path += "-spanish.html"
                if args[2] == "math":
                    name = "Matemáticas"
                elif args[2] == "physics":
                    name = "Física"
                elif args[2] == "chemistry":
                    name = "Química"
                elif args[2] == "biology":
                    name = "Biología"
                elif args[2] == "geography":
                    name = "Geografía"
                elif args[2] == "history":
                    name = "Historial"
                elif args[2] == "english":
                    name = "Inglés"
                elif args[2] == "german":
                    name = "Alemán"
                elif args[2] == "czech":
                    name = "Checo"
                elif args[2] == "russian":
                    name = "Ruso"
                elif args[2] == "french":
                    name = "Francés"
                elif args[2] == "spanish":
                    name = "Español"
            args[4] = path
            Printing.print_header(open(args[4], "w"))
            Printing.print_start_of_body(open(args[4], "a"), name, args[3], args[2], args[8], args[9])
        elif mode == "execute":
            args[9] = "test"
            if os.path.isfile("NiLeM/Main.html"):
                path = "NiLeM/" + args[2].capitalize() + "/" + words[0] + ".html"
                args[4] = path
            else:
                args[4] = words[0] + ".html"
            Printing.print_header(open(args[4], "w"))
            path = words[0].split("/")
            args[8] = len(path)
            Printing.print_start_of_body(open(args[4], "a"), path[len(path) - 1], args[3], args[2], args[8], args[9])
            Printing.create_storing_files(args[4], args[3])
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
            elif mode == "execute":
                Printing.print_start_of_script(open(args[4], "a"))
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
                elif mode == "execute":
                    Printing.store_enter(args[4], words[1], words[2], args[6], args[3])
                    args[6] += 1
            elif words[0] == "radio":
                if len(words) != 4:
                    Errors.wrong_count_of_words_error(line, args[5], 4)
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
            elif words[0] == "explain":
                if len(words) != 2:
                    Errors.wrong_count_of_words_error(line, args[5], 2)
                    args[0] = False
                    return args
                elif mode == "execute":
                    Printing.store_explain(args[4], words[1], args[6])
                    args[6] += 1
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
    path = file_name.split("/")
    if len(path) == 1:
        return
    else:
        start = ""
        for i in range(len(path) - 1):
            start += path[i] + "/"
        start += language.capitalize() + "/"
    results = []
    results.extend(os.walk(start))
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
