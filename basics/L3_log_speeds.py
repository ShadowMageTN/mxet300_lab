import time
import L1_log as log
import L2_kinematics as kin

while True:

    # Get wheel speeds [PDL, PDR]
    wheelSpeeds = kin.getPdCurrent()

    # Get chassis speeds [xdot, thetadot]
    chassisSpeeds = kin.getMotion()

    # Print values to terminal
    print("Wheel Speeds [PDL, PDR]:", wheelSpeeds)
    print("Chassis Speeds [xdot, thetadot]:", chassisSpeeds)

    # Log values for Node-RED
    log.tmpFile(wheelSpeeds[0], "PDL.txt")
    log.tmpFile(wheelSpeeds[1], "PDR.txt")
    log.tmpFile(chassisSpeeds[0], "xdot.txt")
    log.tmpFile(chassisSpeeds[1], "thetadot.txt")

    # Short delay for Node-RED and Ctrl+C
    time.sleep(0.5)