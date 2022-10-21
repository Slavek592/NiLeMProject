#!/usr/bin/python3


def turn_off(language):
    if language == "english":
        return "Turn off"
    elif language == "czech":
        return "Vypnout"
    elif language == "russian":
        return "Выключить"
    elif language == "german":
        return "Schließen"
    elif language == "french":
        return "Fermer"
    elif language == "spanish":
        return "Apagar"


def to_main(language):
    if language == "english":
        return "Back to Main menu"
    elif language == "czech":
        return "Zpátky na hlavní menu"
    elif language == "russian":
        return "Обратно на главное меню"
    elif language == "german":
        return "Zurück zum Hauptmenü"
    elif language == "french":
        return "Retour au menu principal"
    elif language == "spanish":
        return "Volver al menú principal"


def to_nilem(language):
    if language == "english":
        return "Back to NiLeM menu"
    elif language == "czech":
        return "Zpátky na NiLeM menu"
    elif language == "russian":
        return "Обратно на меню NiLeM"
    elif language == "german":
        return "Zurück zum NiLeM-Menü"
    elif language == "french":
        return "Retour au menu NiLeM"
    elif language == "spanish":
        return "Volver al menú NiLeM"


def to_nilesh(language):
    if language == "english":
        return "Back to NiLeSh menu"
    elif language == "czech":
        return "Zpátky na NiLeSh menu"
    elif language == "russian":
        return "Обратно на меню NiLeSh"
    elif language == "german":
        return "Zurück zum NiLeSh-Menü"
    elif language == "french":
        return "Retour au menu NiLeSh"
    elif language == "spanish":
        return "Volver al menú NiLeSh"


def to_editor(language):
    if language == "english":
        return "Back to editor menu"
    elif language == "czech":
        return "Zpátky na menu editoru"
    elif language == "russian":
        return "Вернуться в меню редактора"
    elif language == "german":
        return "Zurück zum Editor-Menü"
    elif language == "french":
        return "Retour au menu de l'éditeur"
    elif language == "spanish":
        return "Volver al menú del editor"


def to_info(language):
    if language == "english":
        return "Back to info menu"
    elif language == "czech":
        return "Zpátky na menu informací"
    elif language == "russian":
        return "Вернуться в информационное меню"
    elif language == "german":
        return "Zurück zum Infomenü"
    elif language == "french":
        return "Retour au menu d'informations"
    elif language == "spanish":
        return "Volver al menú de información"


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


def enter_word(language):
    if language == "english":
        return "Enter"
    elif language == "czech":
        return "Napsat"
    elif language == "russian":
        return "Ввести"
    elif language == "german":
        return "Eingeben"
    elif language == "french":
        return "Entrer"
    elif language == "spanish":
        return "Entrar"


def radio_word(language):
    if language == "english":
        return "Radio"
    elif language == "czech":
        return "Vybrat"
    elif language == "russian":
        return "Выбрать"
    elif language == "german":
        return "Wählen"
    elif language == "french":
        return "Choisir"
    elif language == "spanish":
        return "Escoger"


def explain_word(language):
    if language == "english":
        return "Explain"
    elif language == "czech":
        return "Vysvětlit"
    elif language == "russian":
        return "Объяснить"
    elif language == "german":
        return "Erklären"
    elif language == "french":
        return "Explique"
    elif language == "spanish":
        return "Explicar"


def new_question(language):
    if language == "english":
        return "New question"
    elif language == "czech":
        return "Nová otázka"
    elif language == "russian":
        return "Новый вопрос"
    elif language == "german":
        return "Neue Frage"
    elif language == "french":
        return "Nouvelle question"
    elif language == "spanish":
        return "Nueva pregunta"


def save_to_database(language):
    if language == "english":
        return "Save to database"
    elif language == "czech":
        return "Uložit do databáze"
    elif language == "russian":
        return "Сохранить в базу данных"
    elif language == "german":
        return "In Datenbank speichern"
    elif language == "french":
        return "Enregistrer dans la base de données"
    elif language == "spanish":
        return "Guardar en la base de datos"


