import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_courier_data():
    login = generate_random_string(5)
    password = generate_random_string(5)
    first_name = generate_random_string(5)
    payload_all_fields = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    payload_login = {
        "login": login
    }
    payload_password = {
        "password": password
    }
    return payload_all_fields, payload_login, payload_password
