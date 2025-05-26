from utils.display import display_movies, display_category, display_popular_queries, display_actors
from rich.console import Console

console = Console()

def get_user_command():
    return input("\033[1;34mВведите команду (m — меню, q — выход):\033[0m ")


def display_menu():
    print("Доступные команды:")
    print("  search keyword <слово> — поиск по ключевому слову в названии фильма")
    print("  search genre — поиск по жанру")
    print("  search actor — поиск по актрёру")
    print("  search year <год> — поиск по году")
    print("  p — самые популярные запросы")
    print("  q — выход")

def handle_command(command, db):
    parts = command.strip().split()
    if not parts:
        console.print("[red]Пустая команда. Попробуйте снова.[/red]")
        return
    if parts[0] == "search":
        if parts[1] == "keyword" and len(parts) > 2:
            keyword = " ".join(parts[2:])
            results = db.search_by_keyword(keyword)
            display_movies(results)
        elif parts[1] == "genre":
            category = db.get_category()
            display_category(category)
            user_input = input(f"\033[1;34mВведите номер жанра (целое число от 1 до {len(category)}): \033[0m")
            if user_input.isdigit():
                category_id = int(user_input)
                if 1 <= category_id <= len(category):
                    results = db.search_by_genre(category[category_id-1]["category_id"])
                    display_movies(results)
                else:
                    console.print("[red]Номер жанра вне диапазона.[/red]")
            else:
                console.print("[red]Ошибка при вводе номера жанра.[/red]")
        elif parts[1] == "year" and len(parts) == 3:
            try:
                year = int(parts[2])
                results = db.search_by_year(year)
                display_movies(results)
            except ValueError:
                console.print("[red]Ошибка: введите корректный год.[/red]")
        elif parts[1] == "actor" and len(parts) > 2:
            actor_name = " ".join(parts[2:])
            actors = db.get_actors(actor_name)
            if not actors:
                console.print(f"[bold red]Актёры '{actor_name}' не найдены.[/bold red]")
                return
            actor = display_actors(actors)
            if actor:
                results = db.search_by_actor(actor)
                display_movies(results)
        else:
            console.print("[red]Неверная команда поиска.[/red]")
    elif parts[0] == "p":
        queries = db.get_popular_queries()
        display_popular_queries(queries)
    elif parts[0] == "m":
        display_menu()
    else:
        console.print("[red]Неизвестная команда.[/red]")
