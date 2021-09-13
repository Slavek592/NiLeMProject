#!/usr/bin/python3
from . import Translations


def print_header(file, length_of_path):
    file.write(
        "<!DOCTYPE html>\n"
        "<html>\n"
        "    <head>\n"
        "        <title>Nikiforov's Learning Machine</title>\n"
        "        <meta charset=\"utf-8\"/>\n"
    )
    link_line = "        <link rel=\"stylesheet\" href=\""
    for i in range(length_of_path):
        link_line += "../"
    link_line += "styles.css\">\n"
    file.write(
        link_line +
        "    </head>\n"
        "\n"
        "    <body>\n"
    )


def print_start_of_body(file, name, language, subject, length_of_path, case):
    if case == "menu":
        file.write(
            "        <h1>" + Translations.subject_name(subject, language) + "</h1>\n"
        )
    else:
        file.write(
            "        <h1>" + name + "</h1>\n"
        )
    if case == "menu":
        file.write(
            "        <p><a href=\"../Main" + Translations.file_language(language) +
            ".html\">" + Translations.to_main(language) + "</a></p>\n"
        )
    else:
        file.write(
            "        <div id=\"q\" class=\"container\">"
            + Translations.click_on_next(language) + "</div>\n"
            "        <p>\n"
            "            <button type=\"button\" onclick=\"ChangeContent()\">"
            + Translations.button_next(language) + "</button>\n"
            "            <button type=\"button\" onclick=\"Check()\">"
            + Translations.button_check(language) + "</button>\n"
            "        </p>\n"
            "        <p id=\"c\">" + Translations.no_checked_answer(language) + "</p>\n"
        )
        file.write("        <p><a href=\"")
        for i in range(length_of_path):
            file.write("../")
        file.write(
            subject.capitalize() + Translations.file_language(language) + ".html\">" +
            Translations.on_subject_menu(subject, language) + "</a></p>\n"
        )


def print_start_of_script(file):
    file.write(
        "        <script>\n"
        "            question = 0;\n"
    )


def print_end_of_script(file):
    file.write(
        "        </script>\n"
    )


def print_end_of_body(file):
    file.write(
        "    </body>\n"
        "</html>\n"
    )


def create_storing_files(file_name, language):
    file = open(file_name + ".change", "w")
    file.write(
        "            function ChangeContent()\n"
        "            {\n"
        "                document.getElementById(\"q\").innerHTML = \"\";\n"
        "                document.getElementById(\"c\").innerHTML = \""
        + Translations.no_checked_answer(language) + "\";"
        "\n"
    )
    file.close()
    file = open(file_name + ".check", "w")
    file.write(
        "            function Check()\n"
        "            {\n"
    )
    file.close()


def add_closings_to_storing_files(file_name, language):
    file = open(file_name + ".change", "a")
    file.write(
        "                else\n"
        "                {\n"
        "                    var text = document.createElement(\"p\");\n"
        "                    text.appendChild(document.createTextNode(\""
        + Translations.congrats(language) + "\"));\n"
        "                    document.getElementById(\"q\").appendChild(text);\n"
        "                }\n"
        "            }\n"
    )
    file.close()
    file = open(file_name + ".check", "a")
    file.write(
        "            }\n"
    )
    file.close()


def store_enter(file_name, question, answer, question_number, language):
    file = open(file_name + ".change", "a")
    if question_number == 0:
        file.write(
            "                if (question == 0)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number) + ")\n"
        )
    file.write(
        "                {\n"
        "                    question = " + str(question_number + 1) + ";\n"
        "                    var text = document.createElement(\"p\");\n"
        "                    text.appendChild(document.createTextNode(\""
        + Translations.enter_answer(language) + "\"));\n"
        "                    document.getElementById(\"q\").appendChild(text);\n"
        "\n"
        "                    var text = document.createElement(\"p\");\n"
        "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
        "                    document.getElementById(\"q\").appendChild(text);\n"
        "\n"
        "                    var inputplace = document.createElement(\"p\");\n"
        "                    var inputbox = document.createElement(\"input\");\n"
        "                    inputbox.type = \"text\";\n"
        "                    inputbox.id = \"ans\";\n"
        "                    inputbox.name = \"ans\";\n"
        "                    inputplace.appendChild(inputbox);\n"
        "                    document.getElementById(\"q\").appendChild(inputplace);\n"
        "                }\n"
    )
    file.close()
    file = open(file_name + ".check", "a")
    if question_number == 0:
        file.write(
            "                if (question == 1)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number + 1) + ")\n"
        )
    file.write(
        "                {\n"
        "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
        "                    {\n"
        "                        document.getElementById(\"c\").innerHTML = \""
        + Translations.good(language) + "\";\n"
        "                    }\n"
        "                    else\n"
        "                    {\n"
        "                        document.getElementById(\"c\").innerHTML = \""
        + Translations.bad(language) + "\";\n"
        "                    }\n"
        "                }\n"
    )
    file.close()


