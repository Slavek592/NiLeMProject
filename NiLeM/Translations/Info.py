#!/usr/bin/python3


def about_string(language, part):
    if part == 0:
        if language == "english":
            return "Main author: Viacheslav Nikiforov"
        elif language == "czech":
            return "Hlavní autor: Viacheslav Nikiforov"
        elif language == "russian":
            return "Главный автор: Вячеслав Никифоров"
        elif language == "german":
            return "Hauptautor: Viacheslav Nikiforov"
        elif language == "french":
            return "Auteur principal : Viacheslav Nikiforov"
        elif language == "spanish":
            return "Autor principal: Viacheslav Nikiforov"
    elif part == 1:
        if language == "english":
            return "Start of work: 2021"
        elif language == "czech":
            return "Začátek práce: 2021"
        elif language == "russian":
            return "Начало работы: 2021 г."
        elif language == "german":
            return "Arbeitsbeginn: 2021"
        elif language == "french":
            return "Début des travaux : 2021"
        elif language == "spanish":
            return "Inicio de obra: 2021"
    elif part == 2:
        if language == "english":
            return "Official URL: https://github.com/Slavek592/NiLeMProject"
        elif language == "czech":
            return "Oficiální URL: https://github.com/Slavek592/NiLeMProject"
        elif language == "russian":
            return "Официальный URL: https://github.com/Slavek592/NiLeMProject"
        elif language == "german":
            return " Offizielle URL: https://github.com/Slavek592/NiLeMProject"
        elif language == "french":
            return "URL officielle : https://github.com/Slavek592/NiLeMProject"
        elif language == "spanish":
            return "URL oficial: https://github.com/Slavek592/NiLeMProject"
    elif part == 3:
        if language == "english":
            return " License: GNU GPL3 (free to use and redistribute)"
        elif language == "czech":
            return "Licence: GNU GPL3 (volně k použití a redistribuci)"
        elif language == "russian":
            return "Лицензия: GNU GPL3 (свободно для использования и распространения)"
        elif language == "german":
            return "Lizenz: GNU GPL3 (kostenlos zu verwenden und weiterzugeben) "
        elif language == "french":
            return "Licence: GNU GPL3 (gratuit à utiliser et à redistribuer)"
        elif language == "spanish":
            return "Licencia: GNU GPL3 (gratis para usar y redistribuir)"
