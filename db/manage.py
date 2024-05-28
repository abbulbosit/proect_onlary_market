import psycopg2 as psql


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database='n45_l7',
            user='postgres',
            password='2009',
            host='localhost',
            port='5432',
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'delete', 'update', 'insert', 'alter']
        if query_type in data:
            db.commit()
            if query_type == "create":
                return f" create successful"
            return f"{query_type} query successful"
        else:
            return cursor.fetchall()


class Check:
    @staticmethod
    def login_check(username: str, password: str):
        query = f"SELECT * FROM customers WHERE username = '{username}'and password = '{password}'"
        data = Database.connect(query, "select ")
        if len(data) == 1:
            return True

        else:
            return False


def add_column():
    # query_1 = f"ALTER TABLE customers ADD COLUMN username VARCHAR(20)"
    # query_2 = f"ALTER TABLE customers ADD COLUMN password VARCHAR(20)"
    # Database.connect(query_1, "alter ")
    # Database.connect(query_2, "alter ")

    query = f"""
            INSERT INTO customers(first_name, last_name, username, password) 
            VALUES('Abdulboriy', 'Shojalilov', 'turbo_gaming', '2012game' )
        """
    return Database.connect(query, "insert")


# if __name__ == '__main__':
#     print(add_column())
