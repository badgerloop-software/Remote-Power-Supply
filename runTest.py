import sys
import pyvisa
import time
# Declaring Constants
READ_TERMINATION =  '\r'
WRITE_TERMINATION = '\r'
MAX_VOLTS = 50

# Startup
print("Finding Resources")
rm = pyvisa.ResourceManager()
print("Resources Found: " + rm.list_resources())
rs = rm.list_resources()
z60 = rm.open_resource('rs[0]')
z60.read_termination = READ_TERMINATION
z60.write_termination = WRITE_TERMINATION
# Setting Address
print("Sending Inilization Commands")
z60.write("INST:NSEL 4")
print(z60.query("INST:NSEL?"))
inst.write("SYST:REM REM")
print("Resources found")

# Functions
def setVolts(voltage):
    if (voltage > MAX_VOLTS) voltage = MAX_VOLTS
    z60.write("SOUR:VOLT:LEV " + voltage)

def setOutput(state):
    if (state) state = 1
    if (not state) state = 0
    z60.write("SOUR:POW:STAT" + state)

cmdVolts = 24
if (sys.argv[1]) cmdVolts = sys.argv[1]
print("Setting Voltage to " + cmdVolts)
setVolts(cmdVolts)
print("Turning on Power Supply")
setOutput(1)
timeout = 5 # Sleep for 5 seconds
if (sys.argv[2]) timeout = sys.argv[2]
print("Waiting " + timeout + "seconds")
time.sleep(timeout)
print("Turning off Power Supply")
setOutput(0)
print("Done")
