from utils.display_en import display_movies, display_category, display_popular_queries, display_actors
from rich.console import Console

console = Console()

def get_user_command():
    return console.input("[bold blue]Enter a command (m — menu, q — quit):[/bold blue] ")

def display_menu():
    print("Available commands:")
    print("  search keyword <word> — search by keyword in movie title")
    print("  search genre — search by genre")
    print("  search actor — search by actor")
    print("  search year <year> — search by release year")
    print("  p — most popular queries")
    print("  q — quit")

def handle_command(command, db):
    parts = command.strip().split()
    if not parts:
        console.print("[red]Empty command. Please try again.[/red]")
        return
    if parts[0] == "search":
        if parts[1] == "keyword" and len(parts) > 2:
            keyword = " ".join(parts[2:])
            results = db.search_by_keyword(keyword)
            display_movies(results)
        elif parts[1] == "genre":
            category = db.get_category()
            display_category(category)
            user_input = console.input(f"[bold blue]Enter genre number (integer from 1 to {len(category)}): [/bold blue]")
            if user_input.isdigit():
                category_id = int(user_input)
                if 1 <= category_id <= len(category):
                    results = db.search_by_genre(category[category_id-1]["category_id"])
                    display_movies(results)
                else:
                    console.print("[red]Genre number out of range.[/red]")
            else:
                console.print("[red]Invalid genre number input.[/red]")
        elif parts[1] == "year" and len(parts) == 3:
            try:
                year = int(parts[2])
                results = db.search_by_year(year)
                display_movies(results)
            except ValueError:
                console.print("[red]Error: please enter a valid year.[/red]")
        elif parts[1] == "actor" and len(parts) > 2:
            actor_name = " ".join(parts[2:])
            actors = db.get_actors(actor_name)
            if not actors:
                console.print(f"[bold red]No actors found for '{actor_name}'.[/bold red]")
                return
            actor = display_actors(actors)
            if actor:
                results = db.search_by_actor(actor)
                display_movies(results)
        else:
            console.print("[red]Invalid search command.[/red]")
    elif parts[0] == "p":
        queries = db.get_popular_queries()
        display_popular_queries(queries)
    elif parts[0] == "m":
        display_menu()
    else:
        console.print("[red]Unknown command.[/red]")
