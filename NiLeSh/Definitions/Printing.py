#!/usr/bin/python3
import sqlite3
import os


def create_database(language):
    connection = sqlite3.connect("NiLeM/Databases/" + language.capitalize() + ".db")
    connection.execute("CREATE TABLE Lessons ("
                       "ID INT PRIMARY KEY NOT NULL,"
                       "Subject CHAR(12) NOT NULL,"
                       "Name TEXT NOT NULL);")
    connection.execute("CREATE TABLE Explain ("
                       "LessonID REFERENCES Lessons(ID),"
                       "QuestionNumber INT,"
                       "String TEXT,"
                       "PRIMARY KEY(LessonID, QuestionNumber));")
    connection.execute("CREATE TABLE Enter ("
                       "LessonID REFERENCES Lessons(ID),"
                       "QuestionNumber INT,"
                       "Question TEXT,"
                       "Answer TEXT,"
                       "PRIMARY KEY(LessonID, QuestionNumber));")
    connection.execute("CREATE TABLE Radio ("
                       "LessonID REFERENCES Lessons(ID),"
                       "QuestionNumber INT,"
                       "Question TEXT,"
                       "Answers TEXT,"
                       "Answer INT,"
                       "PRIMARY KEY(LessonID, QuestionNumber));")
    connection.close()


def delete_database(language):
    os.remove("NiLeM/Databases/" + language.capitalize() + ".db")


def add_lesson(language, subject, name):
    name = name.replace("\\\"", "").replace("\"", "")
    try:
        connection = sqlite3.connect("NiLeM/Databases/" + language.capitalize() + ".db")
        result = connection.execute("SELECT MAX(ID) FROM Lessons;")
        new_id = 0
        try:
            for row in result:
                new_id = int(row[0]) + 1
        except TypeError:
            new_id = 0
        connection.execute("INSERT INTO Lessons (ID, Subject, Name)"
                           "VALUES (" + str(new_id) + ", \"" + subject.capitalize() + "\", \"" + name + "\");")
        connection.commit()
        connection.close()
        return new_id
    except sqlite3.OperationalError:
        return -1


def add_enter(language, lesson_id, number, question, answer):
    question = question.replace("\\\"", "").replace("\"", "")
    answer = answer.replace("\\\"", "").replace("\"", "")
    connection = sqlite3.connect("NiLeM/Databases/" + language.capitalize() + ".db")
    connection.execute("INSERT INTO Enter (LessonID, QuestionNumber, Question, Answer)"
                       "VALUES (" + str(lesson_id) + ", " + str(number)
                       + ", \"" + question + "\", \"" + answer + "\");")
    connection.commit()
    connection.close()


def add_radio(language, lesson_id, number, question, answers, answer):
    question = question.replace("\\\"", "").replace("\"", "")
    answers = answers.replace("\\\"", "").replace("\"", "")
    answer = answer.replace("\\\"", "").replace("\"", "")
    connection = sqlite3.connect("NiLeM/Databases/" + language.capitalize() + ".db")
    connection.execute("INSERT INTO Radio (LessonID, QuestionNumber, Question, Answers, Answer)"
                       "VALUES (" + str(lesson_id) + ", " + str(number)
                       + ", \"" + question + "\", \"" + answers + "\", " + answer + ");")
    connection.commit()
    connection.close()


def add_explain(language, lesson_id, number, string):
    string = string.replace("\\\"", "").replace("\"", "")
    connection = sqlite3.connect("NiLeM/Databases/" + language.capitalize() + ".db")
    connection.execute("INSERT INTO Explain (LessonID, QuestionNumber, String)"
                       "VALUES (" + str(lesson_id) + ", " + str(number) + ", \"" + string + "\");")
    connection.commit()
    connection.close()
