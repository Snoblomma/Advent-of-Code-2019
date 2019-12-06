import copy

def up(steps, current_location, visited_locations):
    for i in range(steps):
        current_location[1] += 1
        visited_locations.append(copy.deepcopy(current_location))

def right(steps, current_location, visited_locations):
    for i in range(steps):
        current_location[0] += 1
        visited_locations.append(copy.deepcopy(current_location))

def down(steps, current_location, visited_locations):
    for i in range(steps):
        current_location[1] -= 1      
        visited_locations.append(copy.deepcopy(current_location))

def left(steps, current_location, visited_locations):
    for i in range(steps):
        current_location[0] -= 1
        visited_locations.append(copy.deepcopy(current_location))

options = {'U': up, 'R': right, 'D': down, 'L': left}

def move(direction, steps, current_location, visited_locations):
    options[direction](steps, current_location, visited_locations)

def process(n):
    visited_locations = []
    current_location = [0, 0]
    for item in n:
        move(item[0], int(item[1:]), current_location, visited_locations)
    return visited_locations
   

if __name__ == "__main__":
    wire1 = process(list(input().split(',')))
    wire2 = process(list(input().split(',')))

    repeated_locations = []
    for ele in wire1:
        if ele in wire2 and ele not in repeated_locations:
            repeated_locations.append(ele)

    lengths = []
    for item in repeated_locations:
        lengths.append(abs(item[0]) + abs(item[1]))

    print(min(lengths))