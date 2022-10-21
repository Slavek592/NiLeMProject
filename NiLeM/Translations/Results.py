#!/usr/bin/python3


def no_checked_answer(language):
    if language == "english":
        return "There is no any checked answer."
    elif language == "czech":
        return "Není zde žádná zkontrolovaná odpověď."
    elif language == "russian":
        return "Здесь нет никакого исправленного ответа."
    elif language == "german":
        return "Es gibt keine geprüfte Antwort."
    elif language == "french":
        return "Il n'y a pas de réponse vérifiée."
    elif language == "spanish":
        return "No hay ninguna respuesta marcada."


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
        return "Correct."
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
        return "Félicitations ! Vous avez terminé la leçon."
    elif language == "spanish":
        return "Enhorabuena Has terminado esta lección."


def done(language):
    if language == "english":
        return "Done."
    elif language == "czech":
        return "Hotovo."
    elif language == "russian":
        return "Сделано."
    elif language == "german":
        return "Vollbracht."
    elif language == "french":
        return "C'est fait."
    elif language == "spanish":
        return "Se hace."


def error(language):
    if language == "english":
        return "There was an error."
    elif language == "czech":
        return "Nastala chyba."
    elif language == "russian":
        return "Произошла ошибка."
    elif language == "german":
        return "Es gab einen Fehler."
    elif language == "french":
        return "Il y avait une erreur."
    elif language == "spanish":
        return "Hubo un error."


def can_not_exit(language):
    if language == "english":
        return "I can not exit this directory."
    elif language == "czech":
        return "Nemohu opustit tuto složku."
    elif language == "russian":
        return "Не могу выйти из этой папки."
    elif language == "german":
        return "Ich kann diesen Ordner nicht verlassen."
    elif language == "french":
        return "Je ne peux pas quitter ce dossier."
    elif language == "spanish":
        return "No puedo salir de esta carpeta."
