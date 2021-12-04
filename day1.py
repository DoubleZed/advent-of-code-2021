import os
import pandas as pd
### Part one ###
""" inputPath = os.path.join(os.getcwd(),"input","input_day1.txt")
measureIncrease = 0
measurementList = [line.rstrip() for line in open(inputPath,"r")]
increaseCount = 0
for x,y in zip(measurementList, measurementList[1:]):
    if int(x) < int(y):
        increaseCount += 1
print (increaseCount) """


### Part two ###
inputPath = os.path.join(os.getcwd(),"input","input_day1.txt")
measureIncrease = 0
measurementList = [int(line.rstrip()) for line in open(inputPath,"r")]
threeMeasurementList = pd.DataFrame(
    {'1st':measurementList[:-2],
     '2nd':measurementList[1:-1],
     '3rd':measurementList[2:]
    })

sumList = []
for i in range(len(threeMeasurementList)):
    sum = threeMeasurementList.loc[i]['1st'] + threeMeasurementList.loc[i]['2nd'] + threeMeasurementList.loc[i]['3rd']
    sumList.append(int(sum))

increaseCount = 0
for index, value in enumerate(sumList[:-1]):
    if value < sumList[index+1]:
        increaseCount += 1
print (increaseCount)
