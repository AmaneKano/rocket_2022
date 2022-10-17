from rocketcea.cea_obj_w_units import CEA_Obj
import numpy as np
import matplotlib.pyplot as plt

ispObj = CEA_Obj( oxName='LOX', fuelName='CH3OH',pressure_units='MPa',isp_units='m/s',temperature_units='K')
opf = np.arange(0.1,2.5,0.1)
pcs = [1,3,5,10]

for pc in pcs:
    isp = np.array([ispObj.get_Isp(Pc=pc,MR=r) for r in opf])
    plt.plot(opf,isp,label=str(pc)+'[MPa]')
plt.legend()
plt.xlabel('O/F')
plt.ylabel('Isp[m/s]')
plt.show()
