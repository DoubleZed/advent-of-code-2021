import os
import collections

inputPath = os.path.join(os.getcwd(),"input","input_day3.txt")
lineInput = [line.rstrip() for line in open(inputPath,"r")]
numLines = sum(1 for line in lineInput)

# Part One
""" #Getting Gamma Rate
gammaRate = ""
for i in range(len(lineInput[0])):
    zeros = 0
    ones = 0
    for j in range(numLines-1):
        if lineInput[j][i] == "0":
            zeros += 1
        elif lineInput[j][i] == "1":
            ones += 1
    if zeros > ones:
        gammaRate += str(0)
    else:
        gammaRate += str(1)

#Getting Epsilon Rate
epsilonRate = gammaRate.translate(str.maketrans("01","10"))

#Calculating Power Consumption in decimal
powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)
print(powerConsumption) """



#Part Two
def findMostLeastCommon (inputList,bitPosition,commonality):
    numListLines = numLines = sum(1 for line in inputList)
    zeros = 0
    ones = 0
    for j in range(numListLines-1):
        if inputList[j][bitPosition] == "0":
            zeros += 1
        elif inputList[j][bitPosition] == "1":
            ones += 1
    if commonality == "most":
        if ones >= zeros:
            commonValue = "1"
        else:
            commonValue = "0"            
    elif commonality == "least":
        if zeros >= ones:
            commonValue = "0"
        else:
            commonValue = "1"
    commonValues = [i for i in inputList if i.startswith(commonValue)]  
    return commonValues
