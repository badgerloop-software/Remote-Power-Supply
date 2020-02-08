import easy_scpi as scpi
import sys
PORT = "COM4"

z60 = scpi.Instrument(PORT)

def getVoltage():
  return z60.meas.volt.dc()

def setVoltage(volts):
  z60.source.voltage(volts)

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
  
  if (text[:10] == "setVoltage"):
    z60.init()
    setVoltage(int(text[11:], base=10))
  
  if (text == "on"):
    if(not z60.is_connected):
      print("You must connect to the supply first!")
    else:
      z60.output.state('on')
  
  if (text == "off"):
    z60.output.state ('off')
  
