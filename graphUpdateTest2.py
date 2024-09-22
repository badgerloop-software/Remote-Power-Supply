import numpy as np
import time
import matplotlib.pyplot as plt

MAX_VOLTS = 30
MAX_AMPS = 3.5    # both should be adjustable!

def animate(x):
    def i(x):
        d = 3
        return (-10**-d)*np.exp(((np.log(MAX_AMPS*(10**d)+1))/MAX_VOLTS)*x)+MAX_AMPS+10**-d    
    
    def v(q):
        return MAX_VOLTS*q
    x1 = np.array([30, 30, 29.8, 29.6, 29.4, 29.2, 29, 28.8, 28.6, 28.4, 28.2, 28, 27.8, 27.6, 27.4, 27.2, 27, 26.7, 26.4, 26.1, 25.8, 25.5, 25.2, 24.9, 24.6, 24.3, 24, 23.5, 23, 22.5, 22, 21.5, 21, 20, 19, 18, 17, 16, 15, 14, 12, 9, 6, 3, 0]) #sets proportions for a different MAX_VOLTS.
    x = v(x1/30)                    #combines proportions from x array with whatever MAX_VOLTS is set to.
    z = i(x)                       #sets y component for the IV curve to be plotted.
    #y1 = np.array([0, i(29.9), i(29.7), i(29.5), i(29.3), i(29.1), i(28.9), i(28.7), i(28.5), i(28.3), i(28.1), i(27.9), i(27.7), i(27.5), i(27.3), i(27.1), i(26.85), i(26.55), i(26.25), i(25.95), i(25.65), i(25.35), i(25.05), i(24.75), i(24.45), i(24.15), i(23.75),i(23.25),i(22.75),i(22.25),i(21.75),i(21.25),i(20.5),i(19.5),i(18.5),i(17.5),i(16.5),i(15.5),i(14.5),i(13),i(10.5),i(7.5),i(4.5),i(1.5),3.5])
    y = i((x[1:]+x[:-1]) / 2)    #sets current limits between voltages.
    y = np.append(y, MAX_AMPS)    #adds final current limit at MAX_AMPS
    a=1
    fig = plt.figure(figsize=(14,5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    fig.show()
    fig.canvas.draw()
    # print(len(x1))
    # print(len(z))
    # print(len(y1))
    while True:
        current_input = input()
        if(current_input=="0"):     # first check if the current is at zero (and graph it)
            # IV Plot Update
            ax1.cla()
            ax1.plot(x, z)
            ax1.set(xlabel='voltage',ylabel='current')
            ax1.set_title('IV')
            ax1.hlines(y=y,xmin=0,xmax=MAX_VOLTS,linewidth=1,color='r',alpha=0.2 )
            ax1.scatter(MAX_VOLTS, 0, color="red")
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
            continue

        current_input = float(current_input)
        if(current_input>MAX_AMPS):
            print("Value exceeds Isc")
            break
        elif(current_input<0):
            print("Value cannot be negative")
            break

        elif(current_input>y[a]):
            for w in range(len(y)):
                a += 1
                # supply.setVoltage(x[a])
                # supply.setCurrent(y[a])
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(round(x[a],2),round(y[a],3))
                print(clarification)
                
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
                time.sleep(0.25)
                if a>= len(y):
                    a = len(y)
                if(current_input<=y[a]):
                    break

        elif(current_input<y[a-1]):
            for w in range(len(y)):
                a -= 1
                # supply.setVoltage(x[a])
                # supply.setCurrent(y[a])
                clarification = "\nvoltage: {} volts\ncurrent limit: {} amps".format(x[a],y[a])
                print(clarification)

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
                time.sleep(0.25)
                if a < 1:
                    a = 1
                if(current_input>=y[a-1]):
                        break

animate(1)

