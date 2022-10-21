#!/usr/bin/python3


def enter_question(language):
    if language == "english":
        return "Enter question."
    elif language == "czech":
        return "Napište otázku."
    elif language == "russian":
        return "Напишите вопрос."
    elif language == "german":
        return "Frage eingeben."
    elif language == "french":
        return "Entrer la question."
    elif language == "spanish":
        return "Ingrese la pregunta."


def read_info(language):
    if language == "english":
        return "Read the info."
    elif language == "czech":
        return "Přečtěte si informace."
    elif language == "russian":
        return "Прочтите информацию."
    elif language == "german":
        return "Lesen Sie die Informationen."
    elif language == "french":
        return "Lisez les informations."
    elif language == "spanish":
        return "Lea la información."


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


def click_on_next(language):
    if language == "english":
        return "Click on the button \"Next\" to start."
    elif language == "czech":
        return "Klikněte na tlačítko \"Další\" pro začátek."
    elif language == "russian":
        return "Нажмите на кнопку \"Дальше\", чтобы начать."
    elif language == "german":
        return "Klicken Sie den Knopf \"Nächster\" um fortzufahren."
    elif language == "french":
        return "Cliquez sur le bouton \"Suivant\" pour commencer."
    elif language == "spanish":
        return "Haga clic en el botón \"Siguiente\" para comenzar."


def your_question(language):
    if language == "english":
        return "Your question:"
    elif language == "czech":
        return "Vaše otázka:"
    elif language == "russian":
        return "Ваш вопрос:"
    elif language == "german":
        return "Ihre Frage:"
    elif language == "french":
        return "Votre question :"
    elif language == "spanish":
        return "Tu pregunta:"


def total_questions(language):
    if language == "english":
        return "Total questions:"
    elif language == "czech":
        return "Celkem otázek:"
    elif language == "russian":
        return "Всего вопросов:"
    elif language == "german":
        return "Fragen insgesamt:"
    elif language == "french":
        return "Nombre total de questions :"
    elif language == "spanish":
        return "Total de preguntas:"
