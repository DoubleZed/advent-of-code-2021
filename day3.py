import os

inputPath = os.path.join(os.getcwd(),"input","input_day3.txt")
lineInput = [line.rstrip() for line in open(inputPath,"r")]
lineList = []
for item in lineInput:
    lineList.append(item.split())

print (lineList)