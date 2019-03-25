from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

from bluetooth import *

from Application import Application

def Start(dt):
    portahorn.application.current = "loading_find_bt"
    devices=find_bluetooth()
    if(len(devices) == 1):
        portahorn.application.ids.load_sc.text = "Found " + str(len(devices))
        portahorn.sock = BluetoothSocket( RFCOMM )
        portahorn.sock.connect((devices[0]["host"], devices[0]["port"]))
        Clock.schedule_interval(lambda dt: read_bt(), 1.0/30.0)

def read_bt():
    data = portahorn.sock.recv(1024)
    print("Received %s" % data)

class PortahornApp(App):
    def build(self):
        Clock.schedule_once(Start, 1.0)
        self.application = Application()
        return self.application


def find_bluetooth():
    uuid="a7317d48-cf0f-4b8c-8899-c2b9184964ea"
    print("Finding the Portahorn service at UUID: %s..." % uuid)

    service_matches = find_service( uuid = uuid )

    if len(service_matches) == 0:
            print("Unable to find the Portahorn service!")
            exit(0)

    print("Found Portahorn service!")

    return service_matches

portahorn = PortahornApp()
portahorn.run()
