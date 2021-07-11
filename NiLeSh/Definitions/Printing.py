#!/usr/bin/python3


def print_header(file):
    file.write(
        "<!DOCTYPE html>\n"
        "<html>\n"
        "    <head>\n"
        "        <title>Nikiforov's Learning Machine</title>\n"
        "        <meta charset=\"utf-8\"/>\n"
        "        <style>\n"
        "            body {\n"
        "                background-color: black;\n"
        "                color: white;\n"
        "            }\n"
        "        </style>\n"
        "    </head>\n"
        "\n"
        "    <body>\n"
    )


def print_start_of_body(file, name, language, subject, length_of_path, case):
    file.write(
        "        <h1>" + name + "</h1>\n"
    )
    if language == "english":
        if case != "menu":
            file.write(
                "        <div id=\"q\" class=\"container\">Click on the button \"Next\" to start.</div>\n"
                "        <p>\n"
                "            <button type=\"button\" onclick=\"ChangeContent()\">Next</button>\n"
                "            <button type=\"button\" onclick=\"Check()\">Check answer</button>\n"
                "        </p>\n"
                "        <p id=\"c\">There is no any checked answer.</p>\n"
            )
        if case == "menu":
            file.write(
                "        <p><a href=\"../Main.html\">Back to Main menu</a></p>\n"
            )
        elif subject == "math":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Math.html\">Back to Math menu</a></p>\n"
            file.write(string)
        elif subject == "physics":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Physics.html\">Back to Physics menu</a></p>\n"
            file.write(string)
        elif subject == "chemistry":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Chemistry.html\">Back to Chemistry menu</a></p>\n"
            file.write(string)
        elif subject == "biology":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Biology.html\">Back to Biology menu</a></p>\n"
            file.write(string)
        elif subject == "geography":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Geography.html\">Back to Geography menu</a></p>\n"
            file.write(string)
        elif subject == "history":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "History.html\">Back to History menu</a></p>\n"
            file.write(string)
        elif subject == "english":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "English.html\">Back to English menu</a></p>\n"
            file.write(string)
        elif subject == "german":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "German.html\">Back to German menu</a></p>\n"
            file.write(string)
        elif subject == "czech":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Czech.html\">Back to Czech menu</a></p>\n"
            file.write(string)
        elif subject == "russian":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Russian.html\">Back to Russian menu</a></p>\n"
            file.write(string)
        elif subject == "french":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "French.html\">Back to French menu</a></p>\n"
            file.write(string)
        elif subject == "spanish":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Spanish.html\">Back to Spanish menu</a></p>\n"
            file.write(string)
    elif language == "czech":
        if case != "menu":
            file.write(
                "        <div id=\"q\" class=\"container\">Klikněte na tlačítko \"Další\" pro začátek.</div>\n"
                "        <p>\n"
                "            <button type=\"button\" onclick=\"ChangeContent()\">Další</button>\n"
                "            <button type=\"button\" onclick=\"Check()\">Zkontrolovat</button>\n"
                "        </p>\n"
                "        <p id=\"c\">Není zde žádná zkontrolovaná odpověď.</p>\n"
            )
        if case == "menu":
            file.write(
                "        <p><a href=\"../Main-czech.html\">Zpátky na hlavní menu</a></p>\n"
            )
        elif subject == "math":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Math-czech.html\">Zpátky na menu matematiky</a></p>\n"
            file.write(string)
        elif subject == "physics":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Physics-czech.html\">Zpátky na menu fyziky</a></p>\n"
            file.write(string)
        elif subject == "chemistry":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Chemistry-czech.html\">Zpátky na menu chemie</a></p>\n"
            file.write(string)
        elif subject == "biology":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Biology-czech.html\">Zpátky na menu biologie</a></p>\n"
            file.write(string)
        elif subject == "geography":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Geography-czech.html\">Zpátky na menu zeměpisu</a></p>\n"
            file.write(string)
        elif subject == "history":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "History-czech.html\">Zpátky na menu dějepisu</a></p>\n"
            file.write(string)
        elif subject == "english":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "English-czech.html\">Zpátky na menu angličtiny</a></p>\n"
            file.write(string)
        elif subject == "german":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "German-czech.html\">Zpátky na menu němčiny</a></p>\n"
            file.write(string)
        elif subject == "czech":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Czech-czech.html\">Zpátky na menu češtiny</a></p>\n"
            file.write(string)
        elif subject == "russian":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Russian-czech.html\">Zpátky na menu ruštiny</a></p>\n"
            file.write(string)
        elif subject == "french":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "French-czech.html\">Zpátky na menu francouzštiny</a></p>\n"
            file.write(string)
        elif subject == "spanish":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Spanish-czech.html\">Zpátky na menu španělštiny</a></p>\n"
            file.write(string)
    elif language == "russian":
        if case != "menu":
            file.write(
                "        <div id=\"q\" class=\"container\">Нажмите на кнопку \"Дальше\", чтобы начать.</div>\n"
                "        <p>\n"
                "            <button type=\"button\" onclick=\"ChangeContent()\">Дальше</button>\n"
                "            <button type=\"button\" onclick=\"Check()\">Проверить</button>\n"
                "        </p>\n"
                "        <p id=\"c\">Здесь нет никакого исправленного ответа.</p>\n"
            )
        if case == "menu":
            file.write(
                "        <p><a href=\"../Main-russian.html\">Обратно на главное меню</a></p>\n"
            )
        elif subject == "math":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Math-russian.html\">Обратно на меню математики</a></p>\n"
            file.write(string)
        elif subject == "physics":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Physics-russian.html\">Обратно на меню физики</a></p>\n"
            file.write(string)
        elif subject == "chemistry":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Chemistry-russian.html\">Обратно на меню химии</a></p>\n"
            file.write(string)
        elif subject == "biology":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Biology-russian.html\">Обратно на меню биологии</a></p>\n"
            file.write(string)
        elif subject == "geography":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Geography-russian.html\">Обратно на меню географии</a></p>\n"
            file.write(string)
        elif subject == "history":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "History-russian.html\">Обратно на меню истории</a></p>\n"
            file.write(string)
        elif subject == "english":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "English-russian.html\">Обратно на меню английского</a></p>\n"
            file.write(string)
        elif subject == "german":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "German-russian.html\">Обратно на меню немецкого</a></p>\n"
            file.write(string)
        elif subject == "czech":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Czech-russian.html\">Обратно на меню чешского</a></p>\n"
            file.write(string)
        elif subject == "russian":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Russian-russian.html\">Обратно на меню русского</a></p>\n"
            file.write(string)
        elif subject == "french":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "French-russian.html\">Обратно на меню французского</a></p>\n"
            file.write(string)
        elif subject == "spanish":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Spanish-russian.html\">Обратно на меню испанского</a></p>\n"
            file.write(string)
    elif language == "german":
        if case != "menu":
            file.write(
                "        <div id=\"q\" class=\"container\">Klicken Sie den Knopf \"Nächster\" für fortzufahren.</div>\n"
                "        <p>\n"
                "            <button type=\"button\" onclick=\"ChangeContent()\">Nächster</button>\n"
                "            <button type=\"button\" onclick=\"Check()\">Prüfen</button>\n"
                "        </p>\n"
                "        <p id=\"c\">Es gibt keine geprüfte antwort.</p>\n"
            )
        if case == "menu":
            file.write(
                "        <p><a href=\"../Main-german.html\">Zurück zum Hauptmenü</a></p>\n"
            )
        elif subject == "math":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Math-german.html\">Zurück zum Mathe-Menü</a></p>\n"
            file.write(string)
        elif subject == "physics":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Physics-german.html\">Zurück zum Physik-Menü</a></p>\n"
            file.write(string)
        elif subject == "chemistry":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Chemistry-german.html\">Zurück zum Chemie-Menü</a></p>\n"
            file.write(string)
        elif subject == "biology":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Biology-german.html\">Zurück zum Biologie-Menü</a></p>\n"
            file.write(string)
        elif subject == "geography":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Geography-german.html\">Zurück zum Geografie-Menü</a></p>\n"
            file.write(string)
        elif subject == "history":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "History-german.html\">Zurück zum Geschichte-Menü</a></p>\n"
            file.write(string)
        elif subject == "english":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "English-german.html\">Zurück zum Englisch-Menü</a></p>\n"
            file.write(string)
        elif subject == "german":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "German-german.html\">Zurück zum Deutsch-Menü</a></p>\n"
            file.write(string)
        elif subject == "czech":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Czech-german.html\">Zurück zum Tschechisch-Menü</a></p>\n"
            file.write(string)
        elif subject == "russian":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Russian-german.html\">Zurück zum Russisch-Menü</a></p>\n"
            file.write(string)
        elif subject == "french":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "French-german.html\">Zurück zum Französisch-Menü</a></p>\n"
            file.write(string)
        elif subject == "spanish":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Spanish-german.html\">Zurück zum Spanisch-Menü</a></p>\n"
            file.write(string)
    elif language == "french":
        if case != "menu":
            file.write(
                "        <div id=\"q\" class=\"container\">Cliquez sur le bouton \"Suivant\" pour commencer.</div>\n"
                "        <p>\n"
                "            <button type=\"button\" onclick=\"ChangeContent()\">Suivant</button>\n"
                "            <button type=\"button\" onclick=\"Check()\">Vérifier</button>\n"
                "        </p>\n"
                "        <p id=\"c\">Il n'y a pas de réponse vérifiée.</p>\n"
            )
        if case == "menu":
            file.write(
                "        <p><a href=\"../Main-french.html\">Retour au menu principal</a></p>\n"
            )
        elif subject == "math":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Math-french.html\">Retour au menu mathématique</a></p>\n"
            file.write(string)
        elif subject == "physics":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Physics-french.html\">Retour au menu physique</a></p>\n"
            file.write(string)
        elif subject == "chemistry":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Chemistry-french.html\">Retour au menu chimie</a></p>\n"
            file.write(string)
        elif subject == "biology":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Biology-french.html\">Retour au menu biologie</a></p>\n"
            file.write(string)
        elif subject == "geography":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Geography-french.html\">Retour au menu géographie</a></p>\n"
            file.write(string)
        elif subject == "history":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "History-french.html\">Retour au menu historique</a></p>\n"
            file.write(string)
        elif subject == "english":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "English-french.html\">Retour au menu anglais</a></p>\n"
            file.write(string)
        elif subject == "german":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "German-french.html\">Retour au menu allemand</a></p>\n"
            file.write(string)
        elif subject == "czech":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Czech-french.html\">Retour au menu tchèque</a></p>\n"
            file.write(string)
        elif subject == "russian":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Russian-french.html\">Retour au menu russe</a></p>\n"
            file.write(string)
        elif subject == "french":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "French-french.html\">Retour au menu français</a></p>\n"
            file.write(string)
        elif subject == "spanish":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Spanish-french.html\">Retour au menu espagnol</a></p>\n"
            file.write(string)
    elif language == "spanish":
        if case != "menu":
            file.write(
                "        <div id=\"q\" class=\"container\">Haga clic en el botón \"Siguiente\" para comenzar.</div>\n"
                "        <p>\n"
                "            <button type=\"button\" onclick=\"ChangeContent()\">Siguiente</button>\n"
                "            <button type=\"button\" onclick=\"Check()\">Checar respuesta</button>\n"
                "        </p>\n"
                "        <p id=\"c\">No hay ninguna respuesta marcada.</p>\n"
            )
        if case == "menu":
            file.write(
                "        <p><a href=\"../Main-spanish.html\">Volver al menú principal</a></p>\n"
            )
        elif subject == "math":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Math-spanish.html\">Volver al menú de matemáticas</a></p>\n"
            file.write(string)
        elif subject == "physics":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Physics-spanish.html\">Volver al menú de Física</a></p>\n"
            file.write(string)
        elif subject == "chemistry":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Chemistry-spanish.html\">Volver al menú de Química</a></p>\n"
            file.write(string)
        elif subject == "biology":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Biology-spanish.html\">Volver al menú de Biología</a></p>\n"
            file.write(string)
        elif subject == "geography":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Geography-spanish.html\">Volver al menú Geografía</a></p>\n"
            file.write(string)
        elif subject == "history":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "History-spanish.html\">Volver al menú Historial</a></p>\n"
            file.write(string)
        elif subject == "english":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "English-spanish.html\">Volver al menú en inglés</a></p>\n"
            file.write(string)
        elif subject == "german":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "German-spanish.html\">Volver al menú alemán</a></p>\n"
            file.write(string)
        elif subject == "czech":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Czech-spanish.html\">Volver al menú checo</a></p>\n"
            file.write(string)
        elif subject == "russian":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Russian-spanish.html\">Volver al menú ruso</a></p>\n"
            file.write(string)
        elif subject == "french":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "French-spanish.html\">Volver al menú francés</a></p>\n"
            file.write(string)
        elif subject == "spanish":
            string = "        <p><a href=\""
            for i in range(length_of_path):
                string += "../"
            string += "Spanish-spanish.html\">Volver al menú en español</a></p>\n"


