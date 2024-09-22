#!/usr/bin/python

import power
import time
import argparse
import numpy as np
import matplotlib.pyplot as plt

def create_iv_curve(voc, isc, d, voltage):
    x = np.linspace(0,voc)
    def ivcurve(x):
        return (-10**-d)*np.exp(((np.log(isc*(10**d)+1))/voc)*x)+isc+10**-d
    plt.plot(x,ivcurve(x))
    plt.scatter(voltage, np.interp(voltage, x, (-10**-d)*np.exp(((np.log(isc*(10**d)+1))/voc)*x)+isc+10**-d), color="red")
    print('voltage:',voltage,'volts', '    current:',np.interp(voltage, x, (-10**-d)*np.exp(((np.log(isc*(10**d)+1))/voc)*x)+isc+10**-d),"amps")
    plt.show()


    def powercurve(x):
        return (x * ivcurve(x))
    plt.plot(x,powercurve(x))
    plt.scatter(voltage, np.interp(voltage, x, x * ivcurve(x)), color="red")
    print("power:",np.interp(voltage, x, x * ivcurve(x)),"amps")
    plt.show()
    return


def main():
    #Add arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('voc', type = float, help = 'The open circuit voltage of the solar string @25C')
    parser.add_argument('isc', type = float,  help = 'The short circuit current of the solar string @25C')
    parser.add_argument('d', type = float,  help = 'd!')
    parser.add_argument('voltage', type = float,  help = 'The voltage being read')
    
    args = parser.parse_args()
    voc = args.voc
    isc = args.isc
    d = args.d
    voltage = args.voltage

    if(voc > 60):
        print("Max voltage is 60V")
        quit()


    if(isc > 10):
        print("Short circuit current must be less than 10A")
        quit()

    iv_curve_points = create_iv_curve(voc, isc, d, voltage)

    #Create power supply object
    # z60 = power.PowerSupply()

#Main body of code
if __name__ == "__main__":
    main()
