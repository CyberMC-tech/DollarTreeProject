from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (375, 516)  # This is the size of the image you provided

kv = """
<ContentCard@MDCard>:
    orientation: "vertical"
    size_hint: None, None
    size: "280dp", "100dp"
    pos_hint: {"center_x": 0.5}

    MDLabel:
        id: user_label
        text: "MATHEW CONDER\\nNext Shift:\\nSun 1/28 @ 4:30pm-10:30pm"
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Secondary"
        halign: "center"

BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: 'Compass'
        left_action_items: [['menu', lambda x: None]]
        elevation: 10

    ScrollView:
        do_scroll_x: False

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height

            ContentCard:

            MDGridLayout:
                cols: 2
                spacing: "10dp"
                adaptive_height: True
                padding: dp(20), dp(20)

                # Each button is a raised button with an image icon
                MDRaisedButton:
                    text: "Schedule"
                    on_release: app.on_button_press('Schedule')
                    icon: "calendar-blank"

                MDRaisedButton:
                    text: "Timesheet"
                    on_release: app.on_button_press('Timesheet')
                    icon: "clock"

                MDRaisedButton:
                    text: "Time Off"
                    on_release: app.on_button_press('Time Off')
                    icon: "beach"

                MDRaisedButton:
                    text: "Messages (0)"
                    on_release: app.on_button_press('Messages')
                    icon: "message"

                MDRaisedButton:
                    text: "Shift BB"
                    on_release: app.on_button_press('Shift BB')
                    icon: "clipboard-text"

                MDRaisedButton:
                    text: "Availability"
                    on_release: app.on_button_press('Availability')
                    icon: "calendar-check"
"""


class CompassApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(kv)

    def on_button_press(self, button_text):
        print(f"{button_text} button pressed")


CompassApp().run()
