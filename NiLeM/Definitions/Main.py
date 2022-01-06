#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler


class NiLeMServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.split("/")
        if len(path) > 0:
            if path[1] in ["Math", "Physics", "Chemistry", "Biology",
                           "Geography", "History", "English", "Czech",
                           "Russian", "German", "French", "Spanish",
                           "Literature", "Music", "Art", "Informatics"]:
                if len(path) == 3:
                    self.subject_menu()
                else:
                    self.lesson()
            else:
                try:
                    self.send_file()
                except:
                    self.not_found()
        else:
            self.not_found()

    from .Answers import not_found, send_file, subject_menu, lesson