def word_set(language):
    if language == "english":
        return "Set"
    elif language == "czech":
        return "Nastavit"
    elif language == "russian":
        return "Настроить"
    elif language == "german":
        return "Setzen"
    elif language == "french":
        return "Régler"
    elif language == "spanish":
        return "Colocar"


def databases(language):
    if language == "english":
        return "Databases"
    elif language == "czech":
        return "Databáze"
    elif language == "russian":
        return "Базы данных"
    elif language == "german":
        return "Datenbanken"
    elif language == "french":
        return "Bases de données"
    elif language == "spanish":
        return "Bases de datos"


def file_runner(language):
    if language == "english":
        return "Run files"
    elif language == "czech":
        return "Spustit soubory"
    elif language == "russian":
        return "Выполнить файлы"
    elif language == "german":
        return "Datei anlassen"
    elif language == "french":
        return "Démarrer le fichier"
    elif language == "spanish":
        return "Ejecutar archivos"


def export_lesson(language):
    if language == "english":
        return "Export lesson"
    elif language == "czech":
        return "Exportovat lekci"
    elif language == "russian":
        return "Экспорт урока"
    elif language == "german":
        return "Lektion exportieren"
    elif language == "french":
        return "Exporter le cours"
    elif language == "spanish":
        return "Exportar lección"


def export_text(language):
    if language == "english":
        return "Export as plain text"
    elif language == "czech":
        return "Exportovat jako prostý text"
    elif language == "russian":
        return "Экспорт в виде обычного текста"
    elif language == "german":
        return "Als Klartext exportieren"
    elif language == "french":
        return "Exporter en texte brut"
    elif language == "spanish":
        return "Exportar como texto sin formato"


def save_and_exit(language):
    if language == "english":
        return "Save and exit"
    elif language == "czech":
        return "Uložit a odejít"
    elif language == "russian":
        return "Сохранить и выйти"
    elif language == "german":
        return "Speichern und schließen"
    elif language == "french":
        return "Sauvegarder et quitter"
    elif language == "spanish":
        return "Guardar y Salir"


def delete_and_exit(language):
    if language == "english":
        return "Delete and exit"
    elif language == "czech":
        return "Smazat a odejít"
    elif language == "russian":
        return "Удалить и выйти"
    elif language == "german":
        return "Löschen und schließen"
    elif language == "french":
        return "Supprimer et quitter"
    elif language == "spanish":
        return "Eliminar y salir"


def new(language):
    if language == "english":
        return "New"
    elif language == "czech":
        return "Nová"
    elif language == "russian":
        return "Новый"
    elif language == "german":
        return "Neu"
    elif language == "french":
        return "Nouveau"
    elif language == "spanish":
        return "Nuevo"


def show_correct(language):
    if language == "english":
        return "Show correct answer"
    elif language == "czech":
        return "Ukázat správnou odpověď"
    elif language == "russian":
        return "Показать правильный ответ"
    elif language == "german":
        return "Richtige Antwort anzeigen"
    elif language == "french":
        return "Afficher la réponse correcte"
    elif language == "spanish":
        return "Mostrar respuesta correcta"


def manual(language):
    if language == "english":
        return "Manual"
    elif language == "czech":
        return "Manuál"
    elif language == "russian":
        return "Руководство"
    elif language == "german":
        return "Handbuch"
    elif language == "french":
        return "Manuel"
    elif language == "spanish":
        return "Manual"


def sources(language):
    if language == "english":
        return "Sources"
    elif language == "czech":
        return "Zdroje"
    elif language == "russian":
        return "Источники"
    elif language == "german":
        return "Quellen"
    elif language == "french":
        return "Sources"
    elif language == "spanish":
        return "Fuentes"
