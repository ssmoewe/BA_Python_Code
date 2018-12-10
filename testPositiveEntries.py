import os
import csv
import sys
import time

directory = "C:\\Users\\Arne\\bwSyncAndShare\\Linus-BA-EDR-Data (Richard Jumar)\\EDR0006_2016_L4I_csv"

t1 = time.time()
allFiles = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
iterator = 0

for filename in os.listdir(directory):
    rf = open(os.path.join(directory, filename))
    reader = csv.reader(rf, delimiter=";")
    readData = list(reader)
    calc = 0
    first = []
    found = False
    for i in range(1, len(readData)):
        if '-' in readData[i][2]:
            found = True
            calc += 1
            first.append(i)
          
    if found:
        print("\n", filename, calc, first)
        rf.close()
    
    sys.stdout.write("\r{0} %".format(round(iterator/allFiles * 100, 2)))
    sys.stdout.flush()
    iterator += 1
    

t2 = time.time()
print("\nTook {} seconds".format(t2 - t1))