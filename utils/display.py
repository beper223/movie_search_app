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
    idx_offset = 0  # индекс страницы
    refresh = True
    while True:
        if not refresh:
            refresh = True
        else:
            page = actors[idx_offset:idx_offset + page_size]

            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("№", style="dim", width=4)
            table.add_column("Имя", style="cyan")
            table.add_column("Фамилия", style="cyan")

            for idx, actor in enumerate(page, idx_offset + 1):
                table.add_row(str(idx), actor["first_name"], actor["last_name"])
            console.print(table)

            console.print(
                f"Страница {idx_offset // page_size + 1} из {(total_actors + page_size - 1) // page_size}")

        choice = input(
            "Введите номер актёра для выбора, 'n' - следующая, 'p' - предыдущая, Enter для выхода: ").strip()

        if choice == "":
            return []
        elif choice.lower() == 'n':
            if idx_offset + page_size < total_actors:
                idx_offset += page_size
            else:
                console.print("[yellow]Это последняя страница.[/yellow]")
                refresh = False
        elif choice.lower() == 'p':
            if idx_offset - page_size >= 0:
                idx_offset -= page_size
            else:
                console.print("[yellow]Это первая страница.[/yellow]")
                refresh = False
        else:
            try:
                num = int(choice)
                if 1 <= num <= total_actors:
                    actor = actors[num - 1]
                    return [actor["actor_id"], f"{actor["first_name"]} {actor["last_name"]}"]
                else:
                    console.print("[red]Неверный номер. Попробуйте снова.[/red]")
                    refresh = False
            except ValueError:
                console.print("[red]Некорректный ввод. Попробуйте снова.[/red]")
                refresh = False

