"""MXET 300 Lab 6: log the nearest LIDAR obstacle for Node-RED.

Place this script in basics with L1_lidar.py, L2_vector.py, and L1_log.py.
Set SENSOR_IP in L1_lidar.py to the address on your LIDAR's sticker.
"""

import L1_log as log
import L1_lidar as lidar
import L2_vector as vec
from time import sleep


def main():
    sensor = lidar.Lidar()
    processor = None

    try:
        sensor.connect()
        processor = sensor.run()
        sleep(2)  # Allow the background thread to receive its first scan.

        while True:
            if not processor.is_alive():
                raise RuntimeError(
                    "LIDAR stopped. Check its connection and SENSOR_IP in L1_lidar.py."
                )

            scan = sensor.get()

            # Wait for data and skip scans with no valid distance readings.
            if scan is None:
                print("Waiting for LIDAR data...")
                sleep(0.5)
                continue

            if len(vec.getValid(scan)) == 0:
                print("No valid obstacle measurements.")
                sleep(0.5)
                continue

            distance, angle = vec.getNearest(scan)
            x, y = vec.polar2cart(distance, angle)

            # tmpFile writes one number to /tmp/ using the supplied filename.
            log.tmpFile(distance, "lidar_distance.txt")
            log.tmpFile(angle, "lidar_angle.txt")
            log.tmpFile(x, "lidar_x.txt")
            log.tmpFile(y, "lidar_y.txt")

            # x is positive forward; y is positive to the robot's left.
            print(
                f"Distance: {distance:.2f} m | Angle: {angle:.2f} deg | "
                f"x: {x:.2f} m | y: {y:.2f} m"
            )
            sleep(0.5)  # Give Node-RED time to read the files.

    except KeyboardInterrupt:
        print("\nStopping LIDAR...")

    finally:
        if processor is not None:
            sensor.kill(processor)


if __name__ == "__main__":
    main()