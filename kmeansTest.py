import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import os
import scipy
import time
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from scipy.cluster.hierarchy import dendrogram, linkage

start = time.time()

minutes = 15

savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash"
filename = "2016 - " + str(minutes) + "Min Steps.csv"
file = os.path.join(directory, filename)


result = pd.read_csv(file, sep=';', header=0)
result["PowerP"] = result["PowerP"].abs()

fill = []
#timestamps = []
#print(len(result["PowerP"]))
step = int(1440 / minutes)

for i in range(0, len(result["PowerP"]), step):
    temp = []
    for j in range(i, i + step):
        temp.append(result["PowerP"][j])
    fill.append(temp)
    
fill = array(fill)

def euclid_dist(t1, t2):
         return np.sqrt(((t1-t2)**2).sum())
def k_means(data, num_clust, num_iter):
#    centroids = fill[np.random.randint(0, fill.shape[0], num_clust)]
    centroids = fill

    for n in range(num_iter): 
        assignments={}
        for ind, i in enumerate(data):
            min_dist = float('inf') 
            closest_clust = None
            for c_ind, j in enumerate(centroids):
                dist = euclid_dist(i, j) 
                if dist < min_dist:
                   min_dist = dist
                   closest_clust = c_ind

            if closest_clust in assignments: 
                assignments[closest_clust].append(ind)
            else:
                assignments[closest_clust]=[] 
                assignments[closest_clust].append(ind)

        for key in assignments:
            clust_sum = 0
            for k in assignments[key]: 
                clust_sum = clust_sum + data[k]
            centroids[key] = [m / len(assignments[key]) for m in clust_sum] 

    return centroids

t1 = time.time()
centroids = k_means(fill, 7, 100)
t2 = time.time()
print("Took {} seconds".format(t2 - t1))
print(centroids)
for i in range(0, len(fill)):
    for j in range(0, len(centroids)):
#        print(i, j)
        if sorted(fill[i]) == sorted(centroids[j]):
            print (fill[i], j)
#        print(sorted(centroids[i]) == sorted(centroids[j]), i, j)



#plt.figure(figsize=(100, 40))
#plt.title("Clustering Dendrogram (k-means)")
#plt.xlabel("Index (corresponding to a date)")
#plt.ylabel("Distance")
#plt.rcParams.update({'font.size': 70})
#dendrogram(
#        centroids,
##        labels = timestamps,
#        leaf_rotation = 90,
#        leaf_font_size = 8.,
#        )
#
##plt.show()
#
#
#fig = plt.gcf()
#fig.savefig(os.path.join(savepath, "Dendrogram k-means Algorithm " + str(minutes) + "m.pdf"))