from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from tools.helpers import (
    extract_name,
    extract_address,
    extract_phone_number,
    extract_id,
    extract_store_number,
    extract_position,
)

app = Flask(__name__)

info_popup_xpath = "/html/body/div/div[1]/div[2]/div/div/table/tbody/tr/td[1]/h6/a"


class Employee:
    """
    A class to represent a Dollar Tree employee.

    Attributes:
        driver (webdriver): A Selenium WebDriver instance used to interact with the Dollar Tree website.
    """

    def __init__(self):
        """
        Initialize a new Employee instance.
        """
        self.position = None
        self.store_number = None
        self.phone_number = None
        self.address = None
        self.id = None
        self.next_shift = None
        self.full_name = None
        self.last_name = None
        self.first_name = None
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def login(self, username: str, password: str):
        """
        Login to the Dollar Tree website using the given username and password.

        Args:
            username (str): The username used to login to the Dollar Tree website.
            password (str): The password used to login to the Dollar Tree website.
        """
        self.driver.get("https://compassmobile.dollartree.com")
        username_field = self.driver.find_element(By.ID, "idUNField")
        password_field = self.driver.find_element(By.ID, "idPWField")

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def get_next_shift(self):
        """
        Get the next shift for the currently logged in employee.
        """
        css_selector = "div#cardToggleIcon1 > div > table > tbody > tr > td > div:nth-of-type(2) > a"
        self.next_shift = self.driver.find_element(By.CSS_SELECTOR, css_selector).text

    def get_employee_info(self):
        """
        Get information about the currently logged in employee.
        """
        info_popup = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, info_popup_xpath))
        )

        info_popup.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "empInfoModal"))
        )

        popup_body = self.driver.find_element(
            By.XPATH, "//div[@id='empInfoModal']//div[@class='modal-body']"
        )
        employee_data = popup_body.find_elements(By.TAG_NAME, "li")

        employee_name = employee_data[0].text
        address = employee_data[1].text
        phone_number = employee_data[2].text
        id = employee_data[3].text
        store_number = employee_data[4].text
        position = employee_data[5].text

        self.first_name, self.last_name = extract_name(employee_name)
        self.full_name = f"{self.first_name} {self.last_name}"
        self.address = extract_address(address)
        self.phone_number = extract_phone_number(phone_number)
        self.id = extract_id(id)
        self.store_number = extract_store_number(store_number)
        self.position = extract_position(position)

    def return_data(self) -> dict:
        """
        Return a dictionary containing information about the currently logged in employee.

        Returns:
            dict: A dictionary containing information about the currently logged in employee.
        """
        return {
            "full_name": self.full_name,
            "next_shift": self.next_shift,
            "phone_number": self.phone_number,
            "address": self.address,
            "store_number": self.store_number,
            "position": self.position,
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }


"""
This function is used to extract information about the currently logged in employee.

Args:
    username (str): The username used to login to the Dollar Tree website.
    password (str): The password used to login to the Dollar Tree website.

Returns:
    dict: A dictionary containing information about the currently logged in employee.
"""


@app.route("/", methods=["POST"])
def get_employee_info_api():
    content = request.json
    username = content["username"]
    password = content["password"]

    employee = Employee()
    employee.login(username, password)
    employee.get_next_shift()
    employee.get_employee_info()
    employee_info = employee.return_data()

    return jsonify(employee_info)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
