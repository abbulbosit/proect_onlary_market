from classes import Country, City, Address, Customers
from db.manage import Check
import account
import shop
def country_tables():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        Country.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return country_tables()

    elif services == "2":
        name = input("Name: ")
        country = Country(name)
        print(country.insert())
        return country_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(Country.update(column, new_data, old_data))

        return country_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Country.delete(column, data))
        return country_tables()


def city_tables():

    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        City.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return city_tables()

    elif services == "2":
        name = input("Name: ")
        city_id = int(input("Country ID: "))
        city = City(name, city_id)
        print(city.insert())
        return city_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(City.update(column, new_data, old_data))

        return city_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(City.delete(column, data))
        return city_tables()


def address_tables():

    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>> """)
    if services == "1":
        Address.select()
        back = input("""
            0. back
                >>> """)
        if back == "0":
            return address_tables()

    elif services == "2":
        name = input("Name: ")
        city_id = int(input("Country ID: "))
        city = Address(name, city_id)
        print(city.insert())
        return city_tables()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data: ")
        new_data = input("New data: ")
        print(Address.update(column, new_data, old_data))

        return address_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Address.delete(column, data))
        return address_tables()


def main():
    table = input("""
        1. Country
        2. City
        3. Address
        4. Customers
        5. PaymentStatus
        6. Category
        7. Store
        8. Product
            >>> """)

    if table == '1':
        return country_tables()

    elif table == '2':
        return city_tables()

    elif table == '3':
        return address_tables()

    elif table == '4':
        return address_tables()

    elif table == '5':
        return address_tables()

    elif table == '6':
        return address_tables()

    elif table == '7':
        return address_tables()

    else:
        print("error")
        return main()


def webside(username, password):
    web = input(f"""
    Welcome to website
        1. SHop
        2. Cards
        3. Account
            >>> """)

    if web == "1":
        return shop.shop(username, password)

    elif web == "2":
        pass

    elif web == "3":

        return account.account(username, password)

    else:
        print("error")
        return webside(username, password)


def login():
    username = input("Username: ")
    password = input("Password: ")
    if Check.login_check(username, password):
        return webside(username, password)

    else:
        print("Invalid username or password")
        return login()


def register():
    print("Register page")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    username = input("Username: ")
    password_1 = input("Password: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        print("Passwords do not match")
        password_1 = input("Password: ")
        password_2 = input("Reply Password: ")
    new_customer = Customers(first_name, last_name, username, password_1)
    print(new_customer.insert())

    return main_login()


def main_login():
    user = input("""
        1. Login
        2. Register
            >>> """)

    if user == "1":
        return login()

    elif user == "2":
        return register()

    else:
        print("qiziquvchanlik qilma (shumaxer)")
        return main_login()


if __name__ == "__main__":
    main_login()
