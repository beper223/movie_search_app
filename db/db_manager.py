import mysql.connector
from utils.logger import log_error
from db.local_settings import dbconfig

class DatabaseManager:
    def __init__(self):
        self.dbconfig = dbconfig
        self.conn = None
        self.cursor = None

    def __enter__(self):
        try:
            self.conn = mysql.connector.connect(**self.dbconfig)
            # dictionary=True означает, что fetchall() вернёт список словарей, а не кортежей.
            # Это удобно для доступа к колонкам по имени, например row['title'].
            self.cursor = self.conn.cursor(dictionary=True)
            return self
        except Exception as e:
            log_error(e)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            log_error(e)
        if exc_type:
            log_error((exc_type, exc_val, exc_tb))
            #return False

    def search_by_keyword(self, keyword):
        self.save_search_query(keyword)
        query = "SELECT title, description, release_year FROM film WHERE title LIKE %s LIMIT 20"
        self.cursor.execute(query, (f"%{keyword}%",))
        return self.cursor.fetchall()

    def search_by_genre(self, category_id):
        query = "SELECT name FROM category WHERE category_id = %s"
        self.cursor.execute(query, (category_id,))
        category = self.cursor.fetchone()
        if category:
            self.save_search_query(category['name'])
            query = """
                    SELECT film.title, film.description, film.release_year as year FROM film
                    JOIN film_category ON film.film_id = film_category.film_id
                    WHERE film_category.category_id = %s
                    LIMIT 20
                    """
            self.cursor.execute(query, (category_id,))
            return self.cursor.fetchall()
        return []

    def search_by_year(self, year):
        self.save_search_query(str(year))
        query = "SELECT title, description, release_year FROM movies WHERE release_year = %s LIMIT 20"
        self.cursor.execute(query, (year,))
        return self.cursor.fetchall()

    def get_category(self):
        self.cursor.execute("SELECT category_id, name FROM category")
        return self.cursor.fetchall()

    def save_search_query(self, query):
        try:
            self.cursor.execute(
                "INSERT INTO search_history (query) VALUES (%s)", (query,)
            )
            self.conn.commit()
        except Exception as e:
            log_error(e)

    def get_popular_queries(self):
        self.cursor.execute(
            "SELECT query, COUNT(*) as count FROM search_history GROUP BY query ORDER BY count DESC LIMIT 10"
        )
        return self.cursor.fetchall()