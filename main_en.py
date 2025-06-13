from db.db_manager import DatabaseManager
from ui.console_interface_en import get_user_command, handle_command, display_menu
from utils.logger import log_error
from rich.console import Console

console = Console()

def main():
    console.print("[bold green]Welcome to the Movie Search App![/bold green]")
    display_menu()

    with DatabaseManager() as db:
        while True:
            try:
                command = get_user_command()
                if command.lower() == "q":
                    console.print("[yellow]Exiting the application.[/yellow]")
                    break
                handle_command(command, db)
            except Exception as e:
                log_error(e)
                console.print("[red]An error occurred. See logs/errors.log for details.[/red]")

if __name__ == "__main__":
    main()
