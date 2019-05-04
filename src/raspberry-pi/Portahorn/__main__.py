from bluetooth import *
from gpiozero import Button
from signal import pause

button1 = Button(17) # Can't get pin 1 to work
button2 = Button(2)
button3 = Button(3)
button4 = Button(4)
button5 = Button(5)
button6 = Button(6)
button7 = Button(7)
button8 = Button(8)

sock=BluetoothSocket(RFCOMM)
sock.bind(("",PORT_ANY))
sock.listen(1)

port = sock.getsockname()[1]

uuid = "a7317d48-cf0f-4b8c-8899-c2b9184964ea"

advertise_service( sock, "Portahorn",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ]
)

print("Waiting to connect to RFFCOM Channel: {0}".format(port))

client, info = sock.accept()
print("Accepted connection from: {0}".format(info))

def buttonPress(button):
    pin = button.pin.number
    if pin == 17:
        pin = 1
    print("Button %d pressed", pin)
    client.send(str(button.pin)+"_1")
def buttonRelease(button):
    pin = button.pin.number
    if pin == 17:
        pin = 1
    print("Button %d released", pin)
    client.send(str(button.pin)+"_0")

on = False
button1.when_pressed = buttonPress
button1.when_released = buttonRelease
button2.when_pressed = buttonPress
button2.when_released = buttonRelease
button3.when_pressed = buttonPress
button3.when_released = buttonRelease
button4.when_pressed = buttonPress
button4.when_released = buttonRelease
button5.when_pressed = buttonPress
button5.when_released = buttonRelease
button6.when_pressed = buttonPress
button6.when_released = buttonRelease
button7.when_pressed = buttonPress
button7.when_released = buttonRelease
button8.when_pressed = buttonPress
button8.when_released = buttonRelease

pause()

client.close()
sock.close()
print("Disconnected")
