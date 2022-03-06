# CALIBRATE MODE
import time
def calibrate(SimuStep):
    while not SimuStep.btnMode.value:
        SimuStep.setIntensity()
        SimuStep.activateElectrodes()

        # SimuStep.electrodeSignal1.value = True
        # SimuStep.electrodeSignal2.value = True
        # time.sleep(0.5)
    # SimuStep.electrodeSignal3.duty_cycle= 0
    SimuStep.electrodeSignal1.value = False
    SimuStep.electrodeSignal2.value = False
    SimuStep.electrodeSignal3.value = False
    SimuStep.dac.raw_value = 0
