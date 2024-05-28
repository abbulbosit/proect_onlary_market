from db.manage import Database


class Country:
    table_name = "country"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {Country.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO country( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE country SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE country SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM country WHERE {column} = {data}"
        else:
            query = f"DELETE FROM country WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class City(Country):
    table_name = "city"

    def __init__(self, name, city_id):
        Country.__init__(self, name)
        self.city_id = city_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {City.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO city(name, country_id) VALUES('{self.name}', {self.city_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        names = "city"
        if column == "id":
            query = f"UPDATE {names} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {names} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        name = "city"
        if column == "id":
            query = f"DELETE FROM {name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Address(City):
    table_name = "address"

    def __init__(self, name, city_id):
        City.__init__(self, name, city_id)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Address.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO address(name, country_id) VALUES('{self.name}', {self.city_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        names = "address"
        if column == "id":
            query = f"UPDATE {names} SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE {names} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        name = "address"
        if column == "id":
            query = f"DELETE FROM {name} WHERE {column} = {data}"
        else:
            query = f"DELETE FROM {name} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Customers(Country):
    table_name = "customers"
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    @staticmethod
    def select():
        query = f"SELECT * FROM {Customers.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    @staticmethod
    def personal_data(username, password):
        query = f"SELECT * FROM {Customers.table_name} WHERE username = '{username}' and password = '{password}'"
        return Database.connect(query, "select")

    def insert(self):
        query = f"""
            INSERT INTO customers(first_name, last_name, username, password) 
            VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}')
        """
        return Database.connect(query, "insert")


class PaymentStatus(Country):
    def __init__(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {PaymentStatus.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
             INSERT INTO payment_status( name) VALUES('{self.name}')
         """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE payment_status SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE payment_status SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM payment_status WHERE {column} = {data}"
        else:
            query = f"DELETE FROM payment_status WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Category(Country):
    def __init__(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Category.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO category( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE category SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE category SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM category WHERE {column} = {data}"
        else:
            query = f"DELETE FROM category WHERE {column} = '{data}'"
        return Database.connect(query, "delete")




class Store(Category):
    def __init__(self, name):
        Category.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Store.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO store( name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data):
        if column == "id":
            query = f"UPDATE sotre SET {column} = {new_data} WHERE {column} = {old_data} "

        else:
            query = f"UPDATE sotre SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data):
        if column == "id":
            query = f"DELETE FROM sotre WHERE {column} = {data}"
        else:
            query = f"DELETE FROM sotre WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Product:
    pass

