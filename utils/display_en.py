from rich.console import Console
from rich.table import Table

console = Console()  # force_terminal=True

def display_movies(movies):
    if not movies:
        console.print("[bold red]No movies found.[/bold red]")
        return
    console.rule("[bold green]Found Movies:[/bold green]")

    page_size = 10  # Show 10 movies per page
    total_movies = len(movies)
    page = 0  # page index
    total_pages = (total_movies + page_size - 1) // page_size
    show_table = True

    while True:
        start = page * page_size
        end = start + page_size

        if show_table:
            current_page = movies[start:end]
            for i, movie in enumerate(current_page, start + 1):
                console.print(f"\n[bold cyan]{i}. {movie['title']} ({movie['year']})[/bold cyan]")
                console.print(f"   [green]Genres:[/green] {', '.join(movie.get('categories', []))}")
                console.print(f"   Rating: {movie.get('rating', 'N/A')}, Duration: {movie.get('length', 'N/A')} min.")
                console.print(f"   [italic]Description:[/italic] {movie['description']}")
                console.print(f"   [magenta]Actors:[/magenta] {', '.join(movie.get('actors', []))}")
            console.print(f"Page {page + 1} of {total_pages}")

        show_table = True
        choice = console.input("[bold blue]'n' - next, 'p' - previous, q - exit:[/bold blue] ").strip()

        if choice.lower() == 'q':
            break
        elif choice.lower() == 'n':
            if page < total_pages - 1:
                page += 1
            else:
                console.print("[yellow]This is the last page.[/yellow]")
                show_table = False
        elif choice.lower() == 'p':
            if page > 0:
                page -= 1
            else:
                console.print("[yellow]This is the first page.[/yellow]")
                show_table = False
        else:
            console.print("[red]Invalid input. Please try again.[/red]")
            show_table = False

def display_category(categories):
    table = Table(title="Available Genres")
    table.add_column("No.", style="cyan")
    table.add_column("Name", style="magenta")

    for i, category in enumerate(categories, 1):
        table.add_row(str(i), category['name'])

    console.print(table)

def display_popular_queries(queries):
    table = Table(title="Popular Search Queries")
    table.add_column("No.", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Query", style="green")
    table.add_column("Count", style="yellow")

    for i, row in enumerate(queries, 1):
        table.add_row(str(i), row['search_type'], row['search_text'], str(row['search_count']))

    console.print(table)

def display_actors(actors: list):
    page_size = 10  # number of records per page
    total_actors = len(actors)
    page = 0  # page index
    total_pages = (total_actors + page_size - 1) // page_size
    show_table = True

    while True:
        start = page * page_size
        end = start + page_size

        if show_table:
            current_page = actors[start:end]
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("No.", style="dim", width=4)
            table.add_column("First Name", style="cyan")
            table.add_column("Last Name", style="cyan")

            for i, actor in enumerate(current_page, start + 1):
                table.add_row(str(i), actor["first_name"], actor["last_name"])
            console.print(table)
            console.print(f"Page {page + 1} of {total_pages}")

        show_table = True
        choice = console.input(
            "[bold blue]Enter actor No. to select, 'n' - next, 'p' - previous, q - exit:[/bold blue] ").strip()

        if choice == "q":
            return []
        elif choice.lower() == 'n':
            if page < total_pages - 1:
                page += 1
            else:
                console.print("[yellow]This is the last page.[/yellow]")
                show_table = False
        elif choice.lower() == 'p':
            if page > 0:
                page -= 1
            else:
                console.print("[yellow]This is the first page.[/yellow]")
                show_table = False
        else:
            if choice.isdigit():
                num = int(choice)
                if 1 <= num <= total_actors:
                    actor = actors[num - 1]
                    full_name = f"{actor['first_name']} {actor['last_name']}"
                    return [actor["actor_id"], full_name]
            console.print("[red]Invalid input. Please try again.[/red]")
            show_table = False
