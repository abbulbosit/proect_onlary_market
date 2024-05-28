from classes import Customers


def personal_data(username, password):
    data = Customers.personal_data(username, password)
    print(f"""
        first name: {data[0][1]}
        last name: {data[0][2]}
        username: {data[0][6]}
        password: {data[0][7]}
    """)

    back = input("0. Back")
    if back == "0":
        return account(username, password)

def account(username, password):
    services = input("""
        1. My Personal Data
        2. Story
        3. Ordering
        4. Log Out
            >>> """)

    if services == '1':
        return personal_data(username, password)

    elif services == '2':
        pass

    elif services == '3':
        pass

    elif services == '4':
        pass


