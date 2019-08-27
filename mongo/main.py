import pymongo
from pymongo import MongoClient

from settings import MONGO_DB, MONGO_HOST, MONGO_PASS, MONGO_PORT, MONGO_USER

from themes.handling import ThemeHandler


def main():
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client[MONGO_DB]
    db.authenticate(MONGO_USER, MONGO_PASS)
    # themes_collection = db.themes_collection
    # notes_collection = db.notes_collection
    main_menu = "Список тем - 1. Создать новую тему - 2."
    theme_menu = "Список заметок - 1. Создать новую заметку - 2."
    menu_command = input(main_menu)
    while menu_command != '1' and menu_command !='2':
        menu_command = input(main_menu)
    if menu_command == '1':
        themes = ThemeHandler.list(db)
        for theme in themes:
            print(theme['theme'])
    elif menu_command == '2':
        new_theme = input("Введите название темы: ")
        response  = ThemeHandler.create(db, new_theme)
        print(response)
    theme = input("Перейти к теме: ")

    return


if __name__ == '__main__':
    main()
