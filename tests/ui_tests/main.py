from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class ScheduleScreen(MDScreen):
    pass


class WorkScheduleApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = (
            "Green"  # Adjust the primary color to match the screenshot
        )
        return ScheduleScreen()


WorkScheduleApp().run()
