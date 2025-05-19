def display_movies(movies):
    if not movies:
        print("Фильмы не найдены.")
        return
    print("Найденные фильмы:")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} ({movie['year']})")
        print(f"   Описание: {movie['description']}")

def display_category(categorys):
    print("Доступные жанры:")
    for i, category in enumerate(categorys, 1):
        print(f"{i}. {category['name']}")

def display_popular_queries(queries):
    print("Популярные поисковые запросы:")
    for i, row in enumerate(queries, 1):
        print(f"{i}. {row['query']} ({row['count']} раз)")