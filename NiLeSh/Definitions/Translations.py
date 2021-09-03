#!/usr/bin/python3


def subject_name(subject, language):
    if language == "english":
        return subject.capitalize()
    elif language == "czech":
        if subject == "math":
            return "Matematika"
        elif subject == "physics":
            return "Fyzika"
        elif subject == "chemistry":
            return "Chemie"
        elif subject == "biology":
            return "Biologie"
        elif subject == "geography":
            return "Zeměpis"
        elif subject == "history":
            return "Dějepis"
        elif subject == "english":
            return "Angličtina"
        elif subject == "german":
            return "Němčina"
        elif subject == "czech":
            return "Čeština"
        elif subject == "russian":
            return "Ruština"
        elif subject == "french":
            return "Francouzština"
        elif subject == "spanish":
            return "Španělština"
        elif subject == "literature":
            return "Literatura"
        elif subject == "music":
            return "Hudba"
        elif subject == "art":
            return "Umění"
        elif subject == "informatics":
            return "Informatika"
    elif language == "russian":
        if subject == "math":
            return "Математика"
        elif subject == "physics":
            return "Физика"
        elif subject == "chemistry":
            return "Химия"
        elif subject == "biology":
            return "Биология"
        elif subject == "geography":
            return "География"
        elif subject == "history":
            return "История"
        elif subject == "english":
            return "Английский"
        elif subject == "german":
            return "Немецкий"
        elif subject == "czech":
            return "Чешский"
        elif subject == "russian":
            return "Русский"
        elif subject == "french":
            return "Французский"
        elif subject == "spanish":
            return "Испанский"
        elif subject == "literature":
            return "Литература"
        elif subject == "music":
            return "Музыка"
        elif subject == "art":
            return "Искусство"
        elif subject == "informatics":
            return "Информатика"
    elif language == "german":
        if subject == "math":
            return "Mathe"
        elif subject == "physics":
            return "Physik"
        elif subject == "chemistry":
            return "Chemie"
        elif subject == "biology":
            return "Biologie"
        elif subject == "geography":
            return "Geografie"
        elif subject == "history":
            return "Geschichte"
        elif subject == "english":
            return "Englisch"
        elif subject == "german":
            return "Deutsch"
        elif subject == "czech":
            return "Tschechisch"
        elif subject == "russian":
            return "Russisch"
        elif subject == "french":
            return "Französisch"
        elif subject == "spanish":
            return "Spanisch"
        elif subject == "literature":
            return "Literatur"
        elif subject == "music":
            return "Musik"
        elif subject == "art":
            return "Kunst"
        elif subject == "informatics":
            return "Informatik"
    elif language == "french":
        if subject == "math":
            return "Mathématique"
        elif subject == "physics":
            return "Physique"
        elif subject == "chemistry":
            return "Chimie"
        elif subject == "biology":
            return "Biologie"
        elif subject == "geography":
            return "Géographie"
        elif subject == "history":
            return "Historique"
        elif subject == "english":
            return "Anglais"
        elif subject == "german":
            return "Allemand"
        elif subject == "czech":
            return "Tchèque"
        elif subject == "russian":
            return "Russe"
        elif subject == "french":
            return "Français"
        elif subject == "spanish":
            return "Espagnol"
        elif subject == "literature":
            return "Littérature"
        elif subject == "music":
            return "Musique"
        elif subject == "art":
            return "Arts"
        elif subject == "informatics":
            return "Informatique"
    elif language == "spanish":
        if subject == "math":
            return "Matemáticas"
        elif subject == "physics":
            return "Física"
        elif subject == "chemistry":
            return "Química"
        elif subject == "biology":
            return "Biología"
        elif subject == "geography":
            return "Geografía"
        elif subject == "history":
            return "Historial"
        elif subject == "english":
            return "Inglés"
        elif subject == "german":
            return "Alemán"
        elif subject == "czech":
            return "Checo"
        elif subject == "russian":
            return "Ruso"
        elif subject == "french":
            return "Francés"
        elif subject == "spanish":
            return "Español"
        elif subject == "literature":
            return "Literatura"
        elif subject == "music":
            return "Música"
        elif subject == "art":
            return "Arte"
        elif subject == "informatics":
            return "Informática"


def click_on_next(language):
    if language == "english":
        return "Click on the button \"Next\" to start."
    elif language == "czech":
        return "Klikněte na tlačítko \"Další\" pro začátek."
    elif language == "russian":
        return "Нажмите на кнопку \"Дальше\", чтобы начать."
    elif language == "german":
        return "Klicken Sie den Knopf \"Nächster\" für fortzufahren."
    elif language == "french":
        return "Cliquez sur le bouton \"Suivant\" pour commencer."
    elif language == "spanish":
        return "Haga clic en el botón \"Siguiente\" para comenzar."


