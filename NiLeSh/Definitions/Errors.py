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
