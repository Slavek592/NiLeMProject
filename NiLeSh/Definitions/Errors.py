#!/usr/bin/python3


def error_ending(line, number_of_line):
    print("I got:")
    print(line)
    print("Number of the line is:")
    print(number_of_line)


def first_line_error(line, number_of_line):
    print("Syntax error! File must start with the line \"subject//language\"!")
    error_ending(line, number_of_line)


def file_choosing_error(line, number_of_line):
    print("Syntax error! Code must be followed by the name of file or by \"end\"!")
    error_ending(line, number_of_line)


def file_start_error(line, number_of_line):
    print("Syntax error! Code must be followed by \"{\"!")
    error_ending(line, number_of_line)


def file_middle_error(line, number_of_line):
    print("Syntax error! Code must be followed by a command like \"enter\" "
          "and arguments (the question, the answer...), or by the \"}\"!")
    error_ending(line, number_of_line)


def wrong_count_of_words_error(line, number_of_line, expected_count_of_words):
    print("Syntax error! Expected count of words is " + str(expected_count_of_words) + "!")
    error_ending(line, number_of_line)


def missing_file_error(line, number_of_line, file_name):
    print("Error! File: " + file_name + " is mentioned, but it does not exist!")
    error_ending(line, number_of_line)


def wrong_case_error(line, number_of_line, case, command):
    print("Syntax error! Command: " + command + " was used in the case: " + case + "\n"
          "It is not supported.")
    error_ending(line, number_of_line)


def directory_does_not_exist_error(line, number_of_line, file_name):
    print("Error! A file in not existing directory was tried to be created.\n"
          "Try looking at the path and creating the directory as the solution.\n"
          "File: " + file_name)
    error_ending(line, number_of_line)


def nilem_not_found_error(line, number_of_line):
    print("Error! NiLeM folder not found. Try launching NiLeSh program from "
          "the NiLeMProject folder.")
    error_ending(line, number_of_line)
