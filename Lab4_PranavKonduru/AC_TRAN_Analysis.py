import ahkab
from ahkab import circuit, printing, time_functions
import matplotlib.pyplot as plt
import numpy as np

mycircuit = circuit.Circuit(title="RLC three loopcircuit")


gnd = mycircuit.get_ground_node()


mycircuit.add_inductor("L2", n1="n1", n2="n2", value=100e-3)
mycircuit.add_resistor("R1", n1="n2", n2="n3", value=7.19e3)
mycircuit.add_capacitor("C1", n1="n3", n2=gnd, value=2e-9)
mycircuit.add_resistor("R2", n1="n3", n2="n4", value=14e3)
mycircuit.add_capacitor("C2", n1="n4", n2=gnd, value=2e-9)
mycircuit.add_resistor("R3", n1="n4", n2="n5", value=35e3)
mycircuit.add_capacitor("C3", n1="n4", n2=gnd, value=2e-9)
mycircuit.add_resistor("R4", n1="n5", n2=gnd, value=80e3)





voltage_step = time_functions.pulse(v1=0, v2=1, td=500e-9, tr=1e-12, pw=1, tf=1e-12, per=2)

mycircuit.add_vsource("V1", n1="n1", n2=gnd, dc_value=5, ac_value=1, function=voltage_step)


print (mycircuit)




op_analysis = ahkab.new_op()
ac_analysis = ahkab.new_ac(start=1e3, stop=1e5, points=100)
tran_analysis = ahkab.new_tran(tstart=0, tstop=1.2e-3, tstep=1e-6, x0=None)





r = ahkab.run(mycircuit, an_list=[op_analysis, ac_analysis, tran_analysis])





r['op'].results




r['op'].keys()





r['op']['VN4']





"The DC output voltage is %s %s" % (r['op']['VN4'] , r['op'].units['VN4'])





print(r['ac'])





r['ac'].keys()






fig = plt.figure()
plt.title(mycircuit.title + " - TRAN Simulation")
plt.plot(r['tran']['T'], r['tran']['VN1'], label="Input voltage")
#plt.hold(True)
plt.plot(r['tran']['T'], r['tran']['VN4'], label="output voltage")
plt.legend()
#plt.hold(False)
plt.grid(True)
plt.ylim([0,1.2])
plt.ylabel('Step response')
plt.xlabel('Time [s]')
fig.savefig('tran_plot.png')

fig = plt.figure()
plt.subplot(211)
plt.semilogx(r['ac']['f'], np.abs(r['ac']['Vn4']), 'o-')
plt.ylabel('abs(V(n4)) [V]')
plt.title(mycircuit.title + " - AC Simulation")
plt.subplot(212)
plt.grid(True)
plt.semilogx(r['ac']['f'], np.angle(r['ac']['Vn4']), 'o-')
plt.xlabel('frequency')
plt.ylabel('arg(V(n4)) [rad]')
fig.savefig('ac_plot.png')
plt.show()





r['ac']['f']








