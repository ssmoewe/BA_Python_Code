import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#%pylab inline --no-import-all

t = np.linspace(0, 2*np.pi, 1000, endpoint=True)
f = 3.0 # Frequency in Hz
A = 100.0 # Amplitude in Unit
s = A * np.sin(2*np.pi*f*t) # Signal

Y = np.fft.fft(s)

N = int(len(Y)/2+1)

dt = t[1] - t[0]
fa = 1.0/dt # scan frequency
X = np.linspace(0, fa/2, N, endpoint=True)

hann = np.hanning(len(s))
hamm = np.hamming(len(s))
black= np.blackman(len(s))

Yhann = np.fft.fft(hann*s)

directory = "D:\\EDR-Daten Preprocessed Stash\\1Min7CO"
filename = "KIT-EDR-CONVLOG-2016-01-04-1min.csv"
file = os.path.join(directory, filename)

df = pd.read_csv(file, sep=';', parse_dates=[[0, 0]])
df.PowerP = df.PowerP.interpolate()

plt.figure(figsize=(14,5))
df.PowerP.plot()

hann = np.hanning(len(df.PowerP.values))

Y = np.fft.fft(hann*df.PowerP.values)

N = int(len(Y)/2+1)
fa = 1.0/(1.0*60.0) # every 15 minutes
print('fa=%.4fHz (Frequency)' % fa)

X = np.linspace(0, fa/2, N, endpoint=True)

#plt.plot(X, 2.0*np.abs(Y[:N])/N)
#plt.xlabel('Frequency ($Hz$)')
#plt.ylabel('Power')

Xp = 1.0/X # in seconds
Xph= Xp/(60.0*60.0) # in hours

plt.figure(figsize=(15,6))
plt.plot(Xph, 2.0*np.abs(Y[:N])/N)
    #plt.xticks([12, 24, 33, 84, 168])

plt.xlabel('Period ($h$)')
