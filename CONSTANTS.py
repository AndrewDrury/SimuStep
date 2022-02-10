# CONSTANTS

# ACTIVATION CONSTANTS
START_ACTIVATION_ANGLE = -10    # Leg angle from the vertical at which to START electrode activation
END_ACTIVATION_ANGLE = 35       # Leg angle from the vertical at which to END electrode activation
INTENSITY = 0                   # Intensity of elctrodes
ELECTRODE_FREQ = 50             # Electrode frequency (in Hz)
ELECTRODE_PW = 100              # Electrode pulse width (measured in seconds)
ELECTRODE_DUTYCYCLE = ELECTRODE_PW/1000000 * ELECTRODE_FREQ * 100

GYRO_DEADZONE = 0.5             # TODO: NEEDS TO BE REFINED - the deadzone at which the leg is deemed stationary (no activation)

# OTHER CONSTANTS
AA = 0.97                       # IMU Filter constant to obtain angle
LOOP_PERIOD = 0.02              # 0.02 -> 20ms, how long between each loop
RAD_TO_DEG = 57.29578           # Unit conversion radians to degree

