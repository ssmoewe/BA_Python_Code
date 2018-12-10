import os
import csv
import sys
import time

t1 = time.time()
savepath = "D:\\EDR-Daten Processed Stash"
temp = "D:\\EDR-Daten Processed Stash\\1Min0CO"
allFiles = len([name for name in os.listdir(temp) if os.path.isfile(os.path.join(temp, name))]) * 3
times = [1, 5, 15]
iterator = 0

firstLine = ['Time', 'ms+-', 'PowerP', 'Stabw P', 'PowerQ', 'Gleichspannung', 'Gleichrichtwert', 'Effektivwert', 'Scheitelfaktor',
             'Amplitude', 'Abs. MaxA', 'Stabw Ieff', 'Stabw Imid', 'Stabw Iss', 'THD', 'Phase', 'Number', 'OW0 [%]', 'OW2 [%]',
             'OW3 [%]', 'OW4 [%]', 'OW5 [%]', 'OW6 [%]', 'OW7 [%]', 'OW8 [%]', 'OW9 [%]', 'OW10 [%]', 'OW11 [%]', 'OW12 [%]',
             'OW13 [%]', 'OW14 [%]', 'Temperature', 'Conversion', 'EDRchannel', 'Campaign', 'AcquisitionError', 'PPS', '']

for i in range(0, len(times)):
    directory = "D:\\EDR-Daten Processed Stash\\" + str(times[i]) + "Min0CO"
    outFile = os.path.join(savepath, "2016 - " + str(times[i]) + "Min Steps.csv")
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