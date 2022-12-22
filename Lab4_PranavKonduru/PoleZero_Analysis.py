import ahkab
from ahkab import circuit
import numpy as np
from matplotlib.pyplot import *
import pylab as plt # required to see the plot
import sympy
from sympy.abc import w
from sympy import I

figsize = (15, 10)

print ("We're using ahkab %s" % ahkab.__version__)


bpf = ahkab.Circuit('RLC bandpass')
bpf.add_inductor('L1', 'in', 'n1', 2e-6)
bpf.add_capacitor('C1', 'n1', 'out', 3.2e-12)
bpf.add_resistor('R1', 'out', bpf.gnd, 25)
# we also give V1 an AC value since we wish to run an AC simulation
# in the following
bpf.add_vsource('V1', 'in', bpf.gnd, dc_value=1, ac_value=1)
print(bpf)

pza = ahkab.new_pz('V1', ('out', bpf.gnd), x0=None, shift=1e3)
r = ahkab.run(bpf, pza)['pz']

r.keys()

print('Singularities:')
for x, _ in r:
    print ("* %s = %+g %+gj Hz" % (x, np.real(r[x]), np.imag(r[x])))


figure(figsize=figsize)
# plot o's for zeros and x's for poles
for x, v in r:
    plot(np.real(v), np.imag(v), 'bo'*(x[0]=='z')+'rx'*(x[0]=='p'))
# set axis limits and print some thin axes
xm = 1e6
xlim(-xm*10., xm*10.)
plot(xlim(), [0,0], 'k', alpha=.5, lw=.5)
plot([0,0], ylim(), 'k', alpha=.5, lw=.5)
# plot the distance from the origin of p0 and p1
plot([np.real(r['p0']), 0], [np.imag(r['p0']), 0], 'k--', alpha=.5)
plot([np.real(r['p1']), 0], [np.imag(r['p1']), 0], 'k--', alpha=.5)
# print the distance between p0 and p1
plot([np.real(r['p1']), np.real(r['p0'])],
     [np.imag(r['p1']), np.imag(r['p0'])],
     'k-', alpha=.5, lw=.5)
# label the singularities
text(np.real(r['p1']), np.imag(r['p1'])*1.1, '$p_1$', ha='center',
     fontsize=20)
text(.4e6, .4e7, '$z_0$', ha='center', fontsize=20)
text(np.real(r['p0']), np.imag(r['p0'])*1.2, '$p_0$', ha='center',
     va='bottom', fontsize=20)
xlabel('Real [Hz]'); ylabel('Imag [Hz]'); title('Singularities');
plt.show() #plots the plot

#Resonance Frequency analytics calculations
C = 3.2e-12
L = 2e-6
f0 = 1./(2*np.pi*np.sqrt(L*C))
print('Resonance frequency from analytic calculations: %g Hz' %f0)

#pz analysis of resonance frequency
alpha = (-r['p0']-r['p1'])/2
a1 = np.real(abs(r['p0']-r['p1']))/2
f0 = np.sqrt(a1**2 - alpha**2)
f0 = np.real_if_close(f0)
print('Resonance frequency from PZ analysis: %g Hz' %f0)


#AC AnalysisAC and 
aca = ahkab.new_ac(start=1e8, stop=5e9, points=5e2, x0=None)
rac = ahkab.run(bpf, aca)['ac']
sympy.init_printing()
p0, p1, z0 = sympy.symbols('p0, p1, z0')
k = 25/2e-6 # constant term, can be calculated to be R/L
H = 25/2e-6*(I*w + z0*6.28)/(I*w +p0*6.28)/(I*w + p1*6.28)
Hl = sympy.lambdify(w, H.subs({p0:r['p0'], z0:abs(r['z0']), p1:r['p1']}))
def dB20(x):
    return 20*np.log10(x)
figure(figsize=figsize)
semilogx(rac.get_x()/2/np.pi, dB20(abs(rac['vout'])),
         label='TF from AC analysis')
semilogx(rac.get_x()/2/np.pi, dB20(abs(Hl(rac.get_x()))), 'o', ms=4,
         label='TF from PZ analysis')
legend(); xlabel('Frequency [Hz]'); ylabel('|H(w)| [dB]');
xlim(4e7, 3e8); ylim(-50, 1);

#Symbolic Analysis
symba = ahkab.new_symbolic(source='V1')
rs, tfs = ahkab.run(bpf, symba)['symbolic']
Hs = tfs['VOUT/V1']['gain']
s, C1, R1, L1 = rs.as_symbols('s C1 R1 L1')
HS = sympy.lambdify(w, Hs.subs({s:I*w, C1:3.2e-12, R1:25., L1:2e-6}))
np.allclose(dB20(abs(HS(rac.get_x()))), dB20(abs(Hl(rac.get_x()))), atol=1)

#PZ and AC together
figure(figsize=figsize);  title('Series RLC passband: TFs compared')
semilogx(rac.get_x()/2/np.pi, dB20(abs(rac['vout'])),
         label='TF from AC analysis')
semilogx(rac.get_x()/2/np.pi, dB20(abs(Hl(rac.get_x()))), 'o', ms=4,
         label='TF from PZ analysis')
semilogx(rac.get_x()/2/np.pi, dB20(abs(HS(rac.get_x()))), '-', lw=10,
         alpha=.2, label='TF from symbolic analysis')
vlines(1.07297e+08, *gca().get_ylim(), alpha=.4)
text(7e8/2/np.pi, -45, '$f_d = 107.297\\, \\mathrm{MHz}$', fontsize=20)
legend(); xlabel('Frequency [Hz]'); ylabel('|H(w)| [dB]');
xlim(4e7, 3e8); ylim(-50, 1);
