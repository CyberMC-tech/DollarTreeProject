import requests


def login_request():
    url = "http://localhost:5000/get_employee_info"

    data = {"username": "27606069", "password": "5422"}

    response = requests.post(url, json=data)
    print(response.text)
