import adafruit_icm20x
import analogio
import board
import digitalio

import io
import states
from states import State

# INITIALIZE I/O
def initIO():
    # INITIALIZE INPUTS
    io.pot = analogio.AnalogIn(board.A1)
    io.emg = analogio.AnalogIn(board.A0)
    io.btnMode = digitalio.DigitalInOut(board.D9)
    io.btnMode.direction = digitalio.Direction.INPUT
    io.btnMode.pull = digitalio.Pull.UP
    i2c = board.I2C()
    io.imu =  adafruit_icm20x.ICM20649(i2c)

    # INITIALIZE OUTPUTS
    io.ledBlue = digitalio.DigitalInOut(board.D10)
    io.ledBlue.direction = digitalio.Direction.OUTPUT
    io.ledGreen = digitalio.DigitalInOut(board.D11)
    io.ledGreen.direction = digitalio.Direction.OUTPUT
    io.ledYellow = digitalio.DigitalInOut(board.D12)
    io.ledYellow.direction = digitalio.Direction.OUTPUT
    io.ledPower = digitalio.DigitalInOut(board.D13)
    io.ledPower.direction = digitalio.Direction.OUTPUT
    io.ledPower = digitalio.DigitalInOut(board.D24)
    io.ledPower.direction = digitalio.Direction.OUTPUT

# INITIALIZE STATES
def initStates():
    # INITIALIZE STATES
    states.deviceState = State.STANDBY
    states.elecFreqState = 0
    states.elecPulseWidthState = 0
    states.lowBattery = False