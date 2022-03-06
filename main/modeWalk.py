# WALK MODE
import math
from CONSTANTS import AA, LOOP_PERIOD, RAD_TO_DEG, START_ACTIVATION_ANGLE, END_ACTIVATION_ANGLE, GYRO_DEADZONE

def walk(SimuStep):
    # IMU code to obtain slope and tilt from x, y, z acceleration (m/s^2) and gyro x, y, z, angular velocity (deg/s)
    # print('imu acc (m/s^2)', SimuStep.imu.acceleration)
    # print('imu gyro (deg/s)', SimuStep.imu.gyro)

    # Convert gyro angular velocity (deg/s) -> angle (deg)
    # by multiplying by the loop period
    gyroDegX = SimuStep.imu.gyro[0] * LOOP_PERIOD
    gyroDegY = SimuStep.imu.gyro[1] * LOOP_PERIOD
    gyroDegZ = SimuStep.imu.gyro[2] * LOOP_PERIOD

    accDegX = (math.atan2(SimuStep.imu.acceleration[1], SimuStep.imu.acceleration[2]) + math.pi) * RAD_TO_DEG
    accDegY = - (math.atan2(SimuStep.imu.acceleration[2], SimuStep.imu.acceleration[0]) + math.pi) * RAD_TO_DEG
    accDegZ = (math.atan2(SimuStep.imu.acceleration[0], SimuStep.imu.acceleration[1]) + math.pi) * RAD_TO_DEG

    ## THE FOLLOWING CODE IS AN ATTEMPT AT COMBINING GYRO AND ACC IMU VALUES FOR MORE ACCURATE ANGLE (currently not more accurate so not used)
    # Combine gyro and acceleration data using a filter to obtain an angle
    # angleDegX = AA * (gyroDegX) + (1 - AA) * accDegX
    # angleDegY = AA * (gyroDegY) + (1 - AA) * accDegY
    # angleDegZ = AA * (gyroDegZ) + (1 - AA) * accDegZ
    # print('gyro', gyroDegX, gyroDegY, gyroDegZ)
    # print('acc', accDegX, accDegY, accDegZ)
    # print('angle', angleDegX, angleDegY, angleDegZ)
    # print(gyroDegY, accDegY, angleDegY)

    if accDegY < -180:
        accDegY = accDegY + 360

    # Acceleration and Gyro direction
    accDir = [1, 1, 1]
    gyrDir = [1, 1, 1]

    for direction in range(0,3):
        if SimuStep.imu.acceleration[direction] < 0:
            accDir[direction] = -1
        if SimuStep.imu.gyro[direction] < 0:
            gyrDir[direction] = -1

    # Activate electrodes when moving in forward direction and in between START and END activation angle (defined in constants)
    if accDegY > START_ACTIVATION_ANGLE and accDegY < END_ACTIVATION_ANGLE and accDir[2] > 0 and gyrDir[1] < 0 and abs(SimuStep.imu.gyro[1]) > GYRO_DEADZONE:
       # TURN ON LEDS AS PROOF OF CONCEPT - represents activated electrodes
        SimuStep.ledYellow.value = True
        SimuStep.ledBlue.value = True

        SimuStep.activateElectrodes()

    else:
        SimuStep.ledYellow.value = False
        SimuStep.ledBlue.value = False
