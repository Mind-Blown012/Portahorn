from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

from bluetooth import *

from Application import Application

pressed_buttons = set()
# NOTE_A = SoundLoader.load("a.wav")
# NOTE_A = SoundLoader.load("a.wav")
# NOTE_A = SoundLoader.load("a.wav")
# NOTE_A = SoundLoader.load("a.wav")
# NOTE_A = SoundLoader.load("a.wav")
# NOTE_A = SoundLoader.load("a.wav")
# NOTE_A = SoundLoader.load("a.wav")
notes = { 'a':set([0,1]),'b':set([0]),'c':set([1]),'d':set([0,1,2,3,4,5,6]), 'e':set([0,1,2,3,4,5]), 'f':set([0,1,2,3,4]), 'g':set([0,1,2,3]) }

def Start(dt):
    devices=find_bluetooth()
    for addr, name in devices:
        print("%s - %s" % (addr, name))

    if(len(devices) == 1):
        portahorn.sock = BluetoothSocket( RFCOMM )
        portahorn.sock.connect((devices[0]["host"], devices[0]["port"]))
        Clock.schedule_interval(lambda dt: get_button(), 1.0/30.0)
        Clock.schedule_interval(lambda dt: play_sound(), 1.0/10.0)

def play_sound():
    global last_note
    note = get_note()

    if note is not last_note:
        print(note)

    last_note = note

def get_note():
    for key, value in notes:
        if pressed_buttons is value:
            return key
    return None

def get_button():
    data = portahorn.sock.recv(1024)
    data = data.split("_")
    button = data[0]
    on = (data[1] == 1)
    if on:
        if not (button in pressed_buttons):
            pressed_buttons.add(button)
    else:
        if button in pressed_buttons:
            pressed_buttons.remove(button)

class PortahornApp(App):
    def build(self):
        Clock.schedule_once(Start, 1.0)
        self.application = Application()
        return None


def find_bluetooth():
    uuid="a7317d48-cf0f-4b8c-8899-c2b9184964ea"
    print("Finding the Portahorn service at UUID: %s..." % uuid)

    # service_matches = find_service( uuid = uuid )
    service_matches = discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)


    # if len(service_matches) == 0:
    #         print("Unable to find the Portahorn service!")
    #         exit(0)

    print("Found Portahorn service!")

    return service_matches

portahorn = PortahornApp()
portahorn.run()