def print_start_of_script(file):
    file.write(
        "        <script>\n"
        "            question = 0;\n"
    )


def print_end_of_script(file):
    file.write(
        "        </script>\n"
    )


def print_end_of_body(file):
    file.write(
        "    </body>\n"
        "</html>\n"
    )


def create_storing_files(file_name, language):
    file = open(file_name + ".change", "w")
    if language == "english":
        file.write(
            "            function ChangeContent()\n"
            "            {\n"
            "                document.getElementById(\"q\").innerHTML = \"\";\n"
            "                document.getElementById(\"c\").innerHTML = \"There is no any checked answer.\";"
            "\n"
        )
    elif language == "czech":
        file.write(
            "            function ChangeContent()\n"
            "            {\n"
            "                document.getElementById(\"q\").innerHTML = \"\";\n"
            "                document.getElementById(\"c\").innerHTML = \"Není zde žádná zkontrolovaná odpověď.\";"
            "\n"
        )
    elif language == "russian":
        file.write(
            "            function ChangeContent()\n"
            "            {\n"
            "                document.getElementById(\"q\").innerHTML = \"\";\n"
            "                document.getElementById(\"c\").innerHTML = \"Здесь нет никакого исправленного ответа.\";"
            "\n"
        )
    elif language == "german":
        file.write(
            "            function ChangeContent()\n"
            "            {\n"
            "                document.getElementById(\"q\").innerHTML = \"\";\n"
            "                document.getElementById(\"c\").innerHTML = \"Es gibt keine geprüfte antwort.\";"
            "\n"
        )
    elif language == "french":
        file.write(
            "            function ChangeContent()\n"
            "            {\n"
            "                document.getElementById(\"q\").innerHTML = \"\";\n"
            "                document.getElementById(\"c\").innerHTML = \"Il n'y a pas de réponse vérifiée.\";"
            "\n"
        )
    elif language == "spanish":
        file.write(
            "            function ChangeContent()\n"
            "            {\n"
            "                document.getElementById(\"q\").innerHTML = \"\";\n"
            "                document.getElementById(\"c\").innerHTML = \"No hay ninguna respuesta marcada.\";"
            "\n"
        )
    file.close()
    file = open(file_name + ".check", "w")
    file.write(
        "            function Check()\n"
        "            {\n"
    )
    file.close()


