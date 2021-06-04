import csv
from collections import Counter
with open ('AgeWeight.csv', newline = '') as f : 
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

newList = []
for counter in range(len(fileData)) : 
    newRow = fileData[counter][1]
    newList.append(newRow)


data = Counter(newList)
get_mode_range = {
                    "50-60":0,
                    "60-70":0,
                    "70-80":0
}


for height, occurence in data.items() : 
    height = float(height)
    if (50 < height < 60) : 
        get_mode_range["50-60"] += occurence

    elif (60 < height < 70) : 
        get_mode_range["60-70"] += occurence

    elif (70 < height < 80) : 
        get_mode_range["70-80"] += occurence

mode_range, mode_occurence = 0,0
for range, occurence in get_mode_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence =  [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"The mode is {mode:2f}")