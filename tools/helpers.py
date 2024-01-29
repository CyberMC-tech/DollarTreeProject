# helpers.py


def extract_name(data):
    name = data.split(" ")
    first_name = name[0].capitalize()
    last_name = name[1].capitalize()
    return first_name, last_name


def extract_address(data):
    split_data = data.split("\n")
    street_name_number = split_data[1]
    city_state_zip = split_data[2]
    full_address = f"{street_name_number} {city_state_zip}"
    return full_address


def extract_phone_number(data):
    split_data = data.split("\n")
    phone_number = split_data[1]
    return phone_number


def extract_id(data):
    first_line = data.split("\n")[0]
    employee_id = first_line.split(": ")[1]
    return employee_id


def extract_store_number(data):
    split_data = data.split("\n")[1]
    store_number = split_data.split(" ")[1]
    return store_number


def extract_position(data):
    employee_position = data.split("\n")[1]
    return employee_position
