import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy

savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash"
filename = "2016 - 15Min Steps.csv"
file = os.path.join(directory, filename)


result = pd.read_csv(file, sep=';', header=0)
result["Date"] = pd.to_datetime(result["Time"])
data = result.loc[:, ["PowerP"]]
data = data.set_index(result.Date)
data["PowerP"] = pd.to_numeric(data["PowerP"], downcast="float", errors="coerce")

#data.plot()

#weekly = data.resample('W').mean()
#daily = data.resample('D').mean()
#by_time = data.groupby(data.index.time).mean()
#hourly_ticks = 3 * 60 *  60 * np.arange(9)
#
#by_time.plot(xticks=hourly_ticks, style=[":", "--", "-"])
#daily.rolling(15, center=True).sum().plot(style=[":", "--", "-"])
#weekly.plot(style=[":", "--", "-"])

result2 = pd.read_csv(file, sep=';', header=0)
df = result2.loc[:,["Time", "PowerP"]]
df["PowerP"] = pd.to_numeric(df["PowerP"], errors="coerce")
df["Time"] = pd.to_datetime(df["Time"])
df = df.groupby(["Time"]).sum().reset_index()
#df.plot.line(x = "Time", y="PowerP", figsize=(18,9), linewidth=5, fontsize=20)
#plt.plot(df.Time, df.PowerP)

mon = df["Time"]
temp = pd.DatetimeIndex(mon)
month = pd.Series(temp.month)
tbp = df.drop(["Time"], axis=1)
tbp = tbp.join(month)
#tbp.plot.scatter(x="PowerP", y="Time", figsize=(16,8), linewidth=5, fontsize=20)
#plt.show()
#plt.clf()
#plt.figsize = (16,8)
#plt.linewidth = 5
#plt.fontsize = 20
#plt.xlabel = "PowerP"
#plt.ylabel = "Time"
#plt.scatter(tbp.PowerP, tbp.Time)
#df["PowerP"].rolling(5).mean().plot(figsize=(20,10), linewidth=5, fontsize=20)
#df["PowerP"].diff(periods=15).plot(figsize=(20,10), linewidth=5, fontsize=20)
#plt.plot(df["PowerP"].diff(periods=15))
#plt.show()
pd.plotting.autocorrelation_plot(df.PowerP)


plt.savefig(os.path.join(savepath, "D Test.pdf"), bbox_inches='tight', papertype="ledger", format="pdf")