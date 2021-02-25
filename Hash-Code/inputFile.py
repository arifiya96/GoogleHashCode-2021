# Serves to take in data from the text files

class Street():
    def __init__(self, start, end, name, L):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.L = int(L)

class Car():
    def __init__(self, numStreets, streets):
        self.numStreets= numStreets
        self.streets = streets # list of streets

    def pathLength(self, streets):
        time = 0
        for index in range(1, len(self.streets)):
            s = self.streets[index]
            for street in streetInfo: 
                if s == street.name:
                    time += street.L
        self.time = time
        self.sparetime = simulationtime - time

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

class Intersections():
    def __init__(self, name):
        self.name = name
        self.counter = 0
        self.isgreen = False
        self.smth = 0

class commonIntersections():
    def __init__(self, name):
        self.name = name



def isgreen(numberOfIntersections):
    intersectionList = []
    for i in range(numberOfIntersections):
        a = Intersections(str(i))
        intersectionList.append(a)
        for street in range(len(streetInfo)):
            if streetInfo[street].end == i:
                a.counter += 1 
        if a.counter == 1:
            a.isgreen = True
    return intersectionList
    
file = open("a.txt")

data = file.readlines() 
intersectionList = []
carsList = []
listInfo = []

streets= 0
cars = 0
simulationtime = 0

for index in range(len(data)):
    line = data[index]
    line = line.strip("\n")
    if index == 0:
        listInfo = line.split(" ")
        simulationtime = int(listInfo[0])
        numberOfIntersections = int(listInfo[1])
        streets= int(listInfo[2])
        cars = int(listInfo[3])
        bonus = int(listInfo[4])
    if ( 1 <= index <= streets):
        intersectionList.append(line)
    if ( streets< index <= streets + cars):
        carsList.append(line)

streetInfo = streetIn(intersectionList)
carsInfo = carsIn(carsList)

timesList = []
for i in carsInfo:
    i.pathLength(i.streets)
    timesList.append(i.sparetime)

# for index in range(len(timesList)): 
#     print(timesList[index])

listOfIntersections = isgreen(numberOfIntersections)



''' issue: 
apart from the fact that we've got 4 inner loops, 
we can't seem to get the program to show number of common intersections for athens street'''


for i in carsInfo:
    print(i.streets)
    for j in i.streets:
        print(j.name)
        for n in streetInfo:
            if j == n.name:
                start = n.start
                for q in listOfIntersections:
                    if str(start) == q.name:
                        q.smth += 1


for i in listOfIntersections: #range(numberOfIntersections):
    # print(i.counter) 
    # print(i.isgreen)
    print(i.smth)


# print(streetInfo)
# for i in range(intersections):
#     print(streetInfo[i].name)

# print(carsInfo)
# for i in range(cars):
#     print(carsInfo[i].streets)

# # listInfo = (firstLine.strip("\n")).split(" ")
# print(listInfo) # DEBUGGING
# print(intersections) # DEBUGGING
# print(cars) # DEBUGGING
# print("---")
# print(intersectionList)
# print(carsList)

file.close()

print("done")