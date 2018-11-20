import os

directory = "D:\\EDR-Daten Processed Stash\\15Min0CO"
savepath =  "D:\\EDR-Daten Processed Stash"
savefile = "Index to Date.txt"

wf1 = open(os.path.join(savepath, savefile), "w+")
data = []

for no, filename in enumerate(os.listdir(directory)):
    wf1.write(str(no) + " " + filename[24:26] + "." + filename[21:23] + "\n")
    data.append(filename[24:26] + "." + filename[21:23])
    
wf1.close()
print(data, len(data))