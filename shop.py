from classes import Category
from classes import Database


def category(username, password):
    product = input("Enter product name: ")
    query = f"SELECT * FROM {Category.table_name} WHERE {product} = {product} LIKE '%%{username}%%'"
    data = Database.connect(query, "select")
    for i in data:
        print(i)

    back = input("0. Back: ")
    if back == "0":
        return shop(username, password)


def shop(username, password):
    servise = input(f"""
        1. Cateory
        2. product
            >>>> """)

    if servise == "1":
        return category(username, password)

    elif servise == "2":
        pass