def button_next(language):
    if language == "english":
        return "Next"
    elif language == "czech":
        return "Další"
    elif language == "russian":
        return "Дальше"
    elif language == "german":
        return "Nächster"
    elif language == "french":
        return "Suivant"
    elif language == "spanish":
        return "Siguiente"


def button_check(language):
    if language == "english":
        return "Check answer"
    elif language == "czech":
        return "Zkontrolovat"
    elif language == "russian":
        return "Проверить"
    elif language == "german":
        return "Prüfen"
    elif language == "french":
        return "Vérifier"
    elif language == "spanish":
        return "Checar respuesta"


def no_checked_answer(language):
    if language == "english":
        return "There is no any checked answer."
    elif language == "czech":
        return "Není zde žádná zkontrolovaná odpověď."
    elif language == "russian":
        return "Здесь нет никакого исправленного ответа."
    elif language == "german":
        return "Es gibt keine geprüfte antwort."
    elif language == "french":
        return "Il n'y a pas de réponse vérifiée."
    elif language == "spanish":
        return "No hay ninguna respuesta marcada."


def to_main(language):
    if language == "english":
        return "<a href=\"../Main.html\">Back to Main menu</a>"
    elif language == "czech":
        return "<a href=\"../Main-czech.html\">Zpátky na hlavní menu</a>"
    elif language == "russian":
        return "<a href=\"../Main-russian.html\">Обратно на главное меню</a>"
    elif language == "german":
        return "<a href=\"../Main-german.html\">Zurück zum Hauptmenü</a>"
    elif language == "french":
        return "<a href=\"../Main-french.html\">Retour au menu principal</a>"
    elif language == "spanish":
        return "<a href=\"../Main-spanish.html\">Volver al menú principal</a>"


