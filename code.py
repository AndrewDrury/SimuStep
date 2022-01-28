"""code.py is the first program run when the ItsyBitsy RP2040 is powered on"""
import time

import main.helper as helper
from main.init import initIO, initStates
from main.SimuStep import SimuStep

# Initialize simuStep object (using SimuStep class defined in SimuStepClass.py)
simuStep = SimuStep()

# Initialize Inputs, Outputs, and States
initIO(simuStep)
initStates(simuStep)

# Turn on Power Button light (indicating device on)
simuStep.ledPower.value = True
simuStep.ledBlue.value = True
simuStep.ledGreen.value = True
simuStep.ledYellow.value = True

btnModePushed = False

time.sleep(1)
simuStep.ledBlue.value = False
simuStep.ledGreen.value = False
simuStep.ledYellow.value = False

# Start main loop
while True:
    if simuStep.btnMode.value and btnModePushed == False:
        btnModePushed = True
        simuStep.switchMode()

        simuStep.printInputs()
        # simuStep.printOutputs()
        # simuStep.printStates()
    elif not simuStep.btnMode.value and btnModePushed == True:
        btnModePushed = False

    time.sleep(0.01)
