class Street():
    def __init__ (self, start, end, name, length):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.length = int(length)

class Car():
    def __init__ (self, path_length, path):
        self.path_length = int(path_length)
        self.path = path
        self.trip_time = 0
    
    # Calculating the time it take for the car to finish the trip
    def get_trip_time(self, streets_list, streets_dictionary):
        for street in self.path[1 :]:                                                    # Looking for the length of each street. First street is not used because the car start at the end of it.
            self.trip_time += streets_list[streets_dictionary[street]].length
        return self.trip_time

    def visited_intersections(self, streets_list, streets_dictionary):
        self.visited_intersections = [streets_list[streets_dictionary[street_name]].end for street_name in self.path[:-1]]
        return self.visited_intersections

class Intersection():
    def __init__(self, entry_list, exit_list):
        self.entry_list = entry_list
        self.exit_list = exit_list
        self.always_green = False
        self.always_red = False

# Open and store data
def OpenFile(filename):
    
    # Opening INPUT file and saving data line by line inside the "data" variable
    with open(filename) as file:
        data = file.readlines()
    
    street_lines = []
    car_lines = []
    
    # Processing the lines
    for line_index in range(len(data)):
        data[line_index] = data[line_index].strip("\n")
        if line_index == 0:
            info_line = data[line_index].split(" ")
            simulation_time = int(info_line[0])
            number_of_intersections = int(info_line[1])
            number_of_streets = int(info_line[2])
            number_of_cars = int(info_line[3])
            finish_points = int(info_line[4])
        if 1 <= line_index <= number_of_streets:
            street_lines.append(data[line_index]) 
        if number_of_streets < line_index <= (number_of_streets + number_of_cars):
            car_lines.append(data[line_index])
    return info_line, street_lines, car_lines, simulation_time, number_of_intersections, number_of_streets, number_of_cars, finish_points

# Create Street instances for each line containing street info
def CreateStreetInstances():
    streets_dictionary = {}
    streets_list = []
    for line_index in range(len(street_lines)):
        line_info = street_lines[line_index].split(" ")
        new_street = Street(line_info[0], line_info[1], line_info[2], line_info[3])
        streets_list.append(new_street)
        streets_dictionary[line_info[2]] = line_index
    return streets_list, streets_dictionary

# Create Car instances for each line containing car info
def CreateCarInstances():
    path = []
    cars_list = []
    for line_index in range(len(car_lines)):
        line_info = car_lines[line_index].split(" ")
        path_length = line_info[0]
        path = line_info[1 :]
        new_car = Car(path_length, path)
        cars_list.append(new_car)
        cars_list[line_index].get_trip_time(streets_list, streets_dictionary)
        cars_list[line_index].visited_intersections(streets_list, streets_dictionary)
    return cars_list

def CreateIntersectionInstances():
    intersections_list = []
    for intersection in range(number_of_intersections):
        entry_list = []
        exit_list = []
        for street in streets_list:
            if intersection == street.end:
                entry_list.append(street.name)
            if intersection == street.start:
                exit_list.append(street.name)
        new_intersection = Intersection(entry_list, exit_list)
        intersections_list.append(new_intersection)
        if intersection in intersections_not_used:
            new_intersection.always_red = True
        if len(new_intersection.entry_list) <= 1 and (intersection not in intersections_not_used): 
            new_intersection.always_green = True
    return intersections_list

def UsedOrNot(cars_list):
    intersections_used = []
    intersections_not_used = []
    for car in cars_list:
        for intersection in car.visited_intersections:
            if intersection not in intersections_used:
                intersections_used.append(intersection)
    for intersection in range(number_of_intersections):
        if intersection not in intersections_used:
            intersections_not_used.append(intersection)
    return intersections_used, intersections_not_used

info_line, street_lines, car_lines, simulation_time, number_of_intersections, number_of_streets, number_of_cars, finish_points = OpenFile("b.txt")
streets_list, streets_dictionary = CreateStreetInstances()
cars_list = CreateCarInstances()
intersections_used, intersections_not_used = UsedOrNot(cars_list)
intersections_list = CreateIntersectionInstances()
#print(sorted(intersections_used))

for i in range(number_of_intersections):
    if intersections_list[i].always_green:
        print("Intersection " + str(i) +" is always_green")
    elif intersections_list[i].always_red:
        print("Intersection " + str(i) +" is always_red")
    else:
        print("Intersection " + str(i) +" has a schedule")
