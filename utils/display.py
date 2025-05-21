def display_movies(movies):
    if not movies:
        print("Фильмы не найдены.")
        return
    print("Найденные фильмы:")
    # Выводим по 10 фильмов на страницу
    page_size = 10
    for i in range(0, len(movies), page_size):
        page = movies[i:i + page_size]
        for j, movie in enumerate(page, i + 1):
            print(f"{j}. {movie['title']} ({movie['year']})")
            print(f"   Жанры: {', '.join(movie.get('categories', []))}")
            print(f"   Рейтинг: {movie.get('rating', 'N/A')}, Длительность: {movie.get('length', 'N/A')} мин.")
            print(f"   Описание: {movie['description']}")
            print(f"   Актёры: {', '.join(movie.get('actors', []))}")

        if i + page_size < len(movies):
            cont = input("Нажмите Enter для следующей страницы или 'q' для выхода: ")
            if cont.lower() == 'q':
                break

def display_category(categorys):
    print("Доступные жанры:")
    for i, category in enumerate(categorys, 1):
        print(f"{i}. {category['name']}")

def display_popular_queries(queries):
    print("Популярные поисковые запросы:")
    for i, row in enumerate(queries, 1):
        print(f"{i}. [{row['search_type']}] {row['search_text']} ({row['search_count']} раз)")