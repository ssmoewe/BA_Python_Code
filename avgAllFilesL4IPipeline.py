#! python 3
# minuteAverage.py - Averages in 1 minute blocks

import os, csv
from decimal import Decimal

def averageByTime(minutes, readFile, writeFile):
    seconds = minutes * 60
    
    rf = open(readFile)
    reader = csv.reader(rf, delimiter=";")
    readData = list(reader)
    wf = open(writeFile, "w", newline="")
    writer = csv.writer(wf, delimiter=";")

    writer.writerow(readData[0])

    for i in range(1, len(readData), seconds):
        currentSum = {}
        for j in range(0, seconds):
            for rows in range(0, len(readData[0])-1):
                currentSum.setdefault(readData[0][rows], 0)
                if (rows == 0) or (rows == 34):
                    #onlyNumeric = re.sub('[^0-9]','', readData[i+j][0][-8:-3])
                    currentSum[readData[0][rows]] = readData[i+j][0]
                else:
                    currentSum[readData[0][rows]] += float(readData[i+j][rows])
        for x in currentSum:
            if x == "Time" or x == "Campaign":
                continue
            else:
                currentSum[x] /= seconds
                currentSum[x] = round(Decimal(currentSum[x]), 10)
        writer.writerow(currentSum.values())

    wf.close()
    rf.close()

mins = [5, 15]
directory = "C:\\Users\\Arne\\bwSyncAndShare\\Linus-BA-EDR-Data (Richard Jumar)\\EDR0006_2016_L4I_csv"
allFiles = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]) * 2
iterator = 0
for i in range(0, len(mins)):
    writepath = "D:\\EDR-Daten Processed Stash\\" + str(mins[i]) + "Min0CO"
    for filename in os.listdir(directory):
        readFile = os.path.join(directory, filename)
        output = filename[0:15]+'-'+filename[25:29]+'-'+filename[29:31]+'-'+filename[31:33]+'-'+str(mins[i])+'min.csv'
        writeFile = os.path.join(writepath, output)
    
        averageByTime(mins[i], readFile, writeFile)
        
        if iterator % 10 == 0:
            print(str(round(iterator/allFiles * 100, 2)) + "% done")
        iterator += 1

