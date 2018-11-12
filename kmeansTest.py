import pandas as pd
import numpy as np
from numpy import array
import os
import time

start = time.time()

minutes = 15
amountCentroids = 2
savepath = "D:\\EDR Visualisazion"
directory = "D:\\EDR-Daten Processed Stash"
filename = "2016 - " + str(minutes) + "Min Steps.csv"
writefile = "k-means (" + str(amountCentroids) + " centroids, " + str(minutes) + "min).txt"
file = os.path.join(directory, filename)

result = pd.read_csv(file, sep=';', header=0)
result["PowerP"] = result["PowerP"].abs()

fill = []
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
    centroids = fill[np.random.randint(0, fill.shape[0], num_clust)]

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
centroids = k_means(fill, amountCentroids, 100)
t2 = time.time()
print("Took {} seconds".format(t2 - t1))

sort = []
for i in range(amountCentroids):
    sort.append([])
    
for i in range(0, len(fill)):
    minDist = float("inf")
    clust = -1
    for j in range(0, len(centroids)):
        dist = euclid_dist(fill[i], centroids[j])
        if dist < minDist:
            minDist = dist
            clust = j
    sort[clust].append((i, fill[i]))
    
wf1 = open(os.path.join(directory, writefile), "w")
for i in range(0, len(sort)):
    tmp = ""
    for j in range(0, len(sort[i])-1):
        tmp += str(sort[i][j][0]) + ", "
    tmp += str(sort[i][-1][0])
    wf1.write(tmp)
    wf1.write("\n")

wf1.close()






