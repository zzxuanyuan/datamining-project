import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N)
#y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
y = np.sin(50.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N)
print len(xf)
print len(yf)
fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N]))
print np.abs(yf[:N])
power = 0
for i in yf:
	power += math.pow(np.abs(i),2)
print power
plt.show()
