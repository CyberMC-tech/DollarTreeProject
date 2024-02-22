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
    return f"{street_name_number} {city_state_zip}"


def extract_phone_number(data):
    split_data = data.split("\n")
    return split_data[1]


def extract_id(data):
    first_line = data.split("\n")[0]
    return first_line.split(": ")[1]


def extract_store_number(data):
    split_data = data.split("\n")[1]
    return split_data.split(" ")[1]


def extract_position(data):
    return data.split("\n")[1]
