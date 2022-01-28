import adafruit_icm20x
import adafruit_mcp4725
import analogio
import board
import busio
import digitalio

# DEFINE ENUM FOR DEVICE STATES
class State:
    STANDBY = 0
    CALIBRATE = 1
    WALK = 2
    REHAB = 3

# INITIALIZE I/O
def initIO(simuStep):
    # INITIALIZE INPUTS
    simuStep.pot = analogio.AnalogIn(board.A0)
    simuStep.emg = analogio.AnalogIn(board.A1)
    simuStep.btnMode = digitalio.DigitalInOut(board.D9)
    simuStep.btnMode.direction = digitalio.Direction.INPUT
    simuStep.btnMode.pull = digitalio.Pull.UP
    i2c1 = busio.I2C(board.SCL, board.SDA)
    simuStep.imu =  adafruit_icm20x.ICM20649(i2c1)

    # INITIALIZE OUTPUTS
    i2c0 = busio.I2C(board.RX, board.TX)
    simuStep.dac = adafruit_mcp4725.MCP4725(i2c0)
    simuStep.ledPower = digitalio.DigitalInOut(board.D13)
    simuStep.ledPower.direction = digitalio.Direction.OUTPUT
    simuStep.ledBlue = digitalio.DigitalInOut(board.D12)
    simuStep.ledBlue.direction = digitalio.Direction.OUTPUT
    simuStep.ledGreen = digitalio.DigitalInOut(board.D11)
    simuStep.ledGreen.direction = digitalio.Direction.OUTPUT
    simuStep.ledYellow = digitalio.DigitalInOut(board.D10)
    simuStep.ledYellow.direction = digitalio.Direction.OUTPUT

# INITIALIZE STATES
def initStates(simuStep):
    simuStep.deviceState = State.STANDBY
    simuStep.elecFreqState = 0
    simuStep.elecPWState = 0
    simuStep.lowBattery = False