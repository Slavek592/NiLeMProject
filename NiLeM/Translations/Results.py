#!/usr/bin/python3


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