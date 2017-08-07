import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.legend_handler import HandlerLine2D

def _e( N ):
	E = 1
	I = 1
	l = 1
	return l*math.sqrt(float(abs(N))/float(E*I))

def _A( e, N ):
	if e <= 0:
		return 4
	# positive normal pressure
	if N < 0:
		return (e * math.sin(e) - e**2 * math.cos(e))\
						/(2 * (1 - math.cos(e)) - (e * math.sin(e)))
	# negative normal pressure
	else:
		return -1 * (( e * math.sinh( e ) - e**2 * math.cosh( e ) )\
						/(2 * ( 1- math.cosh(e)) + e * math.sinh(e)))

def _B( e, N ):
	if e <= 0:
		return 2
	# positive normal pressure
	if N < 0:
		return (e**2 - e * math.sin(e) )\
						/( 2*(1 - math.cos(e)) - e * math.sin(e) )
	# negative normal pressure
	else:
		return -1 * ((e**2 - e * math.sinh(e))\
						/(2*(1 - math.cosh(e)) + e * math.sinh(e)))

def _C( e, N ):
	if e <= 0:
		return 3
	# positive normal pressure
	if N < 0:
		return (e**2 * math.sin(e))\
						/(math.sin(e) - e * math.cos(e))
	# negative normal pressure
	else:
		return -1 * ((e**2 * math.sinh(e))\
						/( math.sinh(e) - e * math.cosh(e)))

def _D( e, N ):
	return _A(e, N) + _B(e, N)


#plot 1
e = np.arange(0.0, 6.0, 0.01)
N = -1
A = []
B = []
C = []
D = []

for _e in e:
	A.append(_A(_e,N))

for _e in e:
	B.append(_B(_e,N))

for _e in np.arange(0.0, 4.45, 0.01):
	C.append(_C(_e,N))
for _e in np.arange(4.45, 6.0, 0.01):
	C.append(-100)

for _e in e:
	D.append(_D(_e,N))

plt.plot(e, A)
plt.plot(e, B)
plt.plot(e, C)
plt.plot(e, D)

axes = plt.gca()

axes.annotate('a', xy=(0.03, 4.1))
axes.annotate('b', xy=(0.03, 2.1))
axes.annotate('c', xy=(0.03, 3.1))
axes.annotate('d', xy=(0.03, 6.1))

axes.set_ylim([-2,8])

plt.xlabel(r'$\epsilon$')
plt.grid(True)
plt.savefig("/home/couchsofa/Thesis/paper/images/coeff_N_neg.png")
plt.clf()

#plot 2
e = np.arange(0.0, 6.0, 0.01)
N = 1
A = []
B = []
C = []
D = []

for _e in e:
	A.append(_A(_e,N))

for _e in e:
	B.append(_B(_e,N))

for _e in e:
	C.append(_C(_e,N))

for _e in e:
	D.append(_D(_e,N))

plt.plot(e, A)
plt.plot(e, B)
plt.plot(e, C)
plt.plot(e, D)

axes = plt.gca()

axes.annotate('a', xy=(0.03, 4.1))
axes.annotate('b', xy=(0.03, 2.1))
axes.annotate('c', xy=(0.03, 3.1))
axes.annotate('d', xy=(0.03, 6.1))

axes.set_ylim([0,10])

plt.xlabel(r'$\epsilon$')
plt.grid(True)
plt.savefig("/home/couchsofa/Thesis/paper/images/coeff_N_pos.png")
