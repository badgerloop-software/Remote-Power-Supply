# Main
*Author:* Eric Udlis, Ryan Van Ells, Bowen Quan

The code for remotely controlling the Z60+ power supply.

## Instructions
### Requirements
Install `Python` and `pyvisa-py`. 

Check if you can connect to the power supply by connecting to the power supply via USB and running this code:
``` python
import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
```
If the print statement returns a `()`, you will have to download this [NI-VISA package manager](https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html?srsltid=AfmBOoqHK-onY60csoHtmGnAY_DCnk2QLjKrN-ulTwau5L5eJyFRlXp3#548367) and install its NI-VISA USB driver.

[Z60+ user manual](https://www.emea.lambda.tdk.com/fr/KB/Zplus-User-Manual-low-voltage-models-10V-to-100V.pdf). See page 99 of the PDF for how to manipulate the REM, VOLTAGE, and CURRENT knobs to configure the interface, baud, address settings of the Z60+ power supply. In the very least, it's useful for checking that the configuration has been properly set. 

### Tests
`python simple.py [voltage] [timeout]` Turns on the power supply for `timeout` seconds and sets the voltage to `voltage`. This is a good test to see if you can connect to the power supply and control it. 

### Other Files
`power.py` provides a class to control the power supply. 

### Running (Power Supply)
`python runTest.py`
This code will emulate the solar array with Voc of 30V and Isc of 3.5A

`python runTestAny.py`
This code will emulate the solar array with any Voc and Isc

`python runTestUserInput.py`
This code will emulate the solar array with Voc of 30V and Isc of 3.5A. Takes an input value as power supply current reading.

`python runTestUserInputAny.py`
This code will emulate the solar array with any Voc and Isc. Takes an input value as power supply current reading. 
### Running (Testing/No Power Supply)
`graphUpdateTest.py`
This code cycles through every point that the power supply could output, using very similar code as the power supply tests.

`graphUpdateTest2.py`
This code takes a user input as power supply current reading, and graphs what the power supply would output.
