# CALIBRATE MODE
import math
from CONSTANTS import AA, LOOP_PERIOD, RAD_TO_DEG, ELECTRODE_FREQ, ELECTRODE_PW, INTENSITY

def calibrate(SimuStep):
        SimuStep.setIntensity()
        SimuStep.activateElectrodes()
