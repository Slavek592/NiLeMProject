#!/usr/bin/python3
try:
    import requests
except:
    print("Unable update databases. Try installing requests.")


def update(language):
    try:
        response = requests.get(
            "https://raw.github.com/Slavek592/NiLeMProject/desktop/Data/"
            + language.capitalize() + ".db", verify=False, headers={})
        if response.status_code == 200:
            file = open("Data/" + language.capitalize() + ".db", "wb")
            file.write(response.content)
    except:
        print("I am sorry, it was not successful. Try checking internet connection.")


def complete_update():
    languages = ["english", "czech", "russian", "german", "french", "spanish"]
    for language in languages:
        update(language)
