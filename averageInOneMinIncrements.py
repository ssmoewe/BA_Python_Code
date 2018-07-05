#! python 3
# minuteAverage.py - Averages in 1 minute blocks

import os, csv

os.chdir("C:\\Users\\Linus\\Documents\\Bachelorarbeit")

readFile = open("Files\\example.csv")
reader = csv.reader(readFile, delimiter=";")
readData = list(reader)
writeFile = open("Files\\Output\\average.csv", "w", newline="")
writer = csv.writer(writeFile, delimiter=";")

writer.writerow(readData[0])

for i in range(1, len(readData), 60):
    currentSum = {}
    for j in range(0, 60):
        for rows in range(0, len(readData[0])-1):
            currentSum.setdefault(readData[0][rows], 0)
            if rows == 0:
                currentSum[readData[0][rows]] = readData[i+j][0][-8:-3]
            else:
                currentSum[readData[0][rows]] += float(readData[i+j][rows])
    for x in currentSum:
        if x != "Time":
            currentSum[x] /= 60
            currentSum[x][0:9]
    writer.writerow(currentSum.values())

writeFile.close()
readFile.close()
