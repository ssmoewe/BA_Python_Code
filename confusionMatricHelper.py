import os
import time

def dayCalc(day):
    return weekdays[day%7]

def intCalc(weekday):
    switcher = {
        "friday": 0,
        "saturday": 1,
        "sunday": 2,
        "monday": 3,
        "tuesday": 4,
        "wednesday": 5,
        "thursday": 6
    }
    return switcher.get(weekday)

minutes = [1, 5, 15]
amountCentroids = [2, 4, 7]
weekdays = ['friday', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday']
directory = "D:\\EDR Visualisazion\\kmeans"

for i in range(0, len(minutes)):
    for j in range(0, len(amountCentroids)):
        file = "k-means (" + str(amountCentroids[j]) + " centroids, " + str(minutes[i]) + "min).txt"
        
        with open(os.path.join(directory, file)) as rf1:
            for lineNo, line in enumerate(rf1):
                values =  [int(numeric_string) for numeric_string in line.split()]
                counter = [0 for h in range(7)]
                datesWS = [[], [], [], []]
                for k in range(0, len(values)):
                    if 84 < values[k] < 295:
                        if dayCalc(values[k]) == 'saturday' or dayCalc(values[k]) == 'sunday':
                            datesWS[0].append(values[k])
                        else:datesWS[1].append(values[k])
                    else:
                        if dayCalc(values[k]) == 'saturday' or dayCalc(values[k]) == 'sunday':
                            datesWS[2].append(values[k])
                        else: datesWS[3].append(values[k])
                    
                    counter[values[k]%7] += 1 #counts amount of certain days
                
                filename = "confusion (" + str(amountCentroids[j]) + " c, " + str(minutes[i]) + "min, c-no. " + str(lineNo + 1) + ").txt"
                wf1 = open(os.path.join(directory, filename), "w+")
                for q in range(0, len(counter)):
                    wf1.write(str(counter[q]) + "x " + weekdays[q] + "\n")
                
                wf1.write("\n\n" + str(len(datesWS[0])) + "x\t summer Weekends")
                wf1.write("\n" + str(len(datesWS[1])) + "x\t summer Weekdays")
                wf1.write("\n" + str(len(datesWS[2])) + "x\t winter Weekends")
                wf1.write("\n" + str(len(datesWS[3])) + "x\t winter Weekdays")
                         
                wf1.close()