import os

inputPath = os.path.join(os.getcwd(),"input","input_day2.txt")
commandInput = [line.rstrip() for line in open(inputPath,"r")]
commandList = []
for item in commandInput:
    commandList.append(item.split())


