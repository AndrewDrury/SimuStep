import io
import states
from states import State

# Format output in a table
def printTable(table):
    colWidth = [max(len(x) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, colWidth[i]) for i, x in enumerate(line)) + " |")

# Print all Inputs
def printInputs():
    inputValues= [
        ['btnMode', io.btnMode.value],
        ['emg', io.emg.value],
        ['imu acceleration (m/s^2)', io.imu.acceleration],
        ['imu gyro (deg/s)', io.imu.gyro],
        ['pot', io.pot.value],
    ]

    print('----------------------')
    print('INPUTS')
    printTable(inputValues)
    print('----------------------')

# Print all Outputs
def printOutputs():
    outputValues= [
        ['electrodes', io.electrodes.value],
        ['ledBlue', io.ledBlue.value],
        ['ledGreen', io.ledGreen.acceleration],
        ['ledYellow', io.ledYellow.gyro],
        ['ledPower', io.ledPower.value],
    ]

    print('----------------------')
    print('OUTPUTS')
    printTable(outputValues)
    print('----------------------')

# Print all States
def printStates():
    stateValues= [
        ['deviceState', states.deviceState],
        ['elecFreqState', states.elecFreqState],
        ['elecPulseWidthState', states.elecPulseWidthState],
        ['lowBattery', states.lowBattery],
    ]

    print('----------------------')
    print('STATES')
    printTable(stateValues)
    print('----------------------')