def add_closings_to_storing_files(file_name, language):
    file = open(file_name + ".change", "a")
    if language == "english":
        file.write(
            "                else\n"
            "                {\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\""
            "Congratulation! You have ended this lesson.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "                }\n"
            "            }\n"
        )
    elif language == "czech":
        file.write(
            "                else\n"
            "                {\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\""
            "Gratuluji! Ukončil jste tuto lekci.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "                }\n"
            "            }\n"
        )
    elif language == "russian":
        file.write(
            "                else\n"
            "                {\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\""
            "Поздравляю! Вы закончили этот урок.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "                }\n"
            "            }\n"
        )
    elif language == "german":
        file.write(
            "                else\n"
            "                {\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\""
            "Herzlichen Glückwunsch! Sie haben diese Lektion beendet.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "                }\n"
            "            }\n"
        )
    elif language == "french":
        file.write(
            "                else\n"
            "                {\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\""
            "Félicitations ! Vous avez terminé cette leçon.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "                }\n"
            "            }\n"
        )
    elif language == "spanish":
        file.write(
            "                else\n"
            "                {\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\""
            "Enhorabuena Has terminado esta lección.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "                }\n"
            "            }\n"
        )
    file.close()
    file = open(file_name + ".check", "a")
    file.write(
        "            }\n"
    )
    file.close()


