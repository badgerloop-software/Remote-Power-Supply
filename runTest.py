import sys
import pyvisa
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import power

# Declaring Constants
READ_TERMINATION =  '\r'
WRITE_TERMINATION = '\r'
MAX_VOLTS = 30
MAX_AMPS = 3.5

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def runTest():
    try:
        supply = power.PowerSupply()
        supply.turnOn()
        
        def i(x):
            d = 3
            return (-10**-d)*np.exp(((np.log(MAX_AMPS*(10**d)+1))/MAX_VOLTS)*x)+MAX_AMPS+10**-d    
        x = np.array([30, 30, 29.5, 29, 28.5, 28, 27.5, 27, 26.5, 26, 25.5, 25, 24.5, 24, 23.5, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 12, 9, 6, 3, 0]) #voltage array
        y = np.array([0, i(29.75),i(29.25),i(28.75),i(28.25),i(27.75),i(27.25),i(26.75),i(26.25),i(25.75),i(25.25),i(24.75),i(24.25),i(23.75),i(23.25),i(22.5),i(21.5),i(20.5),i(19.5),i(18.5),i(17.5),i(16.5),i(15.5),i(14.5),i(13),i(10.5),i(7.5),i(4.5),i(1.5),3.5]) #current array
        z = np.array([0, 0, i(29.5), i(29), i(28.5), i(28), i(27.5), i(27), i(26.5), i(26), i(25.5), i(25), i(24.5), i(24), i(23.5), i(23), i(22), i(21), i(20), i(19), i(18), i(17), i(16), i(15), i(14), i(12), i(9), i(6), i(3), MAX_AMPS]) #plotting array
        a = 1
        supply.setVoltage(x[a])
        supply.setCurrent(y[a])
        fig = plt.figure(figsize=(14,5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        while True:
            if(supply.getCurrent()>y[a]):
                a += 1
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(x[a],y[a])
                print(clarification)
                supply.setVoltage(x[a])
                supply.setCurrent(y[a])
                if a >= len(y):
                    a = len(y)

            elif(supply.getCurrent()<y[a-1]):
                a -= 1
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(x[a],y[a])
                print(clarification)
                supply.setVoltage(x[a])
                supply.setCurrent(y[a])
                if a < 1:
                    a = 1
            
            # IV Plot Update
            ax1.cla()
            ax1.plot(x, z)
            ax1.set(xlabel='voltage',ylabel='current')
            ax1.set_title('IV')
            ax1.hlines(y=y,xmin=0,xmax=30,linewidth=1,color='r',alpha=0.2 )
            ax1.scatter(x[a], z[a], color="red")
            ivPoint = "{}V\n~{}I".format(x[a],round(z[a],2))
            ax1.annotate(ivPoint, (x[a],z[a]))

            # Power Plot Update
            ax2.cla()
            ax2.plot(x, x*z)
            ax2.set(xlabel='voltage',ylabel='power')
            ax2.set_title('Power')
            ax2.scatter(x[a], x[a]*z[a], color="red")
            powerPoint = "~{}W".format(round(x[a]*z[a],2))
            ax2.annotate(powerPoint, (x[a],x[a]*z[a]))
            plt.pause(0.01)
            fig.canvas.draw()
            time.sleep(0.1)

    except KeyboardInterrupt:
        supply.turnOff()
    except Exception as e:
        print(e)
        supply.turnOff()


if __name__ == "__main__":
    runTest()