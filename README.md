# SimuStep
This repository contains the code for SimuStep, a fourth year Mechatronics capstone design project at the University of Waterloo. SimuStep is a device that helps people with foot drop (inability to lift the foot) walk by using electrical stimulation.

## Setup
You only need to follow these steps once.

1. Connect the microcontroller to your PC via USB
2. Download [Mu](https://codewith.mu/), a python editor used to program Adafruit CircuitPython boards. Make sure to select `CircuitPython` as the mode when starting Mu.
3. Hold down the `boot/bootsel` button on the board while clicking the `reset` button. Continue to hold down the `boot/bootsel` until the bootloader driver appears.
4. The status LED on the board should flash red and stay green and the device should show up on the PC as a `RPI-RP2` drive.
5. Download [CircuitPython 7.x.x](https://circuitpython.org/board/adafruit_itsybitsy_rp2040/) for Adafruit ItsyBitsy RP2040 microcontroller and add the file to the `RPI-RP2` drive.
6. The LED should flash again and `RPI-RP2` should be replaced by `CIRCUITPY` drive on your PC.
7. Clone this repo to your PC with `git clone git@github.com:AndrewDrury/SimuStep.git`

## Run Code
1. Open `SimuStep/code.py` in the Mu python editor.
2. Click `Load` to load the code onto the microcontroller.
3. Click `Run` to run the code on the microcontroller.