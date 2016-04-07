import sys
import copy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from extractfeature import CalFrame

# --- SensorLog sampling rate is 33 Hz --- #
freq = 33 # 33 Hz ( there are 33 samples within a second )

# --- read csv by Pandas --- #
df  = pd.read_csv(sys.argv[1])
# --- read window size --- #
winSize = int(sys.argv[2])
# --- read accelerometer columns --- #
accx = df['accelerometerAccelerationX']
accy = df['accelerometerAccelerationY']
accz = df['accelerometerAccelerationZ']

tot = accx.count()

winCount = tot/(winSize/2)-1
print "winCount=",winCount

# --- Create empty file --- #
fname = ['DC X','Time Mean X','Power X','Frequency-domain Entropy X','DC Y','Time Mean Y','Power Y','Frequency-domain Entropy Y','DC Z','Time Mean Z','Power Z','Frequency-domain Entropy Z']
fdf = pd.DataFrame(data=np.zeros((0,len(fname))), columns=fname)
for winIndex in range(0,winCount):
	startPos = winIndex * (winSize/2)
	middlePos = startPos + (winSize/2) - 1
	endPos = startPos + winSize - 1
	timeX = accx[startPos:endPos+1]
	timeY = accy[startPos:endPos+1]
	timeZ = accz[startPos:endPos+1]
	winDataTimeX = timeX.values
	winDataTimeY = timeY.values
	winDataTimeZ = timeZ.values
	featureX = CalFrame(winDataTimeX)
	featureY = CalFrame(winDataTimeY)
	featureZ = CalFrame(winDataTimeZ)
	featureList = []
	featureList.extend(featureX)
	featureList.extend(featureY)
	featureList.extend(featureZ)
	dftemp = pd.DataFrame([featureList], columns=fname)
	print "dftemp:",dftemp
	fdf = fdf.append(dftemp,ignore_index=True)
	print "fdf:",fdf

print fdf
