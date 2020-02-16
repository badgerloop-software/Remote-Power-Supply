#!/usr/bin/python

import power
import argparse
import sys

VALID_VOLTAGES = [0, 24]    ## Add if we need a different voltage
HELP_MSG = "Customizable power supply control for automated testing, run with no args to turn off"

def main(onoff, voltage, info):
    
    z60 = power.PowerSupply()
    if z60.initFail():
        return

    if onoff == 'on':
        pass
        z60.setVoltage(voltage)
        z60.turnOn()
    elif onoff == 'off':
        pass
        z60.turnOff()

    if info:
        v = z60.getVoltage()
        c = z60.getCurrent()
        print("CURRENT: " + c)
        print("VOLTAGE: " + v)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=HELP_MSG)
    parser.add_argument('-v', '--volt', nargs=1, default=0, type=int, choices=VALID_VOLTAGES)
    parser.add_argument('-p', '--power', nargs=1, default='off', choices=['off', 'on'])
    parser.add_argument('-i', '--info', help='Reads the voltage and current from the supply', 
        action='store_true')
    args = parser.parse_args()
    main(args.power, args.volt, args.info)

