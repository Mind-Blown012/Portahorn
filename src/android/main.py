from threading import Thread

from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.config import Config
from bluetooth import *


Config.set('graphics', 'fullscreen', 0)
Config.set('graphics','show_cursor', 0)
Config.write()

first_sound = True
last_notes = None
note_name = "None"
time = 20

notes = [
[ SoundLoader.load("res/sounds/a.wav"), SoundLoader.load("res/sounds/a.wav") ],
[ SoundLoader.load("res/sounds/b.wav"), SoundLoader.load("res/sounds/b.wav") ],
[ SoundLoader.load("res/sounds/c.wav"), SoundLoader.load("res/sounds/c.wav") ],
[ SoundLoader.load("res/sounds/d.wav"), SoundLoader.load("res/sounds/d.wav") ],
[ SoundLoader.load("res/sounds/e.wav"), SoundLoader.load("res/sounds/e.wav") ],
[ SoundLoader.load("res/sounds/f.wav"), SoundLoader.load("res/sounds/f.wav") ],
[ SoundLoader.load("res/sounds/g.wav"), SoundLoader.load("res/sounds/g.wav") ]
]

def PlayNote(notes_arg):
    global first_sound
    global last_notes
    global time
    global note_name
    MainApplication.lab.txt = note_name
    if notes_arg is None and last_notes is not None:
        if first_sound:
            last_notes[1].stop()
        else:
            last_notes[0].stop()
        return
    if notes_arg is None:
        return
    else:
        if last_notes == None:
            time = 20
        if last_notes != notes_arg and last_notes != None:
            last_notes[0].stop()
            last_notes[1].stop()
        if time > 18:
            time = 0
            if first_sound:
                first_sound = False
                notes_arg[0].play()
            else:
                first_sound = True
                notes_arg[1].play()
        else:
            time+=1
    last_notes = notes_arg

def get_note():
    global pressed_buttons
    global note_name
    print(pressed_buttons)
    if set([7]) == pressed_buttons:
        note_name = "C"
        return notes[2] # C
    elif set([8]) == pressed_buttons:
        note_name = "B"
        return notes[1] # B
    elif set([8, 7]) == pressed_buttons:
        note_name = "A"
        return notes[0] # A
    elif set([8, 7, 6]) == pressed_buttons:
        note_name = "G"
        return notes[6] # G
    elif set([8, 7, 6, 5]) == pressed_buttons:
        note_name = "F"
        return notes[5] # F
    elif set([8, 7, 6, 5, 4]) == pressed_buttons:
        note_name = "E"
        return notes[4] # E
    elif set([8, 7, 6, 5, 4, 3]) == pressed_buttons:
        note_name = "D"
        return notes[3] # D
    else:
        note_name = "None"

def find_bluetooth():
    global shutdown
    global sock
    # The uuid of the raspberry pi
    uuid="a7317d48-cf0f-4b8c-8899-c2b9184964ea"
    print("Finding a Portahorn near you...")

    service_matches = find_service( uuid = uuid )


    if len(service_matches) == 0:
        print("Unable to find a Portahorn!")
        exit(0)

    print("Found a Portahorn!")

    # Use the first one found
    device = service_matches[0]
    sock = BluetoothSocket( RFCOMM )
    sock.connect((device["host"], device["port"]))
    print("Sucessfully Connected!")
    MainApplication.lab.txt = "None"
    if not shutdown:
        Clock.schedule_once(lambda dt: MainApplication.loop_t.start(), 0.1)

def get_button():
    global sock
    global pressed_buttons
    _data = str(sock.recv(1024))
    data = _data.split("_")
    button = int(''.join(c for c in data[0] if c not in "GPIO'b"))
    print(button)
    _on = int(''.join(c for c in data[1] if c not in "'b"))
    on = (_on == 1)
    if on:
        if not (button in pressed_buttons):
            pressed_buttons.add(button)
    else:
        if button in pressed_buttons:
            pressed_buttons.remove(button)

# The main loop of the application
def looper():
    loop_started = True
    Clock.schedule_interval(lambda dt: PlayNote(get_note()), 0.05)
    while (not shutdown):
        get_button()

class mylabel(Label):
    txt = StringProperty("Connecting...")
    def __init__(self, **kwargs):
        self.bind(txt=self.txt_chg)
        self.text = self.txt
        self.font_size = 75
        super(mylabel, self).__init__(**kwargs)

    def txt_chg(self, instance, value):
        self.text = value

class PortahornApp(App):
    lab = None
    def build(self):
        self.lab = mylabel()
        return self.lab
    # Will be called when the application starts running
    def on_start(self):
        self.find_bt_t =  Thread(target=find_bluetooth)
        self.loop_t = Thread(target=looper)
        # Set BluetoothDevice on the next frame so that
        # it does not interrupt the GUI.
        Clock.schedule_once(lambda dt: self.find_bt_t.start(), 0.1)

    def on_stop(self):
        global shutdown
        shutdown = True
        # Make sure that the main thread waits for looper to finish
        self.find_bt_t.join()
        if loop_started:
            self.loop_t.join()

# Defining main global variables
MainApplication = PortahornApp()
pressed_buttons = set()
loop_started = False
shutdown = False
sock = None

if __name__ == '__main__':
    MainApplication.run()
