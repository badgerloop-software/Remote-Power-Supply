#!/usr/bin/python

import sys
import pyvisa
import time

class PowerSupply:
    _TERM = '\r'
    
    def __init__(self):
        resMan = pyvisa.ResourceManager()
        resList = resMan.list_resources()
        self._z60 = resMan.open_resource(resList[0])
        self._z60.read_termination = self._TERM
        self._z60.write_termination = self._TERM
        self._z60.write("INST:NSEL 4")
        self._z60.write("SYST:REM REM")

    def turnOn(self):
        self._z60.write("OUTP ON")

    def turnOff(self):
        self._z60.write("OUTP OFF")

    def setVoltage(self, voltage):
        if (voltage <= 24):
            self._z60.write("VOLT " + str(voltage))
        
    def getVoltage(self):
        return self._z60.query("MEAS:VOLT:DC?")

    def getCurrent(self):
        return self._z60.query("MEAS:CURR:DC?")
    
