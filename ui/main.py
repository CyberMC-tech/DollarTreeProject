import requests
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField

# sm = ScreenManager


# Define an application class that inherits from MDApp class of the KivyMD library
class MyApp(MDApp):
    # Define the build function, this function is automatically called by the application
    # to build the User Interface (UI) of the application

    def post_login_request(self, instance):
        url = "http://127.0.0.1:5000/get_employee_info"
        data = {
            "username": str(self.username.text),
            "password": str(self.password.text),
        }
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                employee_info = response.json()
                print(employee_info)  # Handle the employee info as needed
            else:
                print("Failed to get employee info")
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def build(self):
        # TODO: Add in functionality to change between light and dark
        # Set the theme style to 'Dark'
        self.theme_cls.theme_style = "Light"

        # Set the primary color palette to 'LightGreen'
        self.theme_cls.primary_palette = "LightGreen"

        # Create an instance of Screen class, to hold other widgets
        screen = Screen
        # Create an instance of Image widget and set properties
        my_image = Image(
            source="../assets/dollar_tree_no_background.png",  # Path to the image source
            # Allow the image to stretch (fill) the whole widget area
            fit_mode="contain",
            pos_hint={
                "top": 0.99
            },  # Specify the relative position for the top edge: 0.99 = 99% from the top
            size_hint=(
                0.98,
                0.25,
            ),  # Set the size of widget relative to its parent: 98% width and 25% height
        )

        # Add the image widget to the screen
        screen.add_widget(screen, my_image)

        # Create an instance of a Label and set properties, Label is a widget used to display text
        info = MDLabel(
            text="The username and password fields of this app are not currently functioning.\n"
            "Click the Sign In button to continue.",  # The text that will be displayed
            theme_text_color="Custom",
            # The color of the text will be set by the colors defined by the text_color property
            text_color=(
                1,
                0,
                0,
                1,
            ),  # Set the color of the text in (R, G, B, A) format.
            halign="center",  # Align the text horizontally in the center
            pos_hint={"bottom": 1},
            # Specify the relative position for the bottom edge: 1 = bottom edge corresponds to bottom edge of the parent
            size_hint=(
                1,
                0.25,
            ),  # Set the size of the widget to be 100% width and 25% height of the parent screen
        )

        # Add the label to the screen
        screen.add_widget(info)

        # Create a TextField for Username and set properties
        self.username = MDTextField(
            # Placeholder text that appears when there is no input in the TextField
            mode="round",
            hint_text="Employee ID",
            helper_text="Numbers used to clock in",  # The small text below the TextField
            helper_text_mode="persistent",
            # When the "helper_text" will be visible. In this case, it will be visible when the TextField is focused on.
            icon_right="account",  # Set the icon displayed on the right side of the text field
            pos_hint={"center_x": 0.5, "top": 0.5},
            # Position hint: center X of the textfield should be at the center (0.5=50%) and top should be in the middle (0.5=50%) of the screen
            size_hint=(
                0.75,
                1,
            ),  # Set the size of the widget to be 50% width and 100% height of the parent screen
        )

        # Add the username TextField to the screen
        screen.add_widget(self.username)

        # Create a TextField for Password and set properties
        self.password = MDTextField(
            padding=[
                10,
                10,
                10,
                10,
            ],  # Set the padding inside the widget from all four sides
            mode="round",
            hint_text="Password",  # Placeholder text to display when the TextField is empty
            helper_text="Usually the last 4 of your SSN",  # Any helper text (not visible in this case)
            password=True,  # The TextField is a password field that hides the input
            icon_right="eye",  # Set the icon displayed on the right side of the text field
            pos_hint={"center_x": 0.5, "top": 0.40},
            # Position hint: center X of the textfield should be at the center (0.5=50%) and top should be somewhat below middle (0.4=40%) of the screen
            size_hint=(
                0.75,
                1,
            ),  # Set the size of widget relative to its parent: 50% width and 100% height
        )

        # Disable the password TextField
        # password.disabled = True

        # Add the password TextField to the screen
        screen.add_widget(self.password)

        # Create a Round Flat Button and set properties
        sign_in_button = MDFillRoundFlatButton(
            text="Sign In",
            pos_hint={"center_x": 0.375, "center_y": 1 / 4},
            # Position the button to where it's center is at 3/8th of the width of its parent.
            # And it's center height is at 1/4 of the height of its parent
            size_hint=(0.2, None),
            # Set the width of the button to be 20% of the parent screen width, 'None' for height implies button will take the minimum size needed.
            # on_release=lambda x: webbrowser.open('https://compassmobile.dollartree.com/')  # Action to perform when button clicked, in this case, open a website
            on_release=self.post_login_request,
        )

        exit_button = MDFillRoundFlatButton(
            text="Exit",
            pos_hint={"center_x": 0.625, "center_y": 1 / 4},
            # Position the button to be at 30% from left and at 4/5th position from the bottom of the screen
            size_hint=(0.2, None),
            # Set the width of the button to be 20% of the parent screen width, 'None' for height implies button will take the minimum size needed.
            # on_release=
            # Action to perform when button clicked, in this case, closes the application.
        )

        # Change the background color of the button to be the correct color green
        sign_in_button.md_bg_color = (5 / 255, 159 / 255, 86 / 255, 1)
        exit_button.md_bg_color = (5 / 255, 159 / 255, 86 / 255, 1)

        # Add the button to the screen
        screen.add_widget(sign_in_button)
        screen.add_widget(exit_button)

        # Return the screen which will be displayed when app runs
        return screen

    def quit(self):
        MyApp.quit()

    def post_login_request(self, instance):
        url = "http://127.0.0.1:5000/get_employee_info"
        data = {
            "username": str(
                self.username.text
            ),  # Get the text from the username input field
            "password": str(
                self.password.text
            ),  # Get the text from the password input field
        }
        # Perform the POST request
        response = requests.post(url, json=data)
        print(response.text)  # Print the response text to the console


# Python's way of running the main script.
if __name__ == "__main__":
    # Create an instance of MyApp and run the app
    MyApp().run()