def on_subject_menu(subject, language):
    if language == "english":
        if subject == "math":
            return "Math.html\">Back to Math menu</a></p>\n"
        elif subject == "physics":
            return "Physics.html\">Back to Physics menu</a></p>\n"
        elif subject == "chemistry":
            return "Chemistry.html\">Back to Chemistry menu</a></p>\n"
        elif subject == "biology":
            return "Biology.html\">Back to Biology menu</a></p>\n"
        elif subject == "geography":
            return "Geography.html\">Back to Geography menu</a></p>\n"
        elif subject == "history":
            return "History.html\">Back to History menu</a></p>\n"
        elif subject == "english":
            return "English.html\">Back to English menu</a></p>\n"
        elif subject == "german":
            return "German.html\">Back to German menu</a></p>\n"
        elif subject == "czech":
            return "Czech.html\">Back to Czech menu</a></p>\n"
        elif subject == "russian":
            return "Russian.html\">Back to Russian menu</a></p>\n"
        elif subject == "french":
            return "French.html\">Back to French menu</a></p>\n"
        elif subject == "spanish":
            return "Spanish.html\">Back to Spanish menu</a></p>\n"
        elif subject == "literature":
            return "Literature.html\">Back to Literature menu</a></p>\n"
        elif subject == "music":
            return "Music.html\">Back to Music menu</a></p>\n"
        elif subject == "art":
            return "Art.html\">Back to Art menu</a></p>\n"
        elif subject == "informatics":
            return "Informatics.html\">Back to Informatics menu</a></p>\n"
    elif language == "czech":
        if subject == "math":
            return "Math-czech.html\">Zpátky na menu matematiky</a></p>\n"
        elif subject == "physics":
            return "Physics-czech.html\">Zpátky na menu fyziky</a></p>\n"
        elif subject == "chemistry":
            return "Chemistry-czech.html\">Zpátky na menu chemie</a></p>\n"
        elif subject == "biology":
            return "Biology-czech.html\">Zpátky na menu biologie</a></p>\n"
        elif subject == "geography":
            return "Geography-czech.html\">Zpátky na menu zeměpisu</a></p>\n"
        elif subject == "history":
            return "History-czech.html\">Zpátky na menu dějepisu</a></p>\n"
        elif subject == "english":
            return "English-czech.html\">Zpátky na menu angličtiny</a></p>\n"
        elif subject == "german":
            return "German-czech.html\">Zpátky na menu němčiny</a></p>\n"
        elif subject == "czech":
            return "Czech-czech.html\">Zpátky na menu češtiny</a></p>\n"
        elif subject == "russian":
            return "Russian-czech.html\">Zpátky na menu ruštiny</a></p>\n"
        elif subject == "french":
            return "French-czech.html\">Zpátky na menu francouzštiny</a></p>\n"
        elif subject == "spanish":
            return "Spanish-czech.html\">Zpátky na menu španělštiny</a></p>\n"
        elif subject == "literature":
            return "Literature-czech.html\">Zpátky na menu literatury</a></p>\n"
        elif subject == "music":
            return "Music-czech.html\">Zpátky na menu hudby</a></p>\n"
        elif subject == "art":
            return "Art-czech.html\">Zpátky na menu umění</a></p>\n"
        elif subject == "informatics":
            return "Informatics-czech.html\">Zpátky na menu informatiky</a></p>\n"
    elif language == "russian":
        if subject == "math":
            return "Math-russian.html\">Обратно на меню математики</a></p>\n"
        elif subject == "physics":
            return "Physics-russian.html\">Обратно на меню физики</a></p>\n"
        elif subject == "chemistry":
            return "Chemistry-russian.html\">Обратно на меню химии</a></p>\n"
        elif subject == "biology":
            return "Biology-russian.html\">Обратно на меню биологии</a></p>\n"
        elif subject == "geography":
            return "Geography-russian.html\">Обратно на меню географии</a></p>\n"
        elif subject == "history":
            return "History-russian.html\">Обратно на меню истории</a></p>\n"
        elif subject == "english":
            return "English-russian.html\">Обратно на меню английского</a></p>\n"
        elif subject == "german":
            return "German-russian.html\">Обратно на меню немецкого</a></p>\n"
        elif subject == "czech":
            return "Czech-russian.html\">Обратно на меню чешского</a></p>\n"
        elif subject == "russian":
            return "Russian-russian.html\">Обратно на меню русского</a></p>\n"
        elif subject == "french":
            return "French-russian.html\">Обратно на меню французского</a></p>\n"
        elif subject == "spanish":
            return "Spanish-russian.html\">Обратно на меню испанского</a></p>\n"
        elif subject == "literature":
            return "Literature-russian.html\">Обратно на меню литературы</a></p>\n"
        elif subject == "music":
            return "Music-russian.html\">Обратно на меню музыки</a></p>\n"
        elif subject == "art":
            return "Art-russian.html\">Обратно на меню искусства</a></p>\n"
        elif subject == "informatics":
            return "Informatics-russian.html\">Обратно на меню информатики</a></p>\n"
    elif language == "german":
        if subject == "math":
            return "Math-german.html\">Zurück zum Mathe-Menü</a></p>\n"
        elif subject == "physics":
            return "Physics-german.html\">Zurück zum Physik-Menü</a></p>\n"
        elif subject == "chemistry":
            return "Chemistry-german.html\">Zurück zum Chemie-Menü</a></p>\n"
        elif subject == "biology":
            return "Biology-german.html\">Zurück zum Biologie-Menü</a></p>\n"
        elif subject == "geography":
            return "Geography-german.html\">Zurück zum Geografie-Menü</a></p>\n"
        elif subject == "history":
            return "History-german.html\">Zurück zum Geschichte-Menü</a></p>\n"
        elif subject == "english":
            return "English-german.html\">Zurück zum Englisch-Menü</a></p>\n"
        elif subject == "german":
            return "German-german.html\">Zurück zum Deutsch-Menü</a></p>\n"
        elif subject == "czech":
            return "Czech-german.html\">Zurück zum Tschechisch-Menü</a></p>\n"
        elif subject == "russian":
            return "Russian-german.html\">Zurück zum Russisch-Menü</a></p>\n"
        elif subject == "french":
            return "French-german.html\">Zurück zum Französisch-Menü</a></p>\n"
        elif subject == "spanish":
            return "Spanish-german.html\">Zurück zum Spanisch-Menü</a></p>\n"
        elif subject == "literature":
            return "Literature-german.html\">Zurück zum Literatur-Menü</a></p>\n"
        elif subject == "music":
            return "Music-german.html\">Zurück zum Musik-Menü</a></p>\n"
        elif subject == "art":
            return "Art-german.html\">Zurück zum Kunst-Menü</a></p>\n"
        elif subject == "informatics":
            return "Informatics-german.html\">Zurück zum Informatik-Menü</a></p>\n"
    elif language == "french":
        if subject == "math":
            return "Math-french.html\">Retour au menu mathématique</a></p>\n"
        elif subject == "physics":
            return "Physics-french.html\">Retour au menu physique</a></p>\n"
        elif subject == "chemistry":
            return "Chemistry-french.html\">Retour au menu chimie</a></p>\n"
        elif subject == "biology":
            return "Biology-french.html\">Retour au menu biologie</a></p>\n"
        elif subject == "geography":
            return "Geography-french.html\">Retour au menu géographie</a></p>\n"
        elif subject == "history":
            return "History-french.html\">Retour au menu historique</a></p>\n"
        elif subject == "english":
            return "English-french.html\">Retour au menu anglais</a></p>\n"
        elif subject == "german":
            return "German-french.html\">Retour au menu allemand</a></p>\n"
        elif subject == "czech":
            return "Czech-french.html\">Retour au menu tchèque</a></p>\n"
        elif subject == "russian":
            return "Russian-french.html\">Retour au menu russe</a></p>\n"
        elif subject == "french":
            return "French-french.html\">Retour au menu français</a></p>\n"
        elif subject == "spanish":
            return "Spanish-french.html\">Retour au menu espagnol</a></p>\n"
        elif subject == "literature":
            return "Literature-french.html\">Retour au menu littérature</a></p>\n"
        elif subject == "music":
            return "Music-french.html\">Retour au menu musique</a></p>\n"
        elif subject == "art":
            return "Art-french.html\">Retour au menu arts</a></p>\n"
        elif subject == "informatics":
            return "Informatics-french.html\">Retour au menu informatique</a></p>\n"
    elif language == "spanish":
        if subject == "math":
            return "Math-spanish.html\">Volver al menú de matemáticas</a></p>\n"
        elif subject == "physics":
            return "Physics-spanish.html\">Volver al menú de Física</a></p>\n"
        elif subject == "chemistry":
            return "Chemistry-spanish.html\">Volver al menú de Química</a></p>\n"
        elif subject == "biology":
            return "Biology-spanish.html\">Volver al menú de Biología</a></p>\n"
        elif subject == "geography":
            return "Geography-spanish.html\">Volver al menú Geografía</a></p>\n"
        elif subject == "history":
            return "History-spanish.html\">Volver al menú Historial</a></p>\n"
        elif subject == "english":
            return "English-spanish.html\">Volver al menú en inglés</a></p>\n"
        elif subject == "german":
            return "German-spanish.html\">Volver al menú alemán</a></p>\n"
        elif subject == "czech":
            return "Czech-spanish.html\">Volver al menú checo</a></p>\n"
        elif subject == "russian":
            return "Russian-spanish.html\">Volver al menú ruso</a></p>\n"
        elif subject == "french":
            return "French-spanish.html\">Volver al menú francés</a></p>\n"
        elif subject == "spanish":
            return "Spanish-spanish.html\">Volver al menú en español</a></p>\n"
        elif subject == "literature":
            return "Literature-spanish.html\">Volver al menú literatura</a></p>\n"
        elif subject == "music":
            return "Music-spanish.html\">Volver al menú música</a></p>\n"
        elif subject == "art":
            return "Art-spanish.html\">Volver al menú arte</a></p>\n"
        elif subject == "informatics":
            return "Informatics-spanish.html\">Volver al menú informática</a></p>\n"


