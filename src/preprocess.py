import sys
import copy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, ifft
from extractfeature import CalFrame

# --- SensorLog sampling rate is 33 Hz --- #
freq = 33 # 33 Hz ( there are 33 samples within a second )

# --- determine activity by file name --- #
name = sys.argv[1]
print "naem",name
print "name[0:3]",name[0:3]
sit = "sit"
stand = "stand"
run = "run"
upstairs = "upstairs"
downstairs = "downstairs"

if sit in name:
	activity = "sit"
elif stand in name:
	activity = "stand"
elif run in name:
	activity = "run"
elif upstairs in name:
	activity = "upstairs"
elif downstairs in name:
	activity = "downstairs"
else:
	print "Error: Activity Unknown"
	activity = "unknown"

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
print "Activity=",activity
# --- Create empty file --- #
fname = ['DC X','Time Mean X','Power X','Frequency-domain Entropy X','DC Y','Time Mean Y','Power Y','Frequency-domain Entropy Y','DC Z','Time Mean Z','Power Z','Frequency-domain Entropy Z','Activity']
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
	featureList.extend([activity])
	print "featureList=",featureList
	dftemp = pd.DataFrame([featureList], columns=fname)
	print "dftemp:",dftemp
	fdf = fdf.append(dftemp,ignore_index=True)
	print "fdf:",fdf

print fdf
fdf.to_csv(path_or_buf=sys.argv[3],sep=',',index=False)
