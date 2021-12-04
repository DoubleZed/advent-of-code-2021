import os

inputPath = os.path.join(os.getcwd(),"input","input_day2.txt")
commandInput = [line.rstrip() for line in open(inputPath,"r")]
commandList = []
for item in commandInput:
    commandList.append(item.split())

horizontal = 0
vertical = 0

for command, value in commandList:
    if command == 'forward':
        horizontal += int(value)
    elif command == 'up':
        vertical -= int(value)
    elif command == 'down':
        vertical += int(value)

print(horizontal*vertical)