def store_enter(file_name, question, answer, question_number, language):
    file = open(file_name + ".change", "a")
    if question_number == 0:
        file.write(
            "                if (question == 0)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number) + ")\n"
        )
    if language == "english":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Enter answer.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    var inputbox = document.createElement(\"input\");\n"
            "                    inputbox.type = \"text\";\n"
            "                    inputbox.id = \"ans\";\n"
            "                    inputbox.name = \"ans\";\n"
            "                    inputplace.appendChild(inputbox);\n"
            "                    document.getElementById(\"q\").appendChild(inputplace);\n"
            "                }\n"
        )
    elif language == "czech":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Napište odpověď.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    var inputbox = document.createElement(\"input\");\n"
            "                    inputbox.type = \"text\";\n"
            "                    inputbox.id = \"ans\";\n"
            "                    inputbox.name = \"ans\";\n"
            "                    inputplace.appendChild(inputbox);\n"
            "                    document.getElementById(\"q\").appendChild(inputplace);\n"
            "                }\n"
        )
    elif language == "russian":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Напишите ответ.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    var inputbox = document.createElement(\"input\");\n"
            "                    inputbox.type = \"text\";\n"
            "                    inputbox.id = \"ans\";\n"
            "                    inputbox.name = \"ans\";\n"
            "                    inputplace.appendChild(inputbox);\n"
            "                    document.getElementById(\"q\").appendChild(inputplace);\n"
            "                }\n"
        )
    elif language == "german":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Antwort eingeben\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    var inputbox = document.createElement(\"input\");\n"
            "                    inputbox.type = \"text\";\n"
            "                    inputbox.id = \"ans\";\n"
            "                    inputbox.name = \"ans\";\n"
            "                    inputplace.appendChild(inputbox);\n"
            "                    document.getElementById(\"q\").appendChild(inputplace);\n"
            "                }\n"
        )
    elif language == "french":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Entrer la réponse\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    var inputbox = document.createElement(\"input\");\n"
            "                    inputbox.type = \"text\";\n"
            "                    inputbox.id = \"ans\";\n"
            "                    inputbox.name = \"ans\";\n"
            "                    inputplace.appendChild(inputbox);\n"
            "                    document.getElementById(\"q\").appendChild(inputplace);\n"
            "                }\n"
        )
    elif language == "spanish":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Ingrese la respuesta\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    var inputbox = document.createElement(\"input\");\n"
            "                    inputbox.type = \"text\";\n"
            "                    inputbox.id = \"ans\";\n"
            "                    inputbox.name = \"ans\";\n"
            "                    inputplace.appendChild(inputbox);\n"
            "                    document.getElementById(\"q\").appendChild(inputplace);\n"
            "                }\n"
        )
    file.close()
    file = open(file_name + ".check", "a")
    if question_number == 0:
        file.write(
            "                if (question == 1)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number + 1) + ")\n"
        )
    if language == "english":
        file.write(
            "                {\n"
            "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Correct.\";\n"
            "                    }\n"
            "                    else\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Incorrect.\";\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "czech":
        file.write(
            "                {\n"
            "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Správně.\";\n"
            "                    }\n"
            "                    else\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Nesprávně.\";\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "russian":
        file.write(
            "                {\n"
            "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Правильно.\";\n"
            "                    }\n"
            "                    else\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Не правильно.\";\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "german":
        file.write(
            "                {\n"
            "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Richtig.\";\n"
            "                    }\n"
            "                    else\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Falsch.\";\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "french":
        file.write(
            "                {\n"
            "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Corriger.\";\n"
            "                    }\n"
            "                    else\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Incorrect.\";\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "spanish":
        file.write(
            "                {\n"
            "                    if (document.getElementById(\"ans\").value == \"" + answer + "\")\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Correcto.\";\n"
            "                    }\n"
            "                    else\n"
            "                    {\n"
            "                        document.getElementById(\"c\").innerHTML = \"Incorrecto.\";\n"
            "                    }\n"
            "                }\n"
        )
    file.close()


def store_radio(file_name, question, answers, correct_answer, question_number, language):
    answers = answers.split("|")
    file = open(file_name + ".change", "a")
    if question_number == 0:
        file.write(
            "                if (question == 0)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number) + ")\n"
        )
    if language == "english":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Choose answer.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    inputplace.id = \"inp\";\n"
        )
    elif language == "czech":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Vyberte odpověď.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    inputplace.id = \"inp\";\n"
        )
    elif language == "russian":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Выберите ответ.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    inputplace.id = \"inp\";\n"
        )
    elif language == "german":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Antwort wählen.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    inputplace.id = \"inp\";\n"
        )
    elif language == "french":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Choisir la réponse.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    inputplace.id = \"inp\";\n"
        )
    elif language == "spanish":
        file.write(
            "                {\n"
            "                    question = " + str(question_number + 1) + ";\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"Elegir respuesta.\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + question + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
            "\n"
            "                    var inputplace = document.createElement(\"p\");\n"
            "                    inputplace.id = \"inp\";\n"
        )
    for answer in answers:
        file.write(
            "                    var inputradio = document.createElement(\"input\");\n"
            "                    inputradio.type = \"radio\";\n"
            "                    inputradio.id = \"ans\";\n"
            "                    inputradio.name = \"ans\";\n"
            "                    inputplace.appendChild(inputradio);\n"
            "                    inputplace.appendChild(document.createTextNode(\"" + answer + "\"));\n"
        )
    file.write(
        "                    document.getElementById(\"q\").appendChild(inputplace);\n"
        "                }\n"
    )
    file.close()
    file = open(file_name + ".check", "a")
    if question_number == 0:
        file.write(
            "                if (question == 1)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number + 1) + ")\n"
        )
    if language == "english":
        file.write(
            "                {\n"
            "                    var ele = document.getElementsByName('ans');\n"
            "                    for (i = 0; i < ele.length; i++)\n"
            "                    {\n"
            "                        if (ele[i].checked)\n"
            "                        {\n"
            "                            if (i == " + correct_answer + ")\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Correct.\";\n"
            "                            }\n"
            "                            else\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Incorrect.\";\n"
            "                            }\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "czech":
        file.write(
            "                {\n"
            "                    var ele = document.getElementsByName('ans');\n"
            "                    for (i = 0; i < ele.length; i++)\n"
            "                    {\n"
            "                        if (ele[i].checked)\n"
            "                        {\n"
            "                            if (i == " + correct_answer + ")\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Správně.\";\n"
            "                            }\n"
            "                            else\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Nesprávně.\";\n"
            "                            }\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "russian":
        file.write(
            "                {\n"
            "                    var ele = document.getElementsByName('ans');\n"
            "                    for (i = 0; i < ele.length; i++)\n"
            "                    {\n"
            "                        if (ele[i].checked)\n"
            "                        {\n"
            "                            if (i == " + correct_answer + ")\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Правилно.\";\n"
            "                            }\n"
            "                            else\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Не правильно.\";\n"
            "                            }\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "german":
        file.write(
            "                {\n"
            "                    var ele = document.getElementsByName('ans');\n"
            "                    for (i = 0; i < ele.length; i++)\n"
            "                    {\n"
            "                        if (ele[i].checked)\n"
            "                        {\n"
            "                            if (i == " + correct_answer + ")\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Richtig.\";\n"
            "                            }\n"
            "                            else\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Falsch.\";\n"
            "                            }\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "french":
        file.write(
            "                {\n"
            "                    var ele = document.getElementsByName('ans');\n"
            "                    for (i = 0; i < ele.length; i++)\n"
            "                    {\n"
            "                        if (ele[i].checked)\n"
            "                        {\n"
            "                            if (i == " + correct_answer + ")\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Corriger.\";\n"
            "                            }\n"
            "                            else\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Incorrect.\";\n"
            "                            }\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
        )
    elif language == "spanish":
        file.write(
            "                {\n"
            "                    var ele = document.getElementsByName('ans');\n"
            "                    for (i = 0; i < ele.length; i++)\n"
            "                    {\n"
            "                        if (ele[i].checked)\n"
            "                        {\n"
            "                            if (i == " + correct_answer + ")\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Correcto.\";\n"
            "                            }\n"
            "                            else\n"
            "                            {\n"
            "                                document.getElementById(\"c\").innerHTML = \"Incorrecto.\";\n"
            "                            }\n"
            "                        }\n"
            "                    }\n"
            "                }\n"
        )
    file.close()


def store_explain(file_name, texts, question_number):
    texts = texts.split("\\n")
    file = open(file_name + ".change", "a")
    if question_number == 0:
        file.write(
            "                if (question == 0)\n"
        )
    else:
        file.write(
            "                else if (question == " + str(question_number) + ")\n"
        )
    file.write(
        "                {\n"
        "                    question = " + str(question_number + 1) + ";\n"
    )
    for text in texts:
        file.write(
            "\n"
            "                    var text = document.createElement(\"p\");\n"
            "                    text.appendChild(document.createTextNode(\"" + text + "\"));\n"
            "                    document.getElementById(\"q\").appendChild(text);\n"
        )
    file.write(
        "                }\n"
    )
    file.close()
    if question_number == 0:
        file = open(file_name + ".check", "a")
        file.write(
            "                if (question == 1)\n"
            "                {"
            "                }"
        )
        file.close()


def print_from_storing_files_to_the_main_one(file_name):
    write_file = open(file_name, "a")
    read_file = open(file_name + ".change", "r")
    for line in read_file:
        write_file.write(line)
    read_file.close()
    read_file = open(file_name + ".check", "r")
    for line in read_file:
        write_file.write(line)
    read_file.close()
    write_file.close()


def print_tests_to_menu(directory, file_name):
    file = open(file_name, "a")
    [dirpath, dirnames, filenames] = directory
    dirpath = dirpath.split("/")
    if 3 < len(dirpath) < 7:
        file.write("        <h" + str(len(dirpath) - 2) + ">" + dirpath[len(dirpath) - 1]
                   + "</h" + str(len(dirpath) - 2) + ">\n")
    file.write("        <p>")
    for filename in filenames:
        file.write("<button onclick=\"window.location.href='")
        depth = 0
        for folder in dirpath:
            depth += 1
            if depth > 2:
                file.write(folder + "/")
        file.write(filename + "';\">" + filename + "</button>")
    file.write("</p>\n")
