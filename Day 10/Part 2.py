import os
import unittest
import copy
import math


class TestAsteroidDetector(unittest.TestCase):
    def test(self):
        lines = ['.#..#',
                 '.....',
                 '#####',
                 '....#',
                 '...##']

        asteroids, location = get_location(lines)
        self.assertEqual(asteroids, 8)
        self.assertEqual(location, [3, 4])

    def test1(self):
        lines = ['......#.#.',
                 '#..#.#....',
                 '..#######.'
                 '.#.#.###..',
                 '.#..#.....',
                 '..#....#.#',
                 '#..#....#.',
                 '.##.#..###',
                 '##...#..#.',
                 '.#....####']

        asteroids, location = get_location(lines)
        self.assertEqual(asteroids, 33)
        self.assertEqual(location, [5, 8])

    def test2(self):
        lines = ['#.#...#.#.',
                 '.###....#.',
                 '.#....#...',
                 '##.#.#.#.#',
                 '....#.#.#.',
                 '.##..###.#',
                 '..#...##..',
                 '..##....##',
                 '......#...',
                 '.####.###.']

        asteroids, location = get_location(lines)
        self.assertEqual(asteroids, 35)
        self.assertEqual(location, [1, 2])

    def test3(self):
        lines = ['.#..#..###',
                 '####.###.#',
                 '....###.#.',
                 '..###.##.#',
                 '##.##.#.#.',
                 '....###..#',
                 '..#.#..#.#',
                 '#..#.#.###',
                 '.##...##.#',
                 '.....#.#..']

        asteroids, location = get_location(lines)
        self.assertEqual(asteroids, 41)
        self.assertEqual(location, [6, 3])

    def test4(self):
        lines = ['.#..##.###...#######',
                 '##.############..##.',
                 '.#.######.########.#',
                 '.###.#######.####.#.',
                 '#####.##.#.##.###.##',
                 '..#####..#.#########',
                 '####################',
                 '#.####....###.#.#.##',
                 '##.#################',
                 '#####.##.###..####..',
                 '..######..##.#######',
                 '####.##.####...##..#',
                 '.#####..#.######.###',
                 '##...#.##########...',
                 '#.##########.#######',
                 '.####.#.###.###.#.##',
                 '....##.##.###..#####',
                 '.#.#.###########.###',
                 '#.#.#.#####.####.###',
                 '###.##.####.##.#..##']

        asteroids, location = get_location(lines)
        self.assertEqual(asteroids, 210)
        self.assertEqual(location, [11, 13])


def get_asteroid_locations(lines):
    locations = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                locations.append([j, i])
    return locations


def present(x, y, location_vectors):
    for location_vector in location_vectors:
        if location_vector[0]/x == location_vector[1]/y and location_vector[0] != x and location_vector[1] != y:
            if are_opposites(location_vector[0], x) == False and are_opposites(location_vector[1], y) == False:
                return True
    return False


def are_opposites(a, b):
    return a*b < 0


def in_array(a, array):
    for item in array:
        if item[0] == a[0] and item[1] == a[1]:
            return True
    return False


def eliminate(location_vectors):
    new_vectors = []
    same_vectors = []
    for vector in location_vectors:

        x = vector[0]
        y = vector[1]
        if x != 0 and y != 0:
            if present(x, y, new_vectors) == True:
                if in_array([x, y], same_vectors) == False:
                    same_vectors.append([x, y])
        new_vectors.append([x, y])

    new_same_vectors = []
    for i in same_vectors:
        if in_array(i, new_vectors) == True:
            new_same_vectors.append(i)
        elif in_array(i, new_vectors) == False:
            if present(i[0], i[1], new_vectors) == False:
                new_same_vectors.append(i)

    return new_vectors, new_same_vectors


def get_location(lines):
    asteroids = 0

    locations = get_asteroid_locations(lines)
    locations_asteroids = []
    points = []

    vectors = []

    for i in range(len(locations)):
        location = locations[i]
        location_vectors = []

        x_less = False
        x_more = False
        y_less = False
        y_more = False

        for j in range(len(locations)):
            if i != j:
                current = locations[j]
                x = location[0]-current[0]
                y = location[1]-current[1]

                if x != 0 and y != 0:
                    location_vectors.append([x, y])
                else:
                    if x == 0 and y > 0 and x_more == False:
                        location_vectors.append([x, y])
                        x_more = True
                    elif x == 0 and y < 0 and x_less == False:
                        location_vectors.append([x, y])
                        x_less = True
                    elif y == 0 and x > 0 and y_more == False:
                        location_vectors.append([x, y])
                        y_more = True
                    elif y == 0 and x < 0 and y_less == False:
                        location_vectors.append([x, y])
                        y_less = True

        location_vectors, same_vectors = eliminate(location_vectors)
        vectors.append(location_vectors)
        locations_asteroids.append(len(location_vectors)-len(same_vectors))
        points.append(location)

    asteroids = max(locations_asteroids)
    return asteroids, points[locations_asteroids.index(asteroids)]


def get_vector(start, end):
    print(start, end)
    return [end[0] - start[0], end[1] - start[1]]


def get_angle(v1, v2):
    mag1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag2 = math.sqrt(v2[0]**2 + v2[1]**2)
    cos_a = (v1[0] * v2[0] + v1[1] * v2[1]) / (mag1 * mag2)
    return math.degrees(math.acos(cos_a))


def which_asteroid(lines, start_location, n):
    locations = get_asteroid_locations(lines)
    angles = []
    main_vector = get_vector(start_location, [start_location[0], 0])
    print("MAIN VECTOR")
    print(main_vector)

    for location in locations:
        if start_location[0] != location[0] and start_location[1] != location[1]:
            print('VECTOR')
            vector = get_vector(start_location, location)
            print(vector)
            print('COS')
            print(get_angle(main_vector, vector))


if __name__ == "__main__":
    # unittest.main()
    # __location__ = os.path.realpath(os.path.join(
    #     os.getcwd(), os.path.dirname(__file__)))
    # file = open(os.path.join(__location__, 'input.txt'))

    # lines = []
    # for line in file:
    #     lines.append(line.rstrip())

    lines = ['.#..#',
             '.....',
             '#####',
             '....#',
             '...##']

    asteroids, start_location = get_location(lines)
    print(asteroids)
    n = 10
    nth_asteroid = which_asteroid(lines, start_location, n)
