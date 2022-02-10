# REHAB MODE
import math
from CONSTANTS import AA, LOOP_PERIOD, RAD_TO_DEG

def rehab(SimuStep):
        SimuStep.setIntensity()
        SimuStep.activateElectrodes()

        # TODO - COMPLETE ONCE CALIBRATE AND WALK ARE DONE (priority 3) 
