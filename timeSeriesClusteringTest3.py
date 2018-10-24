import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import scipy
import fbprophet
from sklearn.preprocessing import MinMaxScaler
from scipy.cluster.hierarchy import dendrogram, linkage

savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash"
filename = "2016 - 15Min Steps.csv"
file = os.path.join(directory, filename)


result = pd.read_csv(file, sep=';', header=0)
result["PowerP"] = result["PowerP"].abs()

fill = []
print(len(result["PowerP"]))

for i in range(0, len(result["PowerP"]), 96):
    temp = []
    for j in range(i, i+96):
        temp.append(result["PowerP"][j])
    fill.append(temp)


z = linkage(fill, method="median")

plt.figure(figsize=(100, 40))
plt.title("Clustering Dendrogram (Median)")
plt.xlabel("Index (corresponding to a date)")
plt.ylabel("Distance")
plt.rcParams.update({'font.size': 70})
dendrogram(
        z,
        leaf_rotation = 90,
        leaf_font_size = 8.,
        )

#plt.show()


fig = plt.gcf()
fig.savefig(os.path.join(savepath, "Dendrogram Median.pdf"))