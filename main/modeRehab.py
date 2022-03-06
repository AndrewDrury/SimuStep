# REHAB MODE
import math, time
from CONSTANTS import AA, LOOP_PERIOD, RAD_TO_DEG

def rehab(SimuStep):
    SimuStep.setIntensity(0.01)
    while not SimuStep.btnMode.value:
        SimuStep.activateElectrodesRehab()
    SimuStep.dac.raw_value = 0
