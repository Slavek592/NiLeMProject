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
        "<!--<link rel=\"stylesheet\" href=\"../Core/styles.css\">-->"
        "<link rel=\"icon\" href=\"../Pictures/Physics.jpg\">"
        "<script src=\"../Core/styler.js\"></script>"
        "</head>"
        "<body>"
        "<h1>" + Translations.subject_name(path[1].lower(), language.lower()) + "</h1>"
        "<div style=\"margin-right: 100px; margin-left: 100px;\">" + lessons + "</div>"
        "<p><button onclick=\"window.location.href='../Core/Subjects"
        + Translations.file_language(language.lower()) + ".html';\">"
        "<p><img src=\"../Pictures/Back.jpg\" alt=\"Back\" class=\"image_big\"></p>"
        "<h3>" + Translations.to_main(language.lower()) + "</h3>"
        "</button></p>"
        "</body>"
        "</html>",
        "utf-8"))


def lesson(self):
    path = self.path.split("/")
    language = path[2].lower()
    questions = ReadDatabase.get_lesson_questions(language, int(path[3]))
    script = "var question = -1; " \
             "var correct_string = \"" + Translations.good(language) + "\"; "\
             "var incorrect_string = \"" + Translations.bad(language) + "\"; "
    script += "function ChangeContent() " \
              "{ " \
              "document.getElementById(\"q\").innerHTML = \"\"; " \
              "document.getElementById(\"c\").innerHTML = \"" \
              + Translations.no_checked_answer(language) + "\"; "
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0) { "
        else:
            script += "else if (question == " + str(question) + ") { "
        for line in questions[question][1].split("\\n"):
            script += "PrintLine(\"" + line + "\"); "
        if questions[question][0] == "enter":
            script += "CreateInputbox(); "
        elif questions[question][0] == "radio":
            script += "CreateInputradio(" + str(questions[question][2].split("|")) + "); "
        script += "} "
    script += "else { " \
              "PrintLine(\"" + Translations.congrats(language) + "\"); " \
              "} } function Check() { "
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0) { "
        else:
            script += "else if (question == " + str(question) + ") { "
        if questions[question][0] == "enter":
            script += "CheckEnter(\"" + questions[question][2] + "\"); "
        elif questions[question][0] == "radio":
            script += "CheckRadio(\"" + str(questions[question][3]) + "\"); "
        script += "} "
    script += "} " \
              "function Show() " \
              "{ "
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0) { "
        else:
            script += "else if (question == " + str(question) + ") { "
        if questions[question][0] == "enter":
            script += "ShowCorrect(\"" + questions[question][2] + "\"); "
        elif questions[question][0] == "radio":
            script += "ShowCorrect(\"" + questions[question][2] \
                .split("|")[questions[question][3]] + "\"); "
        script += "} "
    script += "} "
    lesson_name = ReadDatabase.get_lesson_name(language, int(path[3]))
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Nikiforov's Learning Machine</title>"
        "<meta charset=\"utf-8\"/>"
        "<!--<link rel=\"stylesheet\" href=\"../../Core/styles.css\">-->"
        "<link rel=\"icon\" href=\"../../Pictures/Physics.jpg\">"
        "<script src=\"../../Core/default.js\"></script>"
        "<script src=\"../../Core/styler.js\"></script>"
        "<script>"
        + script +
        "</script>"
        "</head>"
        "<body>"
        "<h1>" + lesson_name + "</h1>"
        "<div id=\"q\"><p>" + Translations.click_on_next(language) + "</p></div>"
        "<p>"
        "<button type=\"button\" onclick=\"Previous()\">"
        + Translations.button_previous(language) + "</button>"
        "<button type=\"button\" onclick=\"Check()\">"
        + Translations.button_check(language) + "</button>"
        "<button type=\"button\" onclick=\"Show()\">"
        + Translations.button_show(language) + "</button>"
        "<button type=\"button\" onclick=\"Next()\">"
        + Translations.button_next(language) + "</button>"
        "</p>"
        "<p><a href=\"" + self.path + "/download\" download=\""
        + lesson_name + ".html\">" + Translations.download_lesson(language) + "</a></p>"
        "<p id=\"c\">" + Translations.no_checked_answer(language) + "</p>"
        "<p><a href=\"../" +
        path[1] + Translations.file_language(language)
        + ".html\">" + Translations.on_subject_menu(path[1].lower(), language)
        + "</a></p>"
        "</body>"
        "</html>",
        "utf-8"
    ))


