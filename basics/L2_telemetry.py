import time as time
import L1_ina as ina
import L1_log as log

while True:
    Voltage = ina.readVolts()
    log.tmpFile(Voltage, "Volts.txt")
    time.sleep(.5)

