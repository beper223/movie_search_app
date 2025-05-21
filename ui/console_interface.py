from sys import exec_prefix

from utils.display import display_movies, display_category, display_popular_queries
from utils.logger import log_error

def get_user_command():
    return input("Введите команду (menu — меню, exit — выход): ")

def display_menu():
    print("Доступные команды:")
    print("  search keyword <слово> — поиск по ключевому слову")
    print("  search genre — поиск по жанру")
    print("  search year <год> — поиск по году")
    print("  popular — самые популярные запросы")
    print("  exit, quit — выход")

def handle_command(command, db):
    parts = command.strip().split()
    if parts[0] == "search":
        if parts[1] == "keyword" and len(parts) > 2:
            keyword = " ".join(parts[2:])
            results = db.search_by_keyword(keyword)
            display_movies(results)
        elif parts[1] == "genre":
            category = db.get_category()
            display_category(category)
            user_input = input(f"Введите номер жанра (целое число от 1 до {len(category)}): ")
            try:
                category_id = int(user_input)
                if 1 <= category_id <= len(category):
                    results = db.search_by_genre(category[category_id-1]["category_id"])
                    display_movies(results)
                else:
                    print("Номер жанра вне диапазона.")
            except ValueError:
                print("Ошибка при вводе номера жанра.")
        elif parts[1] == "year" and len(parts) == 3:
            try:
                year = int(parts[2])
                results = db.search_by_year(year)
                display_movies(results)
            except ValueError:
                print("Ошибка: введите корректный год.")
        else:
            print("Неверная команда поиска.")
    elif parts[0] == "popular":
        queries = db.get_popular_queries()
        display_popular_queries(queries)
    elif parts[0] == "menu":
        display_menu()
    else:
        print("Неизвестная команда.")
