import os
import unittest
import copy


class TestAsteroidDetector(unittest.TestCase):
    def test(self):
        lines = ['.#..#',
                 '.....',
                 '#####',
                 '....#',
                 '...##']
        self.assertEqual(get_location(lines), 8)

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
        self.assertEqual(get_location(lines), 33)

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
        self.assertEqual(get_location(lines), 35)

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

        self.assertEqual(get_location(lines), 41)

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
        self.assertEqual(get_location(lines), 210)


def get_asteroid_locations(lines):
    locations = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                locations.append([i, j])
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

    asteroids = max(locations_asteroids)
    return(asteroids)


if __name__ == "__main__":
    # unittest.main()
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))

    lines = []
    for line in file:
        lines.append(line.rstrip())

    asteroids = get_location(lines)
    print(asteroids)
