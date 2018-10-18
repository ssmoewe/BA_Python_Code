import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

kw = 36

savepath = "D:\\EDR Visualisazion"

directory = "D:\\EDR-Daten Preprocessed Stash\\1Min7CO\\temp"
test = []

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    df = pd.read_csv(file, sep=';', parse_dates=[[0, 0]])
    test.append(df)

cont = pd.concat(test, ignore_index=True)

cont.PowerP = cont.PowerP.interpolate()


plt.figure(figsize=(14,5))
#df1.PowerP.plot()
plt.plot(cont.PowerP)
plt.xlim(0, None)
plt.ylim(0, None)
plt.ylabel('Power [$W$]')
plt.xlabel("Time in Minutes")
plt.title("Power KW1 2016")
plt.grid(linestyle="--")
plt.savefig(os.path.join(savepath, "2016 1M - KW" + str(kw) + ".pdf"), format="pdf")

hann = np.hanning(len(cont.PowerP.values))  #Hanning Filter

Y = np.fft.fft(hann*cont.PowerP.values)     #FFT

N = int(len(Y)/2+1)                         
fa = 1.0/(1.0*60.0)
#fa = 1.0                        # every 1 minutes
print('fa=%.4fHz (Frequency)' % fa)

X = np.linspace(0, fa/2, N, endpoint=True)

plt.figure(figsize=(15,6))
plt.plot(X, 2.0*np.abs(Y[:N])/N)
plt.xlabel('Frequency ($Hz$)')
plt.ylabel('Power [$W$]')
plt.title("FFT")
plt.savefig(os.path.join(savepath, "2016 1M - KW" + str(kw) + " FFT.pdf"), format="pdf")

Xp = 1.0/X          # in seconds
Xph= Xp/(60.0*60.0) # in hours

plt.figure(figsize=(15,6))
plt.plot(Xph, 2.0*np.abs(Y[:N])/N)
plt.xlabel('Period ($h$)')
plt.ylabel('Power [$W$]')
plt.grid(linestyle=":")
plt.xscale("log")
plt.savefig(os.path.join(savepath, "2016 1M - KW" + str(kw) + " FFT in Period.pdf"), bbox_inches='tight', papertype="ledger", format="pdf")