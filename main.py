from kivy.app import App
from kivy.uix.label import Label

class ICBM(App):
    def build(self):
        return Label(text="ICBM OK")

ICBM().run()