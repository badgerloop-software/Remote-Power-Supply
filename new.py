import pyvisa
rm = pyvisa.ResourceManager()
print(rm.list_resources())
rs = rm.list_resources()

z60 = rm.open_resource('rs[0]')
z60.read_termination = '\r'
z60.write_termination = '\r'
z60.write("INST:NSEL 4")
print(z60.query("INST:NSEL?"))
inst.write("SYST:REM REM")
