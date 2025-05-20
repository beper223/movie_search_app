def with_categories(func):
    def wrapper(self, *args, **kwargs):
        films = func(self, *args, **kwargs)
        if not films:
            return []
        film_ids = [film["film_id"] for film in films]
        format_strings = ','.join(['%s'] * len(film_ids))
        query = f"""
            SELECT fc.film_id, c.name 
            FROM film_category fc 
            JOIN category c ON fc.category_id = c.category_id
            WHERE fc.film_id IN ({format_strings})
        """
        self.cursor.execute(query, tuple(film_ids))
        categories = self.cursor.fetchall()

        category_map = {}
        for cat in categories:
            category_map.setdefault(cat["film_id"], []).append(cat["name"])

        for film in films:
            film["categories"] = category_map.get(film["film_id"], [])

        return films
    return wrapper