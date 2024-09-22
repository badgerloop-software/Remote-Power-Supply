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
    supply = power.PowerSupply()
    # Startup
    #print("Finding Resources")
    #rm = pyvisa.ResourceManager()
    # print(rm.list_resources())
    # rs = rm.list_resources()
    # z60 = rm.open_resource(rs[0])
    # z60.read_termination = READ_TERMINATION
    # z60.write_termination = WRITE_TERMINATION
    # # Setting Address
    # print("Sending Inilization Commands")
    # z60.write("INST:NSEL 4")
    # print(z60.query("INST:NSEL?"))
    # z60.write("SYST:REM REM")
    # print("Resources found")
    
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
    # fig.show()
    # fig.canvas.draw()

    while True:
        current_input = input()
        current_input = float(current_input)
        if(current_input>y[a]):
            for w in range(len(y)):
                a += 1
                supply.setVoltage(x[a])
                supply.setCurrent(y[a])
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(x[a],y[a])
                print(clarification)
                
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
                time.sleep(1)

                if(current_input<=y[a]):
                    break

        elif(current_input<y[a-1]):
            for w in range(len(y)):
                a -= 1
                supply.setVoltage(x[a])
                supply.setCurrent(y[a])
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(x[a],y[a])
                print(clarification)

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
                time.sleep(1)

                if(current_input>=y[a-1]):
                        break


    supply.turnOn()



if __name__ == "__main__":
    try:
        runTest()
    except KeyboardInterrupt:
        power.PowerSupply.turnOff()


# Functions
    # def setVolts(voltage):
    #     if (int(voltage) > MAX_VOLTS): voltage = MAX_VOLTS
    #     z60.write("VOLT " + voltage)

    # def setOutput(state):
    #     if (state): state = 1
    #     if (not state): state = 0
    #     z60.write("OUTP:STAT " + str(state))
            
    # cmdVolts = 24
    # if (sys.argv[1]): cmdVolts = sys.argv[1]
    # print("Setting Voltage to " + cmdVolts)
    # setVolts(cmdVolts)
    # print("Turning on Power Supply")
    # setOutput(1)

# timeout = 5 # Sleep for 5 seconds
# if (sys.argv[2]): timeout = sys.argv[2]:
#     print("Waiting " + timeout + "seconds")
#     time.sleep(int(timeout))
#     print("Turning off Power Supply")
#     setOutput(0)
#     print("Done")

#[0, 33, 36, 39, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) #voltage array
#[7.0, 6.9, 6.84, 6.75, 6.61, 6.43, 6.29, 6.18, 6.05, 5.89, 5.71, 5.51, 5.27, 5.0, 4.68, 4.31, 3.88, 3.38, 2.82, 2.16, 1.37, 0.47, 0]) #current array

# x = np.array([60, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 42, 39, 36, 33, 0]) #voltage array
# y = np.array([0, 0, i(59.5), i(58.5), i(57.5), i(56.5), i(55.5), i(54.5), i(53.5), i(52.5), i(51.5), i(50.5), i(49.5), i(48.5), i(47.5), i(46.5), i(45.5), i(44.5), i(43), i(40.5), i(37.5), i(34.5), i(16.5), 7.0]) #current array
               #0, 0, 0.47A    1.37A    2.16A    2.82A    3.38A    3.88A    4.31A
# or maybe: voltages = np.arrange(0.5,60,1)  -->  [0.5, 1.5, 2.5...]