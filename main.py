import easy_scpi as scpi
import sys
import numpy as np
PORT = "COM4"

z60 = scpi.Instrument(PORT)

#Within main.py
def getVoltage():
  return z60.meas.volt.dc()
def setVoltage(volts):
  z60.source.voltage(volts)

#Not sure if these commands work
def getCurrent():
  return z60.meas.curr.dc
def setCurrent(amps):
  z60.source.current(amps)

def connect():
  z60.connect()

## Commands Go Here
print("Sendinging Address Commands")
z60.write("INST:NSEL 4\r")
print("Sent Address Command... Quereying")
z60.query("INST:NSEL?\r")
print("Starting Command Shell... Connecting to Power Supply")
z60.connect()
if (z60.is_connected):
  print("Power Supply Connected Running Command Shell")
else:
  print("Power Supply Can not Connect... Ending")
  sys.exit()
while(1):
  text = input("Enter a command: ")
  if (text == "connect"):
    connect()
    if (z60.is_connected):
      print("Z60 is Connected!")
    else:
        print("Z60 failed to connect")
  
  if (text == "getVolts"):
    print(getVoltage())
  
  #Within main.py
  if (text[:10] == "setVoltage"):
    z60.init()
    setVoltage(int(text[11:], base=10))
    x = np.array([0, 33, 36, 39, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) #voltage array
    y = np.array([7.0, 6.9, 6.84, 6.75, 6.61, 6.43, 6.29, 6.18, 6.05, 5.89, 5.71, 5.51, 5.27, 5.0, 4.68, 4.31, 3.88, 3.38, 2.82, 2.16, 1.37, 0.47, 0]) #current array
    #if current reads 7.0+ amps, set voltage to 0 volts
    if(getCurrent()>=y[0]): setVoltage(x[0])
    
    #else, if current reads between 6.9 and 7 amps, set voltage to 33 volts
    elif(getCurrent()>=y[1]): setVoltage(x[1])

  
  if (text == "on"):
    if(not z60.is_connected):
      print("You must connect to the supply first!")
    else:
      z60.output.state('on')
  
  if (text == "off"):
    z60.output.state ('off')
  
