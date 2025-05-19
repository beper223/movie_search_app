from db.db_manager import DatabaseManager
from ui.console_interface import get_user_command, handle_command
from utils.logger import log_error

def main():
    print("Добро пожаловать в Movie Search App!")
    print("Доступные команды:")
    print("  search keyword <слово> — поиск по ключевому слову")
    print("  search genre — поиск по жанру")
    print("  search year <год> — поиск по году")
    print("  popular — самые популярные запросы")
    print("  exit — выход")

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