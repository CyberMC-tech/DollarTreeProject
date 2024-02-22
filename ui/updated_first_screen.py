from dataclasses import dataclass
from threading import Thread
from typing import Optional

import requests
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager


@dataclass
class Employee:
    """
    A data class used to hold information about an employee.

    Args:
        first_name (Optional[str]): The employee's first name
        last_name (Optional[str]): The employee's last name
        full_name (Optional[str]): The employee's first and last name.
        address (Optional[str]): The adderess on file for the employee.
        id (Optional[str]): The employee's user id number.
        next_shift (Optional[str]): The employee's next scheduled shift.
        phone_number (Optional[str]):  The employee's phone number on file.
        position (Optional[str]): The employee's position with the company.
        store_number (Optional[str]): The store number for the employee's home store.
    """

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    address: Optional[str] = None
    id: Optional[str] = None
    next_shift: Optional[str] = None
    phone_number: Optional[str] = None
    position: Optional[str] = None
    store_number: Optional[str] = None


# Create a global instance of the employee.
employee = Employee()


class AppScreenManager(MDScreenManager):
    pass


class LoginScreen(MDScreen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login(self):

        # Move network call to a background thread
        login_thread = Thread(target=self.perform_login).start()

    """Performs login request to server and handles response.
    
    Sends username and password to provided URL. On 200 response, extracts 
    user info from response and stores first name, last name, and full name.
    
    Handles non-200 responses and network errors.
    """

    def perform_login(self):
        username = self.ids.username_field.text
        password = self.ids.password_field.text

        data = {"username": username, "password": password}
        url = "http://164.92.74.220:5000"
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                employee_info = response.json()
                employee = Employee(**employee_info)
                # print(employee)
                Clock.schedule_once(lambda dt: self.set_employee_info(employee), 0)
                return employee

        except requests.RequestException:
            Clock.schedule_once(
                lambda dt: toast(
                    "Network error occurred.\n Please try again later.", duration=3.5
                ),
                0,
            )
            # TODO: Run the next line of code after the above lambda is complete.
            self.ids.login_button.text = "Login"

    def set_employee_info(self, info):
        home_screen = self.manager.get_screen("home_screen")
        home_screen.employee = info
        CompassMobile.get_running_app().root.current = "home_screen"


class HomeScreen(MDScreen):
    """
    Home Screen class for Compass Mobile App.

    This class contains the code for the Home Screen of the app, which displays the next shift for the user's current shift.

    Attributes:
        employee (ObjectProperty): Object property that holds the user's employee information.
    """

    employee = ObjectProperty(
        None,
    )

    def on_employee(self, instance, value):
        """
        Event handler for when the employee property changes.

        This method updates the welcome label on the screen with the user's next shift information.

        Args:
            value (Employee): The new employee information.
            :param value:
            :param instance:
        """
        self.ids.welcome_label.text = (
            f"Hello {value.first_name},\n \n Your next shift is {value.next_shift}"
        )


screen_manager = AppScreenManager()


class CompassApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        Builder.load_file("updated_first_screen.kv")
        screen_manager.add_widget(LoginScreen(name="login_screen"))
        screen_manager.add_widget(HomeScreen(name="home_screen"))
        return screen_manager

    def quit(self):
        self.stop()

    def open_home_screen(self):
        pass


if __name__ == "__main__":
    CompassMobile = CompassApp()
    CompassMobile.run()
