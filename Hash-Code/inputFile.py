# Serves to take in data from the text files

file = open("a.txt")

data = file.readlines() 
intersectionList = []
carsList = []
listInfo = []

intersections = 0
cars = 0

for index in range(len(data)):
    line = data[index]
    line = line.strip("\n")
    if index == 0:
        listInfo = line.split(" ")
        intersections = int(listInfo[2])
        cars = int(listInfo[3])
        bonus = int(listInfo[4])
    if ( 1 <= index <= intersections):
        intersectionList.append(line)
    if ( intersections < index <= intersections + cars):
        carsList.append(line)



# listInfo = (firstLine.strip("\n")).split(" ")
print(listInfo) # DEBUGGING
print(intersections) # DEBUGGING
print(cars) # DEBUGGING
print("---")
print(intersectionList)
print(carsList)