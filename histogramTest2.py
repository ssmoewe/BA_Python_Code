import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy

savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash\\temp"
dataCollector = []
kw = 51

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    df = pd.read_csv(file, sep=';', parse_dates=[[0, 0]])
    dataCollector.append(df)

continuousData = pd.concat(dataCollector, ignore_index=True)
useData = continuousData.PowerP.interpolate().values
derivData = scipy.diff(useData)



plt.figure(figsize=(20,5))
#plt.xlim(2000, 12300)
binwidth = 5

plt.xlabel('Derivation of Power ($W$)')
plt.ylabel("#Items")
plt.title("Deriv Histogram\nwith Binsize: " + str(binwidth))
(n, bins, patches) = plt.hist(derivData, bins=np.arange(min(derivData), max(derivData) + binwidth, binwidth))
plt.savefig(os.path.join(savepath, "KW" + str(kw) + "-15Min-DerivHistogram.pdf"), bbox_inches='tight', papertype="ledger", format="pdf")
plt.clf()

plt.xlabel('Power ($W$)')
plt.ylabel("#Items")
plt.title("Histogram\nwith Binsize: " + str(binwidth))
(n, bins, patches) = plt.hist(useData, bins=np.arange(min(useData), max(useData) + binwidth, binwidth))
plt.savefig(os.path.join(savepath, "KW" + str(kw) + "-15Min-Histogram.pdf"), bbox_inches='tight', papertype="ledger", format="pdf")
plt.clf()
