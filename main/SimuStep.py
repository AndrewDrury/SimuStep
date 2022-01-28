# DEFINE ENUM FOR DEVICE STATES
class State:
    STANDBY = 0
    CALIBRATE = 1
    WALK = 2
    REHAB = 3

class SimuStep():
    def __init__(
        self,
        # btnMode,
        # emg,
        # imu,
        # pot,
        # dac,
        # ledPower,
        # ledBlue,
        # ledGreen,
        # ledYellow,
        # deviceState,
        # elecFreqState,
        # elecPWState,
        # lowBatteryState,
    ):
        pass
        # self.btnMode = btnMode
        # self.emg = emg
        # self.imu = imu
        # self.pot = pot
        # self.dac = dac
        # self.ledPower = ledPower
        # self.ledBlue = ledBlue
        # self.ledGreen = ledGreen
        # self.ledYellow = ledYellow
        # self.deviceState = deviceState
        # self.elecFreqState = elecFreqState
        # self.elecPWState = elecPWState
        # self.lowBatteryState = lowBatteryState

    # Print all Inputs
    def printInputs(self):
        inputValues= [
            ['btnMode', self.btnMode.value],
            # ['emg', io.emg.value],
            ['imu acc (m/s^2)', self.imu.acceleration],
            ['imu gyro (deg/s)', self.imu.gyro],
            ['pot', self.pot.value],
        ]

        print('-'*24)
        print('INPUTS')
        self.printTable(inputValues)
        
    # Print all Outputs
    def printOutputs(self):
        outputValues= [
            ['dac', self.dac.value],
            ['ledPower', self.ledPower.value],
            ['ledBlue', self.ledBlue.value],
            ['ledGreen', self.ledGreen.value],
            ['ledYellow', self.ledYellow.value],
        ]

        print('-'*24)
        print('OUTPUTS')
        self.printTable(outputValues)

    # Print all States
    def printStates(self):
        stateValues= [
            ['deviceState', self.deviceState],
            ['elecFreqState', self.elecFreqState],
            ['elecPWState', self.elecPWState],
            ['lowBattery', self.lowBattery],
        ]

        print('-'*24)
        print('STATES')
        self.printTable(stateValues)

    # Format output in a table
    def printTable(self, table):
        for row in table:
            print("{:<16} {:<16}".format(row[0], str(row[1])))

    def switchMode(self):
        self.ledBlue.value = False
        self.ledGreen.value = False
        self.ledYellow.value = False

        if self.deviceState == State.REHAB:
            self.deviceState = State.STANDBY
        else:
            self.deviceState += 1
        
        if self.deviceState == State.CALIBRATE:
            self.ledBlue.value = True
        elif self.deviceState == State.WALK:
            self.ledGreen.value = True
        elif self.deviceState == State.REHAB:
            self.ledYellow.value = True


# # INPUTS
# btnMode # Mode-changing button
# emg     # EMG Sensor
# imu     # IMU Sensor
# pot     # Potentiometer

# # OUTPUTS
# dac         # DAC - output to electrodes
# ledPower    # Power LED - indicating the power state of the device
# ledBlue     # Blue LED - indicating calibration mode
# ledGreen    # Green LED - indicating walking mode
# ledYellow   # Yellow LED - indicating rehabilitation mode

# # STATES
# deviceState         # State of the device (standby | calibrate | walk | rehab)
# elecFreqState       # Frequency of the electrodes
# elecPulseWidthState # Pulse width of the electrodes
# lowBatteryState     # Low battery state