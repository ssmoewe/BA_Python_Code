import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

savepath = "D:\\EDR Visualisazion"

directory = "D:\\EDR-Daten Preprocessed Stash\\1Min7CO"
dir2 = "C:\\Users\\Linus\\bwSyncAndShare\\Linus-BA-EDR-Data (Richard Jumar)\\EDR0006_2016_L4I_csv"
f1 = "KIT-EDR-CONVLOG_EDR0006_T20160125_L4I.csv"
f2 = "KIT-EDR-CONVLOG_EDR0006_T20160126_L4I.csv"
f3 = "KIT-EDR-CONVLOG_EDR0006_T20160127_L4I.csv"
f4 = "KIT-EDR-CONVLOG_EDR0006_T20160128_L4I.csv"
f5 = "KIT-EDR-CONVLOG_EDR0006_T20160129_L4I.csv"
filename1 = "KIT-EDR-CONVLOG-2016-01-25-1min.csv"
filename2 = "KIT-EDR-CONVLOG-2016-01-26-1min.csv"
filename3 = "KIT-EDR-CONVLOG-2016-01-27-1min.csv"
filename4 = "KIT-EDR-CONVLOG-2016-01-28-1min.csv"
filename5 = "KIT-EDR-CONVLOG-2016-01-29-1min.csv"

file1 = os.path.join(directory, filename1)
file2 = os.path.join(directory, filename2)
file3 = os.path.join(directory, filename3)
file4 = os.path.join(directory, filename4)
file5 = os.path.join(directory, filename5)

df1 = pd.read_csv(file1, sep=';', parse_dates=[[0, 0]])
df2 = pd.read_csv(file2, sep=";", parse_dates=[[0, 0]])
df3 = pd.read_csv(file3, sep=";", parse_dates=[[0, 0]])
df4 = pd.read_csv(file4, sep=";", parse_dates=[[0, 0]])
df5 = pd.read_csv(file5, sep=";", parse_dates=[[0, 0]])

test = [df1, df2, df3, df4, df5]

cont = pd.concat(test, ignore_index=True)

cont.PowerP = cont.PowerP.interpolate()

plt.figure(figsize=(14,5))
#df1.PowerP.plot()
plt.plot(cont.PowerP)
plt.xlim(0, None)
plt.ylim(0, None)
plt.ylabel("Power")
plt.xlabel("Time in Minutes")
plt.title("Power KW1 2016")
plt.grid(linestyle="--")
plt.savefig(os.path.join(savepath, "2016 1M - KW4.pdf"), format="pdf")

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
plt.ylabel('Power')
plt.title("FFT")
plt.savefig(os.path.join(savepath, "2016 1M - KW4 FFT.pdf"), format="pdf")

Xp = 1.0/X          # in seconds
Xph= Xp/(60.0*60.0) # in hours

plt.figure(figsize=(15,6))
plt.plot(Xph, 2.0*np.abs(Y[:N])/N)
plt.xlabel('Period ($h$)')
plt.ylabel("Power")
plt.grid(linestyle=":")
plt.savefig(os.path.join(savepath, "2016 1M - KW4 FFT in Period.pdf"), bbox_inches='tight', papertype="ledger", format="pdf")