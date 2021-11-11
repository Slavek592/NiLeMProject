#!/usr/bin/python3
import sqlite3


def create_database():
    connection = sqlite3.connect("Data/Local.db")
    connection.execute("CREATE TABLE Settings ("
                       "Setting TEXT PRIMARY KEY NOT NULL,"
                       "Value TEXT);")
    connection.execute("INSERT INTO Settings "
                       "VALUES (\"language\", \"english\");")
    connection.execute("INSERT INTO Settings "
                       "VALUES (\"mode\", \"dark\");")
    connection.commit()
    connection.close()


def get_setting(setting):
    connection = sqlite3.connect("Data/Local.db")
    answer = connection.execute("SELECT * FROM Settings WHERE Setting = '" + setting + "';")
    result = ""
    for row in answer:
        result = row[1]
    connection.close()
    return result


def change_setting(setting, new_mode):
    connection = sqlite3.connect("Data/Local.db")
    connection.execute("UPDATE Settings "
                       "SET Value = '" + new_mode + "' "
                       "WHERE Setting = '" + setting + "';")
    connection.commit()
    connection.close()
