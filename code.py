"""code.py is the first program run when the ItsyBitsy RP2040 is powered on"""
import time

from CONSTANTS import LOOP_PERIOD
from main.init import initIO, initStates
from main.modeCalibrate import calibrate
from main.modeRehab import rehab
from main.modeWalk import walk
from main.SimuStep import SimuStep, State

# Initialize simuStep object (using SimuStep class defined in SimuStepClass.py)
simuStep = SimuStep()

# Initialize Inputs, Outputs, and States
initIO(simuStep)
initStates(simuStep)

# Turn on LED lights at startup (indicating device on), delays are just for **AESTHETICS**
simuStep.ledPower.value = True
time.sleep(0.5)
simuStep.ledBlue.value = True
time.sleep(0.1)
simuStep.ledGreen.value = True
time.sleep(0.1)
simuStep.ledYellow.value = True

btnModePushed = False

time.sleep(2)
simuStep.ledBlue.value = False
simuStep.ledGreen.value = False
simuStep.ledYellow.value = False

# Start main loop
while True:
    # CHANGE MODE BUTTON CLICKED
    if simuStep.btnMode.value and btnModePushed == False:
        btnModePushed = True
        simuStep.switchMode()
    elif not simuStep.btnMode.value and btnModePushed == True:
        btnModePushed = False

    # ENTER CHOSEN MODE
    if simuStep.deviceState == State.CALIBRATE:
        calibrate(simuStep)
    elif simuStep.deviceState == State.WALK:
        walk(simuStep)
    elif simuStep.deviceState == State.REHAB:
        rehab(simuStep)

    # UNCOMMENT TO PRINT INPUTS, OUTPUTS, AND DEVICE STATES - FOR DEBUGGING
        # simuStep.printInputs()
        # simuStep.printOutputs()
        # simuStep.printStates()

    time.sleep(LOOP_PERIOD)
