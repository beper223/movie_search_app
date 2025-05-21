def with_categories_and_actors(func):
    def wrapper(self, *args, **kwargs):
        films = func(self, *args, **kwargs)
        if not films:
            return []
        film_ids = [film["film_id"] for film in films]
        format_strings = ','.join(['%s'] * len(film_ids))

        # Категории
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

        # Актеры
        actor_query = f"""
                    SELECT fa.film_id, a.first_name, a.last_name
                    FROM film_actor fa
                    JOIN actor a ON fa.actor_id = a.actor_id
                    WHERE fa.film_id IN ({format_strings})
                """
        self.cursor.execute(actor_query, tuple(film_ids))
        actors = self.cursor.fetchall()

        actor_map = {}
        for actor in actors:
            name = f"{actor['first_name']} {actor['last_name']}"
            actor_map.setdefault(actor["film_id"], []).append(name)

        for film in films:
            film["categories"] = category_map.get(film["film_id"], [])
            film["actors"] = actor_map.get(film["film_id"], [])

        return films
    return wrapper