def good(language):
    if language == "english":
        return "Correct."
    elif language == "czech":
        return "Správně."
    elif language == "russian":
        return "Правильно."
    elif language == "german":
        return "Richtig."
    elif language == "french":
        return "Corriger."
    elif language == "spanish":
        return "Correcto."


def bad(language):
    if language == "english":
        return "Incorrect."
    elif language == "czech":
        return "Nesprávně."
    elif language == "russian":
        return "Не правильно."
    elif language == "german":
        return "Falsch."
    elif language == "french":
        return "Incorrect."
    elif language == "spanish":
        return "Incorrecto."


def congrats(language):
    if language == "english":
        return "Congratulation! You have ended this lesson."
    elif language == "czech":
        return "Gratuluji! Ukončil jste tuto lekci."
    elif language == "russian":
        return "Поздравляю! Вы закончили этот урок."
    elif language == "german":
        return "Herzlichen Glückwunsch! Sie haben diese Lektion beendet."
    elif language == "french":
        return "Félicitations ! Vous avez terminé cette leçon."
    elif language == "spanish":
        return "Enhorabuena Has terminado esta lección."


def enter_answer(language):
    if language == "english":
        return "Enter answer."
    elif language == "czech":
        return "Napište odpověď."
    elif language == "russian":
        return "Напишите ответ."
    elif language == "german":
        return "Antwort eingeben."
    elif language == "french":
        return "Entrer la réponse."
    elif language == "spanish":
        return "Ingrese la respuesta."


def choose_answer(language):
    if language == "english":
        return "Choose answer."
    elif language == "czech":
        return "Vyberte odpověď."
    elif language == "russian":
        return "Выберите ответ."
    elif language == "german":
        return "Antwort wählen."
    elif language == "french":
        return "Choisir la réponse."
    elif language == "spanish":
        return "Elegir respuesta."
