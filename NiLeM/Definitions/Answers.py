#!/usr/bin/python3
from . import ReadDatabase
from . import Translations


def not_found(self):
    self.send_response(404)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Nikiforov's Learning Machine</title>"
        "<meta charset=\"utf-8\"/>"
        "</head>"
        "<body>"
        "<h1>I am sorry, this page was not found.</h1>"
        "</body>"
        "</html>",
        "utf-8"
    ))


def send_file(self):
    file = open(self.path[1:], "rb")
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(file.read())


def subject_menu(self):
    path = self.path.split("/")
    if "-" not in path[2]:
        language = "english"
    else:
        language = ""
        found = False
        for letter in path[2]:
            if letter == "-":
                found = True
            elif letter == ".":
                break
            elif found:
                language += letter
    [lesson_names, lesson_ids] = ReadDatabase.get_subject_lessons(path[1], language)
    lessons = ""
    for lesson in range(len(lesson_names)):
        lessons += "<button onclick=\"window.location.href='" + language.capitalize() + \
                   "/" + str(lesson_ids[lesson]) + "';\">" + lesson_names[lesson] + "</button>"
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Nikiforov's Learning Machine</title>"
        "<meta charset=\"utf-8\"/>"
        "<link rel=\"stylesheet\" href=\"../Core/styles.css\">"
        "<link rel=\"icon\" href=\"../Pictures/Physics.jpg\">"
        "<script src=\"../Core/styler.js\"></script>"
        "</head>"
        "<body>"
        "<h1>" + Translations.subject_name(path[1].lower(), language.lower()) + "</h1>"
        + lessons +
        "<p><a href=\"../Main" + Translations.file_language(language.lower())
        + ".html\">" + Translations.to_main(language.lower()) + "</a></p>"
        "</body>"
        "</html>",
        "utf-8"))


def lesson(self):
    path = self.path.split("/")
    language = path[2].lower()
    questions = ReadDatabase.get_lesson_questions(language, int(path[3]))
    script = "question = -1;\n" \
             "function OwnCheckEnter(correct_answer)\n" \
             "{\n" \
             "CheckEnter(\"" + Translations.good(language) + "\", \""\
             + Translations.bad(language) + "\", correct_answer)\n" \
             "}\n" \
             "function OwnCheckRadio(correct_answer)\n" \
             "{\n" \
             "CheckRadio(\"" + Translations.good(language) + "\", \""\
             + Translations.bad(language) + "\", correct_answer)\n" \
             "}\n"
    script += "function ChangeContent()\n" \
              "{\n" \
              "document.getElementById(\"q\").innerHTML = \"\";\n" \
              "document.getElementById(\"c\").innerHTML = \""\
              + Translations.no_checked_answer(language) + "\";\n" \
              "question ++;\n"
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0)\n{\n"
        else:
            script += "else if (question == " + str(question) + ")\n{\n"
        for line in questions[question][1].split("\\n"):
            script += "PrintLine(\"" + line + "\");\n"
        if questions[question][0] == "enter":
            script += "CreateInputbox();\n"
        elif questions[question][0] == "radio":
            script += "CreateInputradio(" + str(questions[question][2].split("|")) + ");\n"
        script += "}\n"
    script += "else\n" \
              "{\n" \
              "PrintLine(\"" + Translations.congrats(language) + "\");" \
              "}\n" \
              "}\n" \
              "function Check()\n" \
              "{\n"
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0)\n{\n"
        else:
            script += "else if (question == " + str(question) + ")\n{\n"
        if questions[question][0] == "enter":
            script += "OwnCheckEnter(\"" + questions[question][2] + "\");\n"
        elif questions[question][0] == "radio":
            script += "OwnCheckRadio(\"" + str(questions[question][3]) + "\");\n"
        script += "}\n"
    script += "}\n" \
              "function Show()\n" \
              "{\n"
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0)\n{\n"
        else:
            script += "else if (question == " + str(question) + ")\n{\n"
        if questions[question][0] == "enter":
            script += "ShowCorrect(\"" + questions[question][2] + "\");\n"
        elif questions[question][0] == "radio":
            script += "ShowCorrect(\"" + questions[question][2]\
                .split("|")[questions[question][3]] + "\");\n"
        script += "}\n"
    script += "}\n"
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Nikiforov's Learning Machine</title>"
        "<meta charset=\"utf-8\"/>"
        "<link rel=\"stylesheet\" href=\"../../Core/styles.css\">"
        "<link rel=\"icon\" href=\"../../Pictures/Physics.jpg\">"
        "<script src=\"../../Core/default.js\"></script>"
        "<script src=\"../../Core/styler.js\"></script>"
        "<script>"
        + script +
        "</script>"
        "</head>"
        "<body>"
        "<h1>" + ReadDatabase.get_lesson_name(language, int(path[3])) + "</h1>"
        "<div id=\"q\">" + Translations.click_on_next(language) + "</div>"
        "<p>"
        "<button type=\"button\" onclick=\"ChangeContent()\">"
        + Translations.button_next(language) + "</button>"
        "<button type=\"button\" onclick=\"Check()\">"
        + Translations.button_check(language) + "</button>"
        "<button type=\"button\" onclick=\"Show()\">"
        + Translations.button_show(language) + "</button>"
        "</p>"
        "<p id=\"c\">" + Translations.no_checked_answer(language) + "</p>"
        "<p><a href=\"../" +
        path[1] + Translations.file_language(language)
        + ".html\">" + Translations.on_subject_menu(path[1].lower(), language)
        + "</a></p>"
        "</body>"
        "</html>",
        "utf-8"
    ))
