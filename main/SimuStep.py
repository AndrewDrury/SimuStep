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

from CONSTANTS import ELECTRODE_FREQ, ELECTRODE_PW, ELECTRODE_DUTYCYCLE, ELECTRODE_PERIOD, ELECTRODE_OFFSET

# Define enum for device states
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
        # self.electrodeSignal3.value = True
        # self.electrodeSignal3.duty_cycle= 65535 // 2

        # FIRST PULSE
        self.dac.raw_value = self.intensity
        # self.dac.raw_value = 4095
        self.electrodeSignal1.value = True
        # self.electrodeSignal3.value = True
        time.sleep(ELECTRODE_PW)

        # self.dac.raw_value = 0
        self.electrodeSignal1.value = False
        # self.electrodeSignal3.value = False
        time.sleep(ELECTRODE_OFFSET)

         # SECOND PULSE
        # self.dac.raw_value = self.intensity
        self.electrodeSignal2.value = True
        time.sleep(ELECTRODE_PW)
        # self.dac.raw_value = 0
        self.electrodeSignal2.value = False       
        time.sleep(ELECTRODE_OFFSET)

        # # SIMULTANEOUS PULSES
        # # FIRST PULSE
        # self.dac.raw_value = self.intensity
        # self.electrodeSignal1.value = True
        # self.electrodeSignal2.value = True
        # time.sleep(ELECTRODE_PW)

        # # SECOND PULSE
        # self.electrodeSignal1.value = False
        # self.electrodeSignal2.value = False 
        # time.sleep(ELECTRODE_OFFSET)

    def activateElectrodesRehab(self):
        activationTime = 1 # in seconds
        offTime = 3 # in seconds
        currentTime = 0

        self.dac.raw_value = self.intensity
        signal2Delay = ELECTRODE_PERIOD/2-ELECTRODE_PW

        while currentTime < activationTime and not self.btnMode.value:
            self.electrodeSignal1.value = True
            self.electrodeSignal2.value = False
            print(self.electrodeSignal1.value)
            time.sleep(ELECTRODE_PW)
            self.electrodeSignal1.value = False
            time.sleep(ELECTRODE_OFFSET)
            self.electrodeSignal2.value = True
            time.sleep(ELECTRODE_PW)
            self.electrodeSignal2.value = False
            print(self.electrodeSignal1.value)        
            time.sleep(ELECTRODE_OFFSET)
            currentTime += ELECTRODE_PERIOD
        time.sleep(offTime)

    # Deactivate electrodes
    def deactivateElectrodes(self):
        print('ELECTRODES OFF')
        self.dac.normalized_value = 0

    # Gets the voltage from an analog input pin
    def get_voltage(pin):
        return (pin.value*3.3)/65536

    # Set electrode Intensity based on potentiometer position
    def setIntensity(self, intensity=0):
        if intensity:
            self.intensity = int(4095 * intensity / 3.3)
        else:
            self.intensity = int((self.pot.value/65536) * 4095)
        print(3.3*self.intensity/4095)

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

        # self.deviceState = (self.deviceState + 1) % 4
        self.deviceState = (self.deviceState + 1) % 2
        
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