def download_lesson(self):
    path = self.path.split("/")
    language = path[2].lower()
    questions = ReadDatabase.get_lesson_questions(language, int(path[3]))
    script = "var question = -1; " \
             "function CheckEnter(correct_answer) { " \
             "if (document.getElementById(\"ans\").value == correct_answer) { " \
             "document.getElementById(\"c\").innerHTML = \"" \
             + Translations.good(language) + "\"; " \
             "} else { " \
             "document.getElementById(\"c\").innerHTML = \"" \
             + Translations.bad(language) + "\"; " \
             "} } function CheckRadio(correct_answer) " \
             "{ var ele = document.getElementsByName('ans'); " \
             "for (i = 0; i < ele.length; i++) { " \
             "if (ele[i].checked) { " \
             "if (i == correct_answer) { " \
             "document.getElementById(\"c\").innerHTML = \""\
             + Translations.good(language) + "\"; " \
             "} else { " \
             "document.getElementById(\"c\").innerHTML = \""\
             + Translations.bad(language) + "\"; " \
             "} } } } function PrintLine(line) { " \
             "var text = document.createElement(\"p\"); " \
             "text.appendChild(document.createTextNode(line)); " \
             "document.getElementById(\"q\").appendChild(text); " \
             "} function CreateInputbox() { " \
             "var inputplace = document.createElement(\"p\"); " \
             "var inputbox = document.createElement(\"input\"); " \
             "inputbox.type = \"text\"; " \
             "inputbox.id = \"ans\"; " \
             "inputbox.name = \"ans\"; " \
             "inputplace.appendChild(inputbox); " \
             "document.getElementById(\"q\").appendChild(inputplace); " \
             "} function CreateInputradio(answers) { " \
             "var inputplace = document.createElement(\"p\"); " \
             "inputplace.id = \"inp\"; " \
             "for (let i = 0; i < answers.length; i++) { " \
             "var inputradio = document.createElement(\"input\"); " \
             "inputradio.type = \"radio\"; " \
             "inputradio.id = \"ans\"; " \
             "inputradio.name = \"ans\"; " \
             "inputplace.appendChild(inputradio); " \
             "inputplace.appendChild(document.createTextNode(answers[i])); " \
             "} document.getElementById(\"q\").appendChild(inputplace); " \
             "} function ShowCorrect(answer) {" \
             "document.getElementById(\"c\").innerHTML = answer; " \
             "} function Next() { " \
             "question ++; " \
             "ChangeContent(); " \
             "} function Previous() { " \
             "if (question > 0) { " \
             "question --; " \
             "ChangeContent(); " \
             "} } "
    script += "function ChangeContent() " \
              "{ " \
              "document.getElementById(\"q\").innerHTML = \"\"; " \
              "document.getElementById(\"c\").innerHTML = \"" \
              + Translations.no_checked_answer(language) + "\"; "
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0) { "
        else:
            script += "else if (question == " + str(question) + ") { "
        for line in questions[question][1].split("\\n"):
            script += "PrintLine(\"" + line + "\"); "
        if questions[question][0] == "enter":
            script += "CreateInputbox(); "
        elif questions[question][0] == "radio":
            script += "CreateInputradio(" + str(questions[question][2].split("|")) + "); "
        script += "} "
    script += "else { " \
              "PrintLine(\"" + Translations.congrats(language) + "\"); " \
              "} } function Check() { "
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0) { "
        else:
            script += "else if (question == " + str(question) + ") { "
        if questions[question][0] == "enter":
            script += "CheckEnter(\"" + questions[question][2] + "\"); "
        elif questions[question][0] == "radio":
            script += "CheckRadio(\"" + str(questions[question][3]) + "\"); "
        script += "} "
    script += "} " \
              "function Show() " \
              "{ "
    for question in range(len(questions)):
        if question == 0:
            script += "if (question == 0) { "
        else:
            script += "else if (question == " + str(question) + ") { "
        if questions[question][0] == "enter":
            script += "ShowCorrect(\"" + questions[question][2] + "\"); "
        elif questions[question][0] == "radio":
            script += "ShowCorrect(\"" + questions[question][2] \
                .split("|")[questions[question][3]] + "\"); "
        script += "} "
    script += "} "
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes(
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Nikiforov's Learning Machine</title>"
        "<meta charset=\"utf-8\"/>"
        "<style>"
        "body { "
        "background-color: black; "
        "color: white; } "
        "</style>"
        "<script>"
        + script +
        "</script>"
        "</head>"
        "<body>"
        "<h1>" + ReadDatabase.get_lesson_name(language, int(path[3])) + "</h1>"
        "<div id=\"q\"><p>" + Translations.click_on_next(language) + "</p></div>"
        "<p>"
        "<button type=\"button\" onclick=\"Previous()\">"
        + Translations.button_previous(language) + "</button>"
        "<button type=\"button\" onclick=\"Check()\">"
        + Translations.button_check(language) + "</button>"
        "<button type=\"button\" onclick=\"Show()\">"
        + Translations.button_show(language) + "</button>"
        "<button type=\"button\" onclick=\"Next()\">"
        + Translations.button_next(language) + "</button>"
        "</p>"
        "<p id=\"c\">" + Translations.no_checked_answer(language) + "</p>"
        "</body>"
        "</html>",
        "utf-8"
    ))


def welcome(self):
    file = open("NiLeM.html", "rb")
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(file.read())
