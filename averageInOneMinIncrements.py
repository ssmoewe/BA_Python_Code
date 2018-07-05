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
    summe = {}
    for j in range(0, 60):
        for zeilen in range(0, len(readData[0])-1):
            summe.setdefault(readData[0][zeilen], 0)
            if zeilen == 0:
                summe[readData[0][zeilen]] = readData[i+j][0][-8:-3]
            else:
                summe[readData[0][zeilen]] += float(readData[i+j][zeilen])
    for x in summe:
        if x != "Time":
            summe[x] /= 60
            summe[x][0:9]
    writer.writerow(summe.values())

writeFile.close()
readFile.close()
