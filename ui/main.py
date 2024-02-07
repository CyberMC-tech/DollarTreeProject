import logging

import certifi
import requests
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout


class MyApp(MDApp):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.password = None
        self.username = None
        self.theme_style = "Light"
        self.primary_palette = "Green"

    def build(self):
        self.theme_cls.theme_style = self.theme_style
        self.theme_cls.primary_palette = self.primary_palette

        screen = Screen()
        main_layout = MDBoxLayout(orientation="vertical")



        toolbar = MDTopAppBar(
            title="Compass Mobile"

        screen.add_widget(toolbar)

        background = Image(
            source="../assets/backgrounds/image2.jpg",
            size_hint=(1, 1),
            fit_mode="fill",
            opacity=0.7,
        )

        screen.add_widget(background)

        my_image = Image(
            source="../assets/dollar_tree_no_background.png",
            fit_mode="contain",
            pos_hint={"top": 0.99},
            size_hint=(
                0.98,
                0.25,
            ),
        )

        screen.add_widget(my_image)

        self.username = MDTextField(
            mode="round",
            hint_text="Employee ID",
            helper_text="Same numbers used to clock in",
            helper_text_mode="on_focus",
            icon_right="account",
            pos_hint={"center_x": 0.5, "top": 0.5},
            size_hint=(
                0.75,
                1,
            ),
        )

        screen.add_widget(self.username)

        self.password = MDTextField(
            padding=[
                10,
                10,
                10,
                10,
            ],
            mode="round",
            hint_text="Password",
            helper_text="last 4 of your SSN",
            helper_text_mode="on_focus",
            password=True,
            max_text_length=4,
            icon_right="eye",
            pos_hint={"center_x": 0.5, "top": 0.40},
            size_hint=(
                0.75,
                1,
            ),
        )

        screen.add_widget(self.password)

        sign_in_button = MDFillRoundFlatButton(
            text="Sign In",
            font_size="20dp",
            pos_hint={"center_x": 0.3, "center_y": 1 / 4},
            size_hint=(0.2, None),
            on_release=self.login,
        )

        exit_button = MDFillRoundFlatButton(
            text=" Exit ",
            font_size="20dp",
            pos_hint={"center_x": 0.7, "center_y": 1 / 4},
            width=40,
            size_hint=(0.2, None),
            on_release=lambda x: self.quit_app(),
        )

        sign_in_button.md_bg_color = (5 / 255, 159 / 255, 86 / 255, 1)
        exit_button.md_bg_color = (5 / 255, 159 / 255, 86 / 255, 1)

        screen.add_widget(sign_in_button)
        screen.add_widget(exit_button)

        return screen

    def login(self, obj):
        data = {"username": self.username.text, "password": self.password.text}
        url = "http://164.92.74.220:5000"
        response = requests.post(url, json=data)

        if response.status_code == 200:
            employee_info = response.json()
            print(employee_info)  # Handle the employee info as needed

        """ Makes a POST request to the Compass Mobile API to authenticate a user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            dict: The response from the API.

        Raises:
            requests.exceptions.RequestException: If there is an error making the request.
        """

        # url = "http://164.92.74.220:5000"
        # if len(password) != 4:
        #     return {"status_code": 400, "message": "Password must be 4 characters long"}
        # else:
        #     data = {
        #         "username": username,
        #         "password": password,
        #     }
        #     try:
        #         response = requests.post(url, json=data)
        #         print(response.text)

        # elif response.status_code == 400:
        # raise ValueError("Bad Request: Invalid input data")
        # elif response.status_code == 401:
        #     raise ValueError("Unauthorized: Invalid credentials")
        # elif response.status_code == 403:
        #     raise ValueError("Forbidden: Access denied")
        # elif response.status_code == 404:
        #     raise ValueError("Not Found: Resource not found")
        # else:
        #     raise ValueError("Failed to get employee info")
        # except requests.exceptions.RequestException as e:
        #     logging.error("Error: %s", e)

    # def login_action(self):
    #     response = login(str(self.username.text), str(self.password.text))
    # if response["status_code"] == 400:
    #     self.password.helper_text = response["message"]
    #     self.password.helper_font_color = (1, 0, 0, 1)
    #     self.password.helper_text_mode = "persistent"
    #     self.async_run(self.password.)
    # else:
    # self.theme_cls.theme_style = "Dark"
    # print(response.text)

    def quit_app(self):
        self.stop()


if __name__ == "__main__":
    CompassMobile = MyApp()
    CompassMobile.run()
