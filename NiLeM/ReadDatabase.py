#!/usr/bin/python3
import sqlite3


def get_subject_lessons(subject, language):
    connection = sqlite3.connect("Data/" + language.capitalize() + ".db")
    answer = connection.execute("SELECT * FROM Lessons WHERE Subject = \"" + subject.capitalize() + "\";")
    lessons = []
    lesson_ids = []
    for row in answer:
        lesson_ids.append(row[0])
        lessons.append(row[2])
    connection.close()
    return [lessons, lesson_ids]


def get_lesson_questions(language, lesson_id):
    connection = sqlite3.connect("Data/" + language.capitalize() + ".db")
    enter_answer = connection.execute("SELECT * FROM Enter WHERE LessonID = " + str(lesson_id) + ";")
    radio_answer = connection.execute("SELECT * FROM Radio WHERE LessonID = " + str(lesson_id) + ";")
    explain_answer = connection.execute("SELECT * FROM Explain WHERE LessonID = " + str(lesson_id) + ";")
    questions = {}
    for row in enter_answer:
        questions[row[1]] = ["enter", row[2], row[3]]
    for row in radio_answer:
        questions[row[1]] = ["radio", row[2], row[3], row[4]]
    for row in explain_answer:
        questions[row[1]] = ["explain", row[2]]
    return questions
