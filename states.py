# DEFINE ENUM FOR DEVICE STATES
class State:
    STANDBY = 0
    CALIBRATE = 1
    WALK = 2
    REHAB = 3

# DEFINE STATES
deviceState         # State of the device (standby | calibrate | walk | rehab)
elecFreqState       # Frequency of the electrodes
elecPulseWidthState # Pulse width of the electrodes
lowBattery          # Low battery state