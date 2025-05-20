from db.db_manager import DatabaseManager
from ui.console_interface import get_user_command, handle_command, display_menu
from utils.logger import log_error

def main():
    print("Добро пожаловать в Movie Search App!")
    display_menu()

    with DatabaseManager() as db:
        while True:
            try:
                command = get_user_command()
                if command.lower() in ("exit", "quit"):
                    print("Выход из приложения.")
                    break
                handle_command(command, db)
            except Exception as e:
                log_error(e)
                print("Произошла ошибка. Подробности в logs/errors.log")

if __name__ == "__main__":
    main()