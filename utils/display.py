from rich.console import Console
from rich.table import Table

console = Console() # force_terminal=True

def display_movies(movies):
    if not movies:
        console.print("[bold red]Фильмы не найдены.[/bold red]")
        return
    console.rule("[bold green]Найденные фильмы:[/bold green]")

    page_size = 10 # Выводим по 10 фильмов на страницу
    total_movies = len(movies)
    page = 0  # индекс страницы
    total_pages = (total_movies + page_size - 1) // page_size
    show_table = True

    while True:
        start = page * page_size
        end = start + page_size

        if show_table:
            current_page = movies[start:end]
            for i, movie in enumerate(current_page, start + 1):
                console.print(f"\n[bold cyan]{i}. {movie['title']} ({movie['year']})[/bold cyan]")
                console.print(f"   [green]Жанры:[/green] {', '.join(movie.get('categories', []))}")
                console.print(f"   Рейтинг: {movie.get('rating', 'N/A')}, Длительность: {movie.get('length', 'N/A')} мин.")
                console.print(f"   [italic]Описание:[/italic] {movie['description']}")
                console.print(f"   [magenta]Актёры:[/magenta] {', '.join(movie.get('actors', []))}")
            console.print(f"Страница {page + 1} из {total_pages}")

        show_table = True
        choice = input("\033[1;34m'n' - next, 'p' - previous, q - exit:\033[0m ").strip()

        if choice.lower() == 'q':
            break
        elif choice.lower() == 'n':
            if page < total_pages - 1:
                page += 1
            else:
                console.print("[yellow]Это последняя страница.[/yellow]")
                show_table = False
        elif choice.lower() == 'p':
            if page > 0:
                page -= 1
            else:
                console.print("[yellow]Это первая страница.[/yellow]")
                show_table = False
        else:
            console.print("[red]Некорректный ввод. Попробуйте снова.[/red]")
            show_table = False

def display_category(categories):
    table = Table(title="Доступные жанры")
    table.add_column("№", style="cyan")
    table.add_column("Название", style="magenta")

    for i, category in enumerate(categories, 1):
        table.add_row(str(i), category['name'])

    console.print(table)

def display_popular_queries(queries):
    table = Table(title="Популярные поисковые запросы")
    table.add_column("№", style="cyan")
    table.add_column("Тип", style="magenta")
    table.add_column("Запрос", style="green")
    table.add_column("Количество", style="yellow")

    for i, row in enumerate(queries, 1):
        table.add_row(str(i), row['search_type'], row['search_text'], str(row['search_count']))

    console.print(table)

def display_actors(actors: list):
    page_size = 10  # количество записей на странице
    total_actors = len(actors)
    page  = 0  # индекс страницы
    total_pages = (total_actors + page_size - 1) // page_size
    show_table = True
    while True:
        start = page * page_size
        end = start + page_size

        if show_table:
            current_page = actors[start:end]
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("№", style="dim", width=4)
            table.add_column("Имя", style="cyan")
            table.add_column("Фамилия", style="cyan")

            for i, actor in enumerate(current_page, start + 1):
                table.add_row(str(i), actor["first_name"], actor["last_name"])
            console.print(table)
            console.print(f"Страница {page + 1} из {total_pages}")

        show_table = True
        choice = input(
            "\033[1;34mВведите № актёра для выбора, 'n' - next, 'p' - previous, q - exit:\033[1;34m ").strip()

        if choice == "q":
            return []
        elif choice.lower() == 'n':
            if page < total_pages - 1:
                page += 1
            else:
                console.print("[yellow]Это последняя страница.[/yellow]")
                show_table = False
        elif choice.lower() == 'p':
            if page > 0:
                page -= 1
            else:
                console.print("[yellow]Это первая страница.[/yellow]")
                show_table = False
        else:
            if choice.isdigit():
                num = int(choice)
                if 1 <= num <= total_actors:
                    actor = actors[num - 1]
                    full_name = f"{actor['first_name']} {actor['last_name']}"
                    return [actor["actor_id"], full_name]
            console.print("[red]Некорректный ввод. Попробуйте снова.[/red]")
            show_table = False

