import os
import collections

inputPath = os.path.join(os.getcwd(),"input","input_day3.txt")
lineInput = [line.rstrip() for line in open(inputPath,"r")]
numLines = sum(1 for line in lineInput)
#print(numLines)
lineList = []
transposedList  = []
bitList = []
#print(lineInput[0])
#print(lineInput[0][4])

#for i in range(numLines-1):
#    for j in range(len(lineInput[0])):
#        if lineInput[i][j]
 #  if lineInput[]

gammaRate = ""
for i in range(len(lineInput[0])):
    zeros = 0
    ones = 0
    for j in range(numLines-1):
        if lineInput[j][i] == "0":
            zeros += 1
        elif lineInput[j][i] == "1":
            ones += 1
    #print (zeros)
    #print (ones)
    if zeros > ones:
        gammaRate += str(0)
    else:
        gammaRate += str(1)

print(gammaRate)
print(int(gammaRate, 2))

#Binary to int:
#int(b, 2)
        




#    for i in range(len(item)):

   #     zeros = 0
  #      ones = 0
#        if item[i] == 0:
#            int(zeros) += 1



#    nBits = ""
#    for i in range(len(item)):
  #      nBits+=str(item[i])
    #print(nBits)
    #lineList.append(item.split())
#    transposedList.append(nBits)
    #print (item[0:1])
#print (transposedList)

#print (lineInput)
#print (lineList)