def store_radio(file_name, question, answers, correct_answer, question_number, language):
    answers = answers.split("|")
    file = open(file_name + ".change", "a")
    if question_number == 0:
        file.write(
            "                if (question == 0)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number) + ")\n"
        )
    file.write(
        "                {\n"
        "                    question = " + str(question_number + 1) + ";\n"
        "                    var text = document.createElement(\"p\");\n"
        "                    text.appendChild(document.createTextNode(\""
        + Translations.choose_answer(language) + "\"));\n"
        "                    document.getElementById(\"q\").appendChild(text);\n"
        "\n"
        "                    var text = document.createElement(\"p\");\n"
        "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
        "                    document.getElementById(\"q\").appendChild(text);\n"
        "\n"
        "                    var inputplace = document.createElement(\"p\");\n"
        "                    inputplace.id = \"inp\";\n"
    )
    for answer in answers:
        file.write(
            "                    var inputradio = document.createElement(\"input\");\n"
            "                    inputradio.type = \"radio\";\n"
            "                    inputradio.id = \"ans\";\n"
            "                    inputradio.name = \"ans\";\n"
            "                    inputplace.appendChild(inputradio);\n"
            "                    inputplace.appendChild(document.createTextNode(\"" + answer + "\"));\n"
        )
    file.write(
        "                    document.getElementById(\"q\").appendChild(inputplace);\n"
        "                }\n"
    )
    file.close()
    file = open(file_name + ".check", "a")
    if question_number == 0:
        file.write(
            "                if (question == 1)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number + 1) + ")\n"
        )
    file.write(
        "                {\n"
        "                    var ele = document.getElementsByName('ans');\n"
        "                    for (i = 0; i < ele.length; i++)\n"
        "                    {\n"
        "                        if (ele[i].checked)\n"
        "                        {\n"
        "                            if (i == " + correct_answer + ")\n"
        "                            {\n"
        "                                document.getElementById(\"c\").innerHTML = \""
        + Translations.good(language) + "\";\n"
        "                            }\n"
        "                            else\n"
        "                            {\n"
        "                                document.getElementById(\"c\").innerHTML = \""
        + Translations.bad(language) + "\";\n"
        "                            }\n"
        "                        }\n"
        "                    }\n"
        "                }\n"
    )
    file.close()


def store_explain(file_name, texts, question_number):
    texts = texts.split("\\n")
    file = open(file_name + ".change", "a")
    if question_number == 0:
        file.write(
            "                if (question == 0)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number) + ")\n"
        )
    file.write(
        "                {\n"
        "                    question = " + str(question_number + 1) + ";\n"
    )
    for text in texts:
        file.write(
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + text + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
        )
    file.write(
        "                }\n"
    )
    file.close()
    if question_number == 0:
        file = open(file_name + ".check", "a")
        file.write(
            "                if (question == 1)\n"
            "                {\n"
            "                }\n"
        )
        file.close()


def print_from_storing_files_to_the_main_one(file_name):
    write_file = open(file_name, "a")
    read_file = open(file_name + ".change", "r")
    for line in read_file:
        write_file.write(line)
    read_file.close()
    read_file = open(file_name + ".check", "r")
    for line in read_file:
        write_file.write(line)
    read_file.close()
    write_file.close()


def print_tests_to_menu(directory, file_name):
    file = open(file_name, "a")
    [dirpath, dirnames, filenames] = directory
    dirpath = dirpath.split("/")
    if 3 < len(dirpath) < 7:
        file.write("        <h" + str(len(dirpath) - 2) + ">" + dirpath[len(dirpath) - 1]
                   + "</h" + str(len(dirpath) - 2) + ">\n")
    file.write("        <p>\n")
    for filename in filenames:
        file.write("            <button onclick=\"window.location.href='")
        depth = 0
        for folder in dirpath:
            depth += 1
            if depth > 2:
                file.write(folder + "/")
        file.write(filename + "';\">" + filename + "</button>\n")
    file.write("        </p>\n")
