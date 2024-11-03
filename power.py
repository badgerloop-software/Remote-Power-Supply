#!/usr/bin/python
import pyvisa

class PowerSupply:
    _TERM = '\r'
    _err  = False
    _z60 = 0
    def __init__(self):
        resMan = pyvisa.ResourceManager()
        resList = resMan.list_resources()
        try:
            self._z60 = resMan.open_resource(resList[0])
        except IndexError:
            print("Unable to find a power supply, shutting down")
            self._err = True
            return

        self._z60.read_termination = self._TERM
        self._z60.write_termination = self._TERM
        self._z60.write("INST:NSEL 4")
        self._z60.write("SYST:REM REM")

    def initFail(self):
        return self._err

    def turnOn(self):
        self._z60.write("OUTP ON")

    def turnOff(self):
        self._z60.write("OUTP OFF")

    def setVoltage(self, voltage):
        #if (voltage <= 24):
        self._z60.write("VOLT " + str(voltage))
 
    def setCurrent(self, current):
        self._z60.write("CURR:LEV " + str(current))
        
    def getVoltage(self):
        return self._z60.query("MEAS:VOLT:DC?")

    def getCurrent(self):
        q = self._z60.query("MEAS:CURR:DC?")

        try:
            return float(q)
        except ValueError:
            print("Value Error")
            self._err = True
            return


