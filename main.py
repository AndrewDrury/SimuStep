"""main.py is the first program run when the ItsyBitsy RP2040 is powered on"""
from typing import Protocol
import adafruit_icm20x
import analogio
import board
import digitalio
import time

import helper
import init
import io
import states
from states import State

# Initialize Inputs, Outputs, and States
init.initIO()
init.initStates()

# Start main loop
while True:
    time.sleep(1)
