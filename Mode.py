import csv
from collections import Counter
with open ('HeightWeight.csv', newline = '') as Hw : 
    reader = csv.reader(Hw)
    fileData = list(reader)

fileData.pop(0)

newList = []
for counter in range(len(fileData)) : 
    newRow = fileData[counter][1]
    newList.append(newRow)

noOfRows = len(newList)

# use Counter method to get number of occurences
data = Counter(newList)
get_mode = dict(data)
mode = []
mode2 = []
mode3 = []

for k, v in get_mode.items() : 
    k = float(k)
    if (50 < k < 60) : 
        if (v == max(list(data.values()))) : 
            mode.append(k)
    elif (60 < k < 70) : 
        if (v == max(list(data.values()))) : 
            mode2.append(k)

    elif (70 < k < 80) : 
        if (v == max(list(data.values()))) : 
            mode3.append(k)

if (len(mode) > len(mode2) and len(mode3)) : 
    print ("Mode is " + ',' + .join(map(str, mode)))

elif (len(mode2) > len(mode) and len(mode3)) : 
    print ("Mode is " + ',' + .join(map(str, mode2)))

elif (len(mode3) > len(mode2) and len(mode)) : 
    print ("Mode is " + ',' + .join(map(str, mode3)))