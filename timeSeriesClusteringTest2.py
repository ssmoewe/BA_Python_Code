import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy
import fbprophet
from sklearn.preprocessing import MinMaxScaler

savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash"
filename = "2016 - 15Min Steps.csv"
file = os.path.join(directory, filename)


result = pd.read_csv(file, sep=';', header=0)
result["PowerP"] = result["PowerP"].abs()
result["Date"] = pd.to_datetime(result["Time"])
data = result.loc[:, ["PowerP"]]
data = data.set_index(result.Date)
data["PowerP"] = pd.to_numeric(data["PowerP"], downcast="float", errors="coerce")

weekly = data.resample('W').mean()
daily = data.resample('D').mean()
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 3 * 60 *  60 * np.arange(9)

#by_time.plot(xticks=hourly_ticks, style=[":", "--", "-"])
#daily.rolling(15, center=True).sum().plot(style=[":", "--", "-"])
#weekly.plot(style=[":", "--", "-"])

df2 = daily
df2.reset_index(inplace=True)
df2 = df2.rename(columns={"Date": "ds", "PowerP": "y"})
#plt.plot(df2["ds"], df2["y"])
#plt.show()

df2prophet = fbprophet.Prophet(changepoint_prior_scale=0.05)
df2prophet.fit(df2)

df2forecast = df2prophet.make_future_dataframe(periods=30*2, freq="D")
df2forecast = df2prophet.predict(df2forecast)

#df2prophet.plot(df2forecast, xlabel = "Date", ylabel="W/H")
#plt.title("simple test")
#
#df2prophet.plot_components(df2forecast, weekly_start=1)
#fig = plt.gcf()
#fig.savefig(os.path.join(savepath, "test2.pdf"))


#mydata = daily.loc[:, ["PowerP"]]
#mydata = mydata.set_index(daily.Date)
#values = mydata["PowerP"].values.reshape(-1,1)
#values = values.astype("float32")
#scaler = MinMaxScaler(feature_range=(0,1))
#scaled = scaler.fit_transform(values)
#trainsize = int(len(scaled) * 0.8)
#testsize = len(scaled) - trainsize
#train, test = scaled[0:trainsize,:], scaled[trainsize:len(scaled),:]
#print(len(train), len(test))












