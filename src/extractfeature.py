import math
import numpy as np
import pandas as pd
from scipy.fftpack import fft, ifft

def CalTimeMean(winDataTime):
	mean = 0
	sumt = 0
	for i in winDataTime:
		sumt += i
	mean = sumt/len(winDataTime)
	return mean

def CalFreqPower(winDataFreq):
	power = 0
	for i in range(0,len(winDataFreq)):
		power += math.pow(winDataFreq[i],2)
	return power

def CalFreqEntropy(winDataFreq):
	N         = len(winDataFreq)
	fname     = ['Power']
	powerRaw  = np.zeros(N)
	powerNor  = np.zeros(N)
	entropy   = np.zeros(N)
	for i in range(0,N):
		powerRaw[i] = math.pow(winDataFreq[i],2)/N
	powerSum = sum(powerRaw)
	for i in range(0,N):
		powerNor[i] = powerRaw[i]/powerSum
	for i in range(0,N):
		if powerNor[i] is 0:
			entropy[i] = 0
		else:
			entropy[i] = -(powerNor[i]*(math.log(powerNor[i])))

	H = sum(entropy)
	return H

def CalFrame(winDataTime):
	N            = len(winDataTime)
	fftData      = fft(winDataTime)
	dc           = 2.0/N * np.abs(fftData[0])
	winDataFreq  = 2.0/N * np.abs(fftData[1:N])
	timeMean     = CalTimeMean(winDataTime)
#	timeMin      = math.min(winDataTime)
#	timeMax      = math.max(winDataTime)
	freqPower    = CalFreqPower(winDataFreq)
	freqEntropy  = CalFreqEntropy(winDataFreq)

	ret = [dc,timeMean,freqPower,freqEntropy]
	return ret

