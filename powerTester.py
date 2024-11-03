import power
import time


z60 = power.PowerSupply()

z60.turnOn()

z60.setVoltage(3)
time.sleep(1)
print(f"voltage: {float(z60.getVoltage())}")
time.sleep(1)
print(f"current: {z60.getCurrent()}")
time.sleep(1)

z60.turnOff()