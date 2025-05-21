from rich.console import Console
from rich.table import Table

console = Console() # force_terminal=True

def display_movies(movies):
    if not movies:
        console.print("[bold red]Фильмы не найдены.[/bold red]")
        return
    console.rule("[bold green]Найденные фильмы:[/bold green]")
    # Выводим по 10 фильмов на страницу
    page_size = 10
    for i in range(0, len(movies), page_size):
        page = movies[i:i + page_size]
        for j, movie in enumerate(page, i + 1):
            console.print(f"\n[bold cyan]{j}. {movie['title']} ({movie['year']})[/bold cyan]")
            console.print(f"   [green]Жанры:[/green] {', '.join(movie.get('categories', []))}")
            console.print(f"   Рейтинг: {movie.get('rating', 'N/A')}, Длительность: {movie.get('length', 'N/A')} мин.")
            console.print(f"   [italic]Описание:[/italic] {movie['description']}")
            console.print(f"   [magenta]Актёры:[/magenta] {', '.join(movie.get('actors', []))}")

        if i + page_size < len(movies):
            cont = input("Нажмите Enter для следующей страницы или 'q' для выхода: ")
            if cont.lower() == 'q':
                break

def display_category(categorys):
    table = Table(title="Доступные жанры")
    table.add_column("ID", style="cyan")
    table.add_column("Название", style="magenta")

    for i, category in enumerate(categorys, 1):
        table.add_row(str(i), category['name'])

    console.print(table)

def display_popular_queries(queries):
    table = Table(title="Популярные поисковые запросы")
    table.add_column("#", style="cyan")
    table.add_column("Тип", style="magenta")
    table.add_column("Запрос", style="green")
    table.add_column("Количество", style="yellow")

    for i, row in enumerate(queries, 1):
        table.add_row(str(i), row['search_type'], row['search_text'], str(row['search_count']))

    console.print(table)