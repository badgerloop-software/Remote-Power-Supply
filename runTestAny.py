import time
import numpy as np
import matplotlib.pyplot as plt
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
        def v(q):
            return MAX_VOLTS*q
        x1 = np.array([30, 30, 29.8, 29.6, 29.4, 29.2, 29, 28.8, 28.6, 28.4, 28.2, 28, 27.8, 27.6, 27.4, 27.2, 27, 26.7, 26.4, 26.1, 25.8, 25.5, 25.2, 24.9, 24.6, 24.3, 24, 23.5, 23, 22.5, 22, 21.5, 21, 20, 19, 18, 17, 16, 15, 14, 12, 9, 6, 3, 0]) #sets proportions for a different MAX_VOLTS.
        x = v(x1/30)                    #combines proportions from x1 array with whatever MAX_VOLTS is set to.
        z = i(x)                        #sets y component for the IV curve to be plotted.
        y = i((x[1:]+x[:-1]) / 2)       #sets current limits between voltages.
        y = np.append(y, MAX_AMPS)      #adds the final current limit of MAX_AMPS.
        a = len(y)-1                    #starts at the last current limit
        supply.setVoltage(x[a])         # initializes voltage (to max voltage)
        supply.setCurrent(y[a])         # initializes current limit (to first current limit)
        fig = plt.figure(figsize=(14,5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)

        print(y)

        while True:
            if(supply.getCurrent()>y[a]):   # if current is higher than first limit
                a += 1                      # raise the limit by one step
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(x[a],y[a])
                print(clarification)
                supply.setVoltage(x[a])
                supply.setCurrent(y[a])
                if a >= len(y):
                    a = len(y)

            elif(supply.getCurrent()<y[a-1]):   # if current is lower than the previous limit
                a -= 1                          # lower the limit by one step
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
            ax1.hlines(y=y,xmin=0,xmax=MAX_VOLTS,linewidth=1,color='r',alpha=0.2 )
            ax1.scatter(x[a], z[a], color="red")
            ivPoint = "{}V\n~{}I".format(round(x[a],2),round(z[a],2))
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
            time.sleep(0.25)    # adjust frequency of update
    
    except KeyboardInterrupt:
        supply.turnOff()
    except Exception as e:
        print(e)
        supply.turnOff()



if __name__ == "__main__":
    runTest()
