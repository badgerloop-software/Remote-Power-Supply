# Main
*Author:* Eric Udlis, Ryan Van Ells

The code for remotely controlling the Z60+ power supply.

## Instructions
### Requirements
Install `Python` and `pyvisa-py`

### Running (Power Supply)
`python runTest.py`
This code will emulate the solar array with Voc of 30V and Isc of 3.5A

`python runTestAny.py`
This code will emulate the solar array with any Voc and Isc

`python runtTestUserInput.py`
This code will emulate the solar array with Voc of 30V and Isc of 3.5A. Takes an input value as power supply current reading.

`python runTestUserInputAny.py`
This code will emulate the solar array with any Voc and Isc. Takes an input value as power supply current reading. 
### Running (Testing/No Power Supply)
`graphUpdateTest.py`
This code cycles through every point that the power supply could output, using very similar code as the power supply tests.

`graphUpdateTest2.py`
This code takes a user input as power supply current reading, and graphs what the power supply would output.
