import os

inputPath = os.path.join(os.getcwd(),"input","input_day1.txt")
measureIncrease = 0
measurementList = [line.rstrip() for line in open(inputPath,"r")]
increaseCount = 0
for x,y in zip(measurementList, measurementList[1:]):
    if int(x) < int(y):
        increaseCount += 1
print (increaseCount)
       
