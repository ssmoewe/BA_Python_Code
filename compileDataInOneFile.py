import os
import csv
import sys
import time

savepath = "D:\\EDR-Daten Processed Stash"
directory = "D:\\EDR-Daten Processed Stash\\15Min7CO"
#directory = "C:\\Users\\Arne\\bwSyncAndShare\\Linus-BA-EDR-Data (Richard Jumar)\\EDR0006_2016_L4I_csv"
firstLine = ['Time', 'ms+-', 'PowerP', 'Stabw P', 'PowerQ', 'Gleichspannung', 'Gleichrichtwert', 'Effektivwert', 'Scheitelfaktor',
             'Amplitude', 'Abs. MaxA', 'Stabw Ieff', 'Stabw Imid', 'Stabw Iss', 'THD', 'Phase', 'Number', 'OW0 [%]', 'OW2 [%]',
             'OW3 [%]', 'OW4 [%]', 'OW5 [%]', 'OW6 [%]', 'OW7 [%]', 'OW8 [%]', 'OW9 [%]', 'OW10 [%]', 'OW11 [%]', 'OW12 [%]',
             'OW13 [%]', 'OW14 [%]', 'Temperature', 'Conversion', 'EDRchannel', 'Campaign', 'AcquisitionError', 'PPS', '']

t1 = time.time()
allFiles = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
iterator = 0
outFile = os.path.join(savepath, "2016 - 15Min 7CO.csv")
wf1 = open(outFile, "w", newline="")
writer = csv.writer(wf1, delimiter=";")
writer.writerow(firstLine)

for filename in os.listdir(directory):
    rf = open(os.path.join(directory, filename))
    reader = csv.reader(rf, delimiter=";")
    readData = list(reader)
    for i in range(1, len(readData)):
        writer.writerow(readData[i])
    rf.close()
    
    sys.stdout.write("\r{0} %".format(round(iterator/allFiles * 100, 2)))
    sys.stdout.flush()

#    if iterator % 10 == 0:
#        print(str(round(iterator/allFiles * 100, 2)) + "% done")   
     
    iterator += 1

wf1.close()
t2 = time.time()
print("\nTook {} seconds".format(t2 - t1))