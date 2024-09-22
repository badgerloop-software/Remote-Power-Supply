import numpy as np
import time
import matplotlib.pyplot as plt

MAX_VOLTS = 30
MAX_AMPS = 3.5

def animate(x):
    def i(x):
        d = 3
        return (-10**-d)*np.exp(((np.log(MAX_AMPS*(10**d)+1))/MAX_VOLTS)*x)+MAX_AMPS+10**-d    
    def v(q):
        return MAX_VOLTS*q
    # x = [30, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 12, 9, 6, 3, 0] #voltage array
    # y = [0, 0, i(29.5), i(28.5), i(27.5), i(26.5), i(25.5), i(24.5), i(23.5), i(22.5), i(21.5), i(20.5), i(19.5), i(18.5), i(17.5), i(16.5), i(15.5), i(14.5), i(13), i(10.5), i(7.5), i(4.5), i(1.5), 3.5] #current array
    # x = [0, 3, 6, 9, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, MAX_VOLTS] #voltage array
    # y = [MAX_AMPS, i(3), i(6), i(9), i(12), i(14), i(15), i(16), i(17), i(18), i(19), i(20), i(21), i(22), i(23), i(24), i(25), i(26), i(27), i(28), i(29), 0] #current array
    x1 = np.array([30, 30, 29.8, 29.6, 29.4, 29.2, 29, 28.8, 28.6, 28.4, 28.2, 28, 27.8, 27.6, 27.4, 27.2, 27, 26.7, 26.4, 26.1, 25.8, 25.5, 25.2, 24.9, 24.6, 24.3, 24, 23.5, 23, 22.5, 22, 21.5, 21, 20, 19, 18, 17, 16, 15, 14, 12, 9, 6, 3, 0]) #sets proportions for a different MAX_VOLTS.
    x = v(x1/30)                    #combines proportions from x1 array with whatever MAX_VOLTS is set to.
    z = i(x)                        #sets y component for the IV curve to be plotted.
    y = i((x[1:]+x[:-1]) / 2)       #sets current limits between voltages.
    y = np.append(y, MAX_AMPS)      #adds the final current limit of MAX_AMPS.
    a=1
    fig = plt.figure(figsize=(14,5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    fig.show()
    fig.canvas.draw()

    while True:
    # compute something
        ax1.cla()
        ax1.plot(x, z)
        ax1.set(xlabel='voltage',ylabel='current')
        ax1.set_title('IV')
        ax1.hlines(y=y,xmin=0,xmax=MAX_VOLTS,linewidth=1,color='r',alpha=0.2 )
        ax1.scatter(x[a], z[a], color="red")
        ivPoint = "{}V\n~{}I".format(round(x[a],2),round(z[a],2))
        ax1.annotate(ivPoint, (x[a],z[a]))
        ax2.cla()
        ax2.plot(x, x*z)
        ax2.set(xlabel='voltage',ylabel='power')
        ax2.set_title('Power')
        ax2.scatter(x[a], x[a]*z[a], color="red")
        powerPoint = "~{}W".format(round(x[a]*z[a],2))
        ax2.annotate(powerPoint, (x[a],x[a]*z[a]))
        a += 1
        if a > len(z)-1:
            a = 1

    # update canvas immediately
        plt.pause(0.01)
        fig.canvas.draw()
        time.sleep(0.5)

animate(1)

