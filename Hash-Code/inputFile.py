# Serves to take in data from the text files

class Street():
    def __init__(self, start, end, name, L):
        self.start = start
        self.end = end
        self.name = name
        self.L = L

class Car():
    def __init__(self, numStreets, streets):
        self.numStreets= numStreets
        self.streets = streets # list of streets

def streetIn(streetList):
    streetInfo = []
    for index in range(len(streetList)):
        line = streetList[index]
        info = line.split(" ")
        #name = "s" + str(index)
        name = Street(info[0], info[1], info[2], info[3])
        streetInfo.append(name)
    return streetInfo

def carsIn(list_):
    carInfo = []
    for index in range(len(list_)):
        line = list_[index]
        info = line.split(" ")
        name = Car(None, [])
        for car in range(int(info[0])+1):
            if car == 0:
                name.numCars = info[car]
            else:
                name.streets.append(info[car])
        carInfo.append(name)
    return carInfo

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

streetInfo = streetIn(intersectionList)
carsInfo = carsIn(carsList)


print(streetInfo)
for i in range(intersections):
    print(streetInfo[i].name)

print(carsInfo)
for i in range(cars):
    print(carsInfo[i].streets)




    

# # listInfo = (firstLine.strip("\n")).split(" ")
# print(listInfo) # DEBUGGING
# print(intersections) # DEBUGGING
# print(cars) # DEBUGGING
# print("---")
# print(intersectionList)
# print(carsList)

file.close()