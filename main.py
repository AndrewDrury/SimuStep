"""main.py is the first program run when the ItsyBitsy RP2040 is powered on"""
from typing import Protocol
import adafruit_icm20x
import analogio
import board
import digitalio
import time

# DEFINE ENUM FOR DEVICE STATES
class State:
    STANDBY = 0
    CALIBRATE = 1
    WALK = 2
    REHAB = 3

# DEFINE INPUTS
pot     # Potentiometer
emg     # EMG Sensor
imu     # IMU Sensor
btnMode # Mode-changing button

# DEFINE OUTPUTS
ledBlue     # Blue LED - indicating calibration mode
ledGreen    # Green LED - indicating walking mode
ledYellow   # Yellow LED - indicating rehabilitation mode
ledPower    # Power LED - indicating the power state of the device
electrodes  # 2 Electrodes (top and bottom)

# DEFINE STATES
deviceState         # State of the device (standby | calibrate | walk | rehab)
elecFreqState       # Frequency of the electrodes
elecPulseWidthState # Pulse width of the electrodes
lowBattery          # Low battery state

# INITIALIZE I/O AND STATES
def init():
    # INITIALIZE INPUTS
    pot = analogio.AnalogIn(board.A1)
    emg = analogio.AnalogIn(board.A0)
    btnMode = digitalio.DigitalInOut(board.D9)
    btnMode.direction = digitalio.Direction.INPUT
    btnMode.pull = digitalio.Pull.UP
    i2c = board.I2C()
    imu =  adafruit_icm20x.ICM20649(i2c)

    # INITIALIZE OUTPUTS
    ledBlue = digitalio.DigitalInOut(board.D10)
    ledBlue.direction = digitalio.Direction.OUTPUT
    ledGreen = digitalio.DigitalInOut(board.D11)
    ledGreen.direction = digitalio.Direction.OUTPUT
    ledYellow = digitalio.DigitalInOut(board.D12)
    ledYellow.direction = digitalio.Direction.OUTPUT
    ledPower = digitalio.DigitalInOut(board.D13)
    ledPower.direction = digitalio.Direction.OUTPUT
    ledPower = digitalio.DigitalInOut(board.D24)
    ledPower.direction = digitalio.Direction.OUTPUT

    # INITIALIZE STATES
    deviceState = State.STANDBY
    elecFreqState = 0
    elecPulseWidthState = 0
    lowBattery = False

init()

while True:
    time.sleep(1)
