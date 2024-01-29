import requests
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

# Initialize ScreenManager
sm = ScreenManager()


# Application class that inherits from MDApp
class MyApp(MDApp):
    def build(self):
        # Set the theme style and primary color palette
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Light_Green"
        self.theme_cls.accent_hue = "100"

        # Create an instance of Screen
        screen = Screen()

        # Add widgets (Image, Label, TextFields, Buttons) to the screen...

        # (Add your Image, MDLabel, MDTextField widgets here)

        # Sign In Button
        sign_in_button = MDFillRoundFlatButton(
            text="Sign In",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            size_hint=(0.2, None),
            on_release=self.post_login_request,
        )

        # Exit Button
        exit_button = MDFillRoundFlatButton(
            text="Exit",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(0.2, None),
            on_release=self.quit,
        )

        # Button Colors
        sign_in_button.md_bg_color = (5 / 255, 159 / 255, 86 / 255, 1)
        exit_button.md_bg_color = (5 / 255, 159 / 255, 86 / 255, 1)

        # Add buttons to screen
        screen.add_widget(sign_in_button)
        screen.add_widget(exit_button)

        # Add screen to ScreenManager
        sm.add_widget(screen)

        # Create and add DataDisplayScreen
        self.data_display_screen = DataDisplayScreen(name="data_display")
        sm.add_widget(self.data_display_screen)

        return sm

    def quit(self):
        self.stop()

    def post_login_request(self, instance):
        url = "http://127.0.0.1:5000/get_employee_info"
        data = {
            "username": self.username.text,
            "password": self.password.text,
        }
        response = requests.post(url, json=data)
        print(response.text)  # Handle response appropriately


# DataDisplayScreen class...
# (Define the DataDisplayScreen class here)

# Run the app
if __name__ == "__main__":
    MyApp().run()
