# CONSTANTS

# ACTIVATION CONSTANTS
START_ACTIVATION_ANGLE = -10    # Leg angle from the vertical at which to START electrode activation
END_ACTIVATION_ANGLE = 35       # Leg angle from the vertical at which to END electrode activation
INTENSITY = 0                   # Intensity of elctrodes
ELECTRODE_FREQ = 40             # Electrode frequency (in  - 40Hz)
ELECTRODE_PW = 0.0001           # Electrode pulse width (measured in seconds - 150 microseconds)
ELECTRODE_DUTYCYCLE = ELECTRODE_PW * ELECTRODE_FREQ * 100
ELECTRODE_PERIOD = 1/ELECTRODE_FREQ
ELECTRODE_OFFCYCLE = ELECTRODE_PERIOD - ELECTRODE_PW
ELECTRODE_OFFSET = ELECTRODE_PERIOD/2-ELECTRODE_PW

GYRO_DEADZONE = 0.53            # TODO: NEEDS TO BE REFINED - the deadzone at which the leg is deemed stationary (no activation)

# OTHER CONSTANTS
AA = 0.97                       # IMU Filter constant to obtain angle
LOOP_PERIOD = 0.02              # 0.02 -> 20ms, how long between each loop
RAD_TO_DEG = 57.29578           # Unit conversion radians to degree

