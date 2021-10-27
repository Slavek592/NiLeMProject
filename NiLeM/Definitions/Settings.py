#!/usr/bin/python3
import sqlite3


def create_database():
    connection = sqlite3.connect("Data/Local.db")
    connection.execute("CREATE TABLE Settings ("
                       "Setting TEXT PRIMARY KEY NOT NULL,"
                       "Value TEXT);")
    connection.execute("INSERT INTO Settings "
                       "VALUES (\"mode\", \"dark\");")
    connection.commit()
    connection.close()


def get_mode():
    connection = sqlite3.connect("Data/Local.db")
    answer = connection.execute("SELECT * FROM Settings WHERE Setting = 'mode';")
    mode = ""
    for row in answer:
        mode = row[1]
    connection.close()
    return mode


def change_mode(new_mode):
    connection = sqlite3.connect("Data/Local.db")
    connection.execute("UPDATE Settings "
                       "SET Value = '" + new_mode + "' "
                       "WHERE Setting = 'mode';")
    connection.commit()
    connection.close()
