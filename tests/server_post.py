import requests

username = input("Username: ")
password = input("Password: ")


url = "http://164.92.74.220:5000"
data = {"username": username, "password": password}

response = requests.post(url, json=data)
print(response.text)
