# SimuStep CLASS - defining the device and helper functions

# INPUTS
# btnMode # Mode-changing button
# imu     # IMU Sensor
# pot     # Potentiometer

# OUTPUTS
# dac         # DAC - output to electrodes
# ledPower    # Power LED - indicating the power state of the device
# ledBlue     # Blue LED - indicating calibration mode
# ledGreen    # Green LED - indicating walking mode
# ledYellow   # Yellow LED - indicating rehabilitation mode

# STATES
# deviceState         # State of the device (standby | calibrate | walk | rehab)
# lowBatteryState     # Low battery state

import time

from CONSTANTS import ELECTRODE_FREQ, ELECTRODE_PW, ELECTRODE_DUTYCYCLE

# Defin enum for device states
class State:
    STANDBY = 0
    CALIBRATE = 1
    WALK = 2
    REHAB = 3

# SimuStep class - defining the device and helper functions
class SimuStep():
    def __init__(self):
        pass

    # Activate electrodes - used for all modes
    def activateElectrodes(self):
        self.dac.normalized_value = self.intensity

        # # CUSTOM IMPLEMENTATION PULSE WIDTH MODULATION
        # # print('Intensity: ', self.intensity)

        # periodTime = int(1/ELECTRODE_FREQ * 10000) # Time for one period in 10^-4 seconds
        # q
        #     # print('DUTYCYCLEss', ELECTRODE_DUTYCYCLE)
        #     # print('periodTime', periodTime)

        #     # cycleTime is current microseconds in period
        #     for cycleTime in (cycleTime for cycleTime in range(0, periodTime) if not self.btnMode.value):
        #         # print(self.dac.normalized_value)
        #         # print(cycleTime)
        #         print((self.dac.normalized_value,0))

        #         if cycleTime < ELECTRODE_DUTYCYCLE * periodTime:
        #             self.dac.normalized_value = self.intensity
        #         else:
        #             self.dac.normalized_value = 0

        #         # Sleep for 1x10^-4 seconds
        #         time.sleep(1/10000)

    # Deactivate electrodes
    def deactivateElectrodes(self):
        print('ELECTRODES OFF')
        self.dac.normalized_value = 0

    # Gets the voltage from an analog input pin
    def get_voltage(pin):
        return (pin.value*3.3)/65536

    # Set electrode Intensity based on potentiometer position
    def setIntensity(self):
        self.intensity = self.pot.value/65536

    # Print all Inputs
    def printInputs(self):
        inputValues= [
            ['btnMode', self.btnMode.value],
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
            ['intensity', self.intensity],
            ['lowBattery', self.lowBattery],
        ]

        print('-'*24)
        print('STATES')
        self.printTable(stateValues)

    # Format output in a table
    def printTable(self, table):
        for row in table:
            print("{:<16} {:<16}".format(row[0], str(row[1])))

    # Handles button click to switch modes
    def switchMode(self):
        self.ledBlue.value = False
        self.ledGreen.value = False
        self.ledYellow.value = False

        self.deviceState = (self.deviceState + 1) % 4
        
        if self.deviceState == State.CALIBRATE:
            print('CALIBRATE MODE ' + '-'*12)
            self.ledBlue.value = True
        elif self.deviceState == State.WALK:
            print('WALK MODE ' + '-' * 12)
            self.ledGreen.value = True
        elif self.deviceState == State.REHAB:
            print('REHAB MODE ' + '-'*12)
            self.ledYellow.value = True
        else:
            print('STANDY MODE ' + '-' * 12)
