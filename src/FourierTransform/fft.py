import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from scipy.fftpack import fft, ifft

# --- SensorLog sampling rate is 33 Hz --- #
freq = 33 # 33 Hz ( there are 33 samples within a second )

# --- read csv by Pandas --- #
df  = pd.read_csv(sys.argv[1])

# --- read accelerometer columns --- #
accx = df['accelerometerAccelerationX']
accy = df['accelerometerAccelerationY']
accz = df['accelerometerAccelerationZ']

# --- calculate fft --- #
fftx = fft(accx)
ffty = fft(accy)
fftz = fft(accz)

# --- frequency spectrum of Accelerometer{X,Y,Z}, frequency in -33~33 Hz --- #
samx = np.linspace(-33.0, 33.0, num=accx.size)
samy = np.linspace(-33.0, 33.0, num=accy.size)
samz = np.linspace(-33.0, 33.0, num=accz.size)

# --- fft{x,y,z} are complex number and abs calculate the modulus (x^2+y^2)^-2 --- #
valx = np.abs(fftx[0:accx.size])
valy = np.abs(ffty[0:accy.size])
valz = np.abs(fftz[0:accz.size])

# --- time samples of Accelerometer{X,Y,Z} the unit is second --- #
timx = np.linspace(0.0, accx.size/33, num=accx.size)
timy = np.linspace(0.0, accy.size/33, num=accy.size)
timz = np.linspace(0.0, accz.size/33, num=accz.size)

# --- Set Window Title --- #
fig = plt.gcf()
fig.canvas.set_window_title(sys.argv[1])

# --- Draw frequency and time domains --- #
fdx = fig.add_subplot(231)
fdx.set_title('Frequency Domain X')
fdx.set_xlabel('frequency (Hz)')
fdx.set_ylabel('acceleration (g=9.81 m/s^2)')
fdx.plot(samx,valx,'r')
plt.grid()
fdy = fig.add_subplot(232)
fdy.set_title('Frequency Domain Y')
fdy.set_xlabel('frequency (Hz)')
fdy.set_ylabel('acceleration (g=9.81 m/s^2)')
fdy.plot(samy,valy,'b')
plt.grid()
fdz = fig.add_subplot(233)
fdz.set_title('Frequency Domain Z')
fdz.set_xlabel('frequency (Hz)')
fdz.set_ylabel('acceleration (g=9.81 m/s^2)')
fdz.plot(samz,valz,'g')
plt.grid()
tdx = fig.add_subplot(234)
tdx.set_title('Time Domain X')
tdx.set_xlabel('time sample (s)')
tdx.set_ylabel('acceleration (g=9.81 m/s^2)')
tdx.plot(timx,accx,'r')
plt.grid()
tdy = fig.add_subplot(235)
tdy.set_title('Time Domain Y')
tdy.set_xlabel('time sample (s)')
tdy.set_ylabel('acceleration (g=9.81 m/s^2)')
tdy.plot(timy,accy,'b')
plt.grid()
tdz = fig.add_subplot(236)
tdz.set_title('Time Domain Z')
tdz.set_xlabel('time sample (s)')
tdz.set_ylabel('acceleration (g=9.81 m/s^2)')
tdz.plot(timz,accz,'g')
plt.grid()

plt.show()
