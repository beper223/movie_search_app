import mysql.connector
from utils.logger import log_error
from db.local_settings import dbconfig
from utils.decorators import with_categories_and_actors as with_categories


def get_query_fields():
    return """
           SELECT film.film_id,
                film.title,
                film.description,
                film.release_year as year,
                film.rating,
                film.length
           FROM film"""


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
            # raise

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

    @with_categories
    def search_by_keyword(self, keyword):
        self.save_search_query(keyword, "keyword")
        query = get_query_fields() + """
               WHERE film.title LIKE %s"""
        self.cursor.execute(query, (f"%{keyword}%",))
        return self.cursor.fetchall()



    @with_categories
    def search_by_genre(self, category_id):
        query = "SELECT name FROM category WHERE category_id = %s"
        self.cursor.execute(query, (category_id,))
        category = self.cursor.fetchone()
        if category:
            self.save_search_query(category['name'],"genre")
            query = get_query_fields() + """ film
                JOIN film_category
                ON film.film_id = film_category.film_id
                WHERE film_category.category_id = %s"""
            self.cursor.execute(query, (category_id,))
            return self.cursor.fetchall()
        return []

    @with_categories
    def search_by_year(self, year):
        self.save_search_query(str(year),"year")
        query = get_query_fields() + """
            WHERE release_year = %s"""
        self.cursor.execute(query, (year,))
        return self.cursor.fetchall()

    @with_categories
    def search_by_actor(self, actor):
        self.save_search_query(actor[1], "actor")
        query = get_query_fields() + """ film
                    JOIN film_actor fa
                ON film.film_id = fa.film_id
                    JOIN actor a ON fa.actor_id = a.actor_id
                WHERE a.actor_id = %s
                """
        self.cursor.execute(query, (actor[0],))
        return self.cursor.fetchall()

    def get_category(self):
        self.cursor.execute("SELECT category_id, name FROM category")
        return self.cursor.fetchall()

    def get_actors(self, name_part):
        query = """
                SELECT actor_id, first_name, last_name
                FROM actor 
                WHERE CONCAT(first_name,' ',last_name) LIKE %s
                ORDER BY first_name, last_name
                """
        like_pattern = f"%{name_part}%"
        self.cursor.execute(query, (like_pattern,))
        return self.cursor.fetchall()

    def save_search_query(self, query_text,query_type):
        try:
            # Проверка существующего запроса
            self.cursor.execute("""
                SELECT id, search_count
                FROM search_logs
                WHERE search_type = %s
                  AND search_text = %s
            """, (query_type, query_text))
            row = self.cursor.fetchone()
            if row:
                # Обновляем счётчик и дату
                self.cursor.execute("""
                    UPDATE search_logs
                    SET search_count = search_count + 1,
                        search_date  = NOW()
                    WHERE id = %s
                    """, (row["id"],))
            else:
                # Вставляем новую запись
                self.cursor.execute("""
                    INSERT INTO search_logs (
                    search_type, search_text, search_count, search_date)
                    VALUES (%s, %s, 1, NOW())
                    """, (query_type, query_text))
            self.conn.commit()
        except Exception as e:
            log_error(e)

    def get_popular_queries(self):
        self.cursor.execute("""
            SELECT search_text, search_type, search_count
            FROM search_logs
            ORDER BY search_count DESC LIMIT 10
                            """)
        return self.cursor.fetchall()
