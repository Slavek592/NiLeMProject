#!/usr/bin/python3
from . import Translations
import os


def print_header(file_name):
    file = open(file_name, "a")
    file.write(
        "<!DOCTYPE html>\n"
        "<html>\n"
        "    <head>\n"
        "        <title>Nikiforov's Learning Machine</title>\n"
        "        <meta charset=\"utf-8\"/>\n"
        "        <style>\n"
        "            body {\n"
        "                background-color: black;\n"
        "                color: white;\n"
        "            }\n"
        "        </style>\n"
        "    </head>\n"
        "\n"
        "    <body>\n"
    )


def print_start_of_body(file_name, name, language):
    file = open(file_name, "a")
    file.write(
        "        <h1>" + name + "</h1>\n"
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


def print_start_of_script(file_name, language):
    file = open(file_name, "a")
    file.write(
        "        <script>\n"
        "            question = -1;\n"
        "            function OwnCheckEnter(correct_answer)\n"
        "            {\n"
        "                if (document.getElementById(\"ans\").value == correct_answer)\n"
        "                {\n"
        "                    document.getElementById(\"c\").innerHTML = \""
        + Translations.good(language) + "\";\n"
        "                }\n"
        "                else\n"
        "                {\n"
        "                    document.getElementById(\"c\").innerHTML = \""
        + Translations.bad(language) + "\";\n"
        "                }\n"
        "            }\n"
        "            function OwnCheckRadio(correct_answer)\n"
        "            {\n"
        "                var ele = document.getElementsByName('ans');\n"
        "                for (i = 0; i < ele.length; i++)\n"
        "                {\n"
        "                    if (ele[i].checked)\n"
        "                    {\n"
        "                        if (i == correct_answer)\n"
        "                        {\n"
        "                            document.getElementById(\"c\").innerHTML = \""
        + Translations.good(language) + "\";\n"
        "                        }\n"
        "                        else\n"
        "                        {\n"
        "                            document.getElementById(\"c\").innerHTML = \""
        + Translations.bad(language) + "\";\n"
        "                        }\n"
        "                    }\n"
        "                }\n"
        "            }\n"
        "            function PrintLine(line)\n"
        "            {\n"
        "                var text = document.createElement(\"p\");\n"
        "                text.appendChild(document.createTextNode(line));\n"
        "                document.getElementById(\"q\").appendChild(text);\n"
        "            }\n"
        "            function CreateInputbox()\n"
        "            {\n"
        "                var inputplace = document.createElement(\"p\");\n"
        "                var inputbox = document.createElement(\"input\");\n"
        "                inputbox.type = \"text\";\n"
        "                inputbox.id = \"ans\";\n"
        "                inputbox.name = \"ans\";\n"
        "                inputplace.appendChild(inputbox);\n"
        "                document.getElementById(\"q\").appendChild(inputplace);\n"
        "            }\n"
        "            function CreateInputradio(answers)\n"
        "            {\n"
        "                var inputplace = document.createElement(\"p\");\n"
        "                inputplace.id = \"inp\";\n"
        "                for (let i = 0; i < answers.length; i++)\n"
        "                {\n"
        "                    var inputradio = document.createElement(\"input\");\n"
        "                    inputradio.type = \"radio\";\n"
        "                    inputradio.id = \"ans\";\n"
        "                    inputradio.name = \"ans\";\n"
        "                    inputplace.appendChild(inputradio);\n"
        "                    inputplace.appendChild(document.createTextNode(answers[i]));\n"
        "                }\n"
        "                document.getElementById(\"q\").appendChild(inputplace);\n"
        "            }\n"
    )


def print_end_of_script(file_name):
    file = open(file_name, "a")
    file.write(
        "        </script>\n"
    )


def print_end_of_body(file_name):
    file = open(file_name, "a")
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
        + Translations.no_checked_answer(language) + "\";\n"
        "                question++;\n"
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
        "                    PrintLine(\"" + Translations.congrats(language) + "\");\n"
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
    texts = question.split("\\n")
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
        "                    PrintLine(\"" + Translations.enter_answer(language) + "\");\n"
    )
    for text in texts:
        file.write(
            "                    PrintLine(\"" + text + "\");\n"
        )
    file.write(
        "                    CreateInputbox();\n"
        "                }\n"
    )
    file.close()
    file = open(file_name + ".check", "a")
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
        "                    OwnCheckEnter(\"" + answer + "\");\n"
        "                }\n"
    )
    file.close()


def store_radio(file_name, question, answers, correct_answer, question_number, language):
    texts = question.split("\\n")
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
        "                    PrintLine(\"" + Translations.choose_answer(language) + "\");\n"
    )
    for text in texts:
        file.write(
            "                    PrintLine(\"" + text + "\");\n"
        )
    file.write(
        "                    CreateInputradio(" + str(answers) + ");\n"
        "                }\n"
    )
    file.close()
    file = open(file_name + ".check", "a")
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
        "                    OwnCheckRadio(\"" + str(correct_answer) + "\");\n"
        "                }\n"
    )
    file.close()


def store_explain(file_name, texts, question_number, language):
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
        "                    PrintLine(\"" + Translations.read_info(language) + "\");\n"
    )
    for text in texts:
        file.write(
            "                    PrintLine(\"" + text + "\");\n"
        )
    file.write(
        "                }\n"
    )
    file.close()
    if question_number == 0:
        file = open(file_name + ".check", "a")
        file.write(
            "                if (question == 0)\n"
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


def delete_storing_files(file_name):
    os.remove(file_name + ".change")
    os.remove(file_name + ".check")
