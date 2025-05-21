def display_movies(movies):
    if not movies:
        print("Фильмы не найдены.")
        return
    print("Найденные фильмы:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} ({movie['year']})")
        print(f"   Жанры: {', '.join(movie.get('categories', []))}")
        print(f"   Рейтинг: {movie.get('rating', 'N/A')}, Длительность: {movie.get('length', 'N/A')} мин.")
        print(f"   Описание: {movie['description']}")
        print(f"   Актёры: {', '.join(movie.get('actors', []))}")

def display_category(categorys):
    print("Доступные жанры:")
    for i, category in enumerate(categorys, 1):
        print(f"{i}. {category['name']}")

def display_popular_queries(queries):
    print("Популярные поисковые запросы:")
    for i, row in enumerate(queries, 1):
        print(f"{i}. [{row['search_type']}] {row['search_text']} ({row['search_count']} раз)")