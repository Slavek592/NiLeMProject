#!/usr/bin/python3
import requests


def update(language):
    response = requests.get(
        "https://raw.github.com/Slavek592/NiLeMProject/desktop/Data/"
        + language.capitalize() + ".db", verify=False, headers={})
    if response.status_code == 200:
        file = open("Data/" + language.capitalize() + ".db", "wb")
        file.write(response.content)


def complete_update():
    languages = ["english", "czech", "russian", "german", "french", "spanish"]
    for language in languages:
        update(language)
