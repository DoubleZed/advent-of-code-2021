import os
inputPath = os.path.join(os.getcwd(),"input","input_day2.txt")
commandList = [line.rstrip() for line in open(inputPath,"r")]
print(commandList)
