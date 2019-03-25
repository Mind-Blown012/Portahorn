from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty

class Application(ScreenManager):
    pass

class DevicesScreen(Screen):
    def register_device(instance=None, device=None):
        pass

class LoadingScreen(Screen):
    text = StringProperty()


class BTDeviceButton(Button):
    def __init__(self, device, **kwargs):
        self.device = device
        self.text = device["name"]
        super(BTDeviceButton, self).__init__(**kwargs)
