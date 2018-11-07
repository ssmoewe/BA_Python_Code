import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from scipy.cluster.hierarchy import dendrogram, linkage

start = time.time()

minutes = 15

savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash"
filename = "2016 - " + str(minutes) + "Min Steps.csv"
file = os.path.join(directory, filename)

result = pd.read_csv(file, sep=';', header=0)
result["PowerP"] = result["PowerP"].abs()
#result["Time"] = [datetime.strptime(date, "%d.%m.%Y %H:%M:%S").date() for date in result["Time"]]

fill = []
#timestamps = []
#print(len(result["PowerP"]))
step = int(1440 / minutes)

for i in range(0, len(result["PowerP"]), step):
    temp = []
    for j in range(i, i + step):
        temp.append(result["PowerP"][j])
    fill.append(temp)

#for i in range(0, len(result["Time"]), step):
#    timestamps.append(result["Time"][i])

z = linkage(fill)

plt.figure(figsize=(100, 40))
plt.title("Clustering Dendrogram (Incremental  Algorithm)")
plt.xlabel("Index (corresponding to a week)")
plt.ylabel("Distance")
plt.rcParams.update({'font.size': 70})
dendrogram(
        z,
        leaf_rotation = 90,
        leaf_font_size = 8.,
        )

fig = plt.gcf()
fig.savefig(os.path.join(savepath, "Dendrogram Euclidian Algorithm " + str(minutes) + "m.pdf"))

print("Time elapsed in s", time.time() - start)