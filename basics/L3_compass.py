import time
import L2_compass_heading
import L1_log


# Get compass heading
def getCompassHeading():
    heading = L2_compass_heading.get_heading()
    return heading


# Convert heading into cardinal direction
def getCardinalDirection(heading):

    if -22.5 <= heading < 22.5:
        return "North"

    elif 22.5 <= heading < 67.5:
        return "NorthWest"

    elif 67.5 <= heading < 112.5:
        return "West"

    elif 112.5 <= heading < 157.5:
        return "SouthWest"

    elif heading >= 157.5 or heading < -157.5:
        return "South"

    elif -157.5 <= heading < -112.5:
        return "SouthEast"

    elif -112.5 <= heading < -67.5:
        return "East"

    elif -67.5 <= heading < -22.5:
        return "NorthEast"


while True:

    heading = getCompassHeading()
    direction = getCardinalDirection(heading)

    # Log numerical heading
    L1_log.tmpFile(heading, "heading.txt")

    # Log cardinal direction
    L1_log.stringTmpFile(direction, "direction.txt")

    print("Heading:", heading, "degrees")
    print("Direction:", direction)

    time.sleep(.5)