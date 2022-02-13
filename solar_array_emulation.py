#!/usr/bin/python

import power
import argparse
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def create_iv_curve(voc, isc, vmpp, impp, temp):
    x = np.array([0.0,vmpp,voc])
    y = np.array([isc,impp,0.0])

    print(voc)

    #x = np.array([ 1.92, 30, 34.21])
    #y = np.array([8.30, 5, 0.06])
   
    def fun(x, a, b, c):
        return a*np.exp(b*x)
        #return a * np.cosh(b * x) + c

    coef,_ = curve_fit(fun, x, y)

    plt.plot(x,y, label = "IV Curve")

    plt.plot(np.linspace(x[0],x[-1]), fun(np.linspace(x[0],x[-1]), *coef), label=f'Model: %5.3f cosh(%4.2f x) + %4.2f' % tuple(coef) )

    plt.legend()
    plt.show()

    return

def main():
    #Add arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('voc', type = float, help = 'The open circuit voltage of the solar string @25C')
    parser.add_argument('isc', type = float,  help = 'The short circuit current of the solar string @25C')
    parser.add_argument('vmpp', type = float,  help = 'The maximum power point voltage of the solar string @25C')
    parser.add_argument('impp', type = float, help = 'The maximum power point current of the solar string @25C')
    parser.add_argument('temp', type = float, help = 'The temperature (C) of the solar array')
    
    args = parser.parse_args()
    voc = args.voc
    isc = args.isc
    vmpp = args.vmpp
    impp = args.impp
    temp = args.temp

    if(voc < vmpp):
        print("Voc must be greater than vmpp")
        quit()
    if(voc > 60):
        print("Max voltage is 60V)")
        quit()
    if(impp > isc):
        print("Isc must be greater than Impp")

    if(isc > 10):
        print("Short circuit current must be less than 10A")
        quit()

    iv_curve_points = create_iv_curve(voc, isc, vmpp, impp, temp)

    #Create power supply object
    z60 = power.PowerSupply()

#Main body of code
if __name__ == "__main__":
    main()
