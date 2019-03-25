# OC Maker Challenge ![](./res/img/oc_maker.png "OC Maker")
### ```"Design and build, or significantly repurpose, a product that will solve a problem, need or want."```
#### Our project:
To innovate an instrument and make it more useful. We will 3D-print a clarinet shaped instrument. It will have push buttons on it representing keys. The buttons will be controlled by a Raspberry Pi 3 B+. These buttons will be rearrangeable and what note they play will be customizable through our included Android app. The sound from the notes will go straight to your phone and from there anywhere you want. (Speakers, earbuds, etc.)

#### How it Helps:
- It makes it so you don't have to lug around your priceless instrument, instead, you can just bring this.
- If you're somewhere that needs to be quiet, or you don't want to annoy people with your loud instrument, just bring this and use earbuds

#### Goals:
- [ ] 3D print the parts for the instrument and assemble them.
- [ ] Hook up all of the buttons to a Raspberry Pi 3 B+
- [ ] Program the Pi to sense the button presses and communicate with your phone via Bluetooth
- [ ] Create the Android app to:
  1. Adjust the output volume
  2. Change the output source
  3. Adjust what button plays what note

#### Materials:
- [x] __Raspberry Pi 3 B+__: To handle button presses and communicate with app
- [x] __24-32 wires__: to connect buttons to Pi
- [x] __12-16 10k resistors__: To limit the power that the push buttons give to the GPIO (General Purpose Input Output)
- [x] __Breadboard__: an easy way to connect the circuitry
- [ ] __12-16 digital buttons__ *(currently have about 8)*: To provide communication between the instrument player and the Pi

#### 3rd Party Libraries / Programming Languages:
- [__Python__](https://python.org): To be used on the Raspberry Pi to handle button presses and Pi-App communication
  - [__PyBluez__](https://pypi.org/project/PyBluez/): Used for python to send bluetooth signals to the App
  - [__GPIO Zero__](https://pypi.org/project/gpiozero/): Used to detect button presses
  - [Kivy](https://kivy.org): Used to create the UI of the android app
  - [Buildozer](https://pypi.org/project/buildozer): Used to build the android app out of python scripts.

#### Software:
- [Atom](https://atom.io): Used as an editor for the python code
- [Autodesk Inventor 2016](https://www.autodesk.com/products/inventor/overview): Used to create the 3D model of our product
