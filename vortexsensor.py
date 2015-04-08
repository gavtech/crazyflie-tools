#!/usr/bin/env python2

import u3
import lcm
from crazyflie_t import vortex_sensor_t

if __name__=="__main__":
    d = u3.U3()
    lc = lcm.LCM()

    try:

        while True:
            ain0bits, = d.getFeedback(u3.AIN(0)) # Read from raw bits from AIN0
            ainValue = d.binaryToCalibratedAnalogVoltage(ain0bits, isLowVoltage=False, channelNumber=0)
            msg = vortex_sensor_t()
            msg.sensor1 = ainValue
            lc.publish('vortex_sensor',msg.encode())

    except KeyboardInterrupt:
        exit(0)