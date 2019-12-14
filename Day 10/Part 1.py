import os
import unittest


class TestAsteroidDetector(unittest.TestCase):
    def test(self):
        lines = ['.#..#',
                 '.....',
                 '#####',
                 '....#',
                 '...##']
        self.assertEqual(get_location(lines), 8)

    # def test1(self):
    #     lines = ['......#.#.',
    #              '#..#.#....',
    #              '..#######.'
    #              '.#.#.###..',
    #              '.#..#.....',
    #              '..#....#.#',
    #              '#..#....#.',
    #              '.##.#..###',
    #              '##...#..#.',
    #              '.#....####']
    #     self.assertEqual(get_location(lines), 33)

    # def test2(self):
    #     lines = ['#.#...#.#.',
    #              '.###....#.',
    #              '.#....#...',
    #              '##.#.#.#.#',
    #              '....#.#.#.',
    #              '.##..###.#',
    #              '..#...##..',
    #              '..##....##',
    #              '......#...',
    #              '.####.###.']
    #     self.assertEqual(get_location(lines), 35)

    # def test3(self):
    #     lines = ['.#..#..###',
    #              '####.###.#',
    #              '....###.#.',
    #              '..###.##.#',
    #              '##.##.#.#.',
    #              '....###..#',
    #              '..#.#..#.#',
    #              '#..#.#.###',
    #              '.##...##.#',
    #              '.....#.#..']

    #     self.assertEqual(get_location(lines), 41)

    # def test4(self):
    #     lines = ['.#..##.###...#######',
    #              '##.############..##.',
    #              '.#.######.########.#',
    #              '.###.#######.####.#.',
    #              '#####.##.#.##.###.##',
    #              '..#####..#.#########',
    #              '####################',
    #              '#.####....###.#.#.##',
    #              '##.#################',
    #              '#####.##.###..####..',
    #              '..######..##.#######',
    #              '####.##.####...##..#',
    #              '.#####..#.######.###',
    #              '##...#.##########...',
    #              '#.##########.#######',
    #              '.####.#.###.###.#.##',
    #              '....##.##.###..#####',
    #              '.#.#.###########.###',
    #              '#.#.#.#####.####.###',
    #              '###.##.####.##.#..##']
    #     self.assertEqual(get_location(lines), 210)


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
                print('ARE SAME')
                print(x, y, location_vector[0], location_vector[1])
                return True
            else:
                print('ARE OPPOSITES')
                print(x, y, location_vector[0], location_vector[1])

    return False

def are_opposites(a, b):
    return a*b < 0

def eliminate(location_vectors):

    print('OLD VECTOR')
    print(location_vectors)
    new_vectors = []
    same_vectors = []
    for vector in location_vectors:
        x = vector[0]
        y = vector[0]
        if x != 0 and y != 0:
            if present(x, y, new_vectors) == True:
                if [x, y] not in same_vectors:
                    same_vectors.append([x, y])
            new_vectors.append(vector)

    # print('NEW VECTOR')
    # print(new_vectors)
    # print('Same VECTOR')
    print('Checking same vecors')
    new_same_vectors = []
    for i in same_vectors:
        # if i in location_vectors:
        prest = present(i[0], i[1], location_vectors)
        print('PRESENT?', i[0], i[1], prest)
        # print(present(i[0], i[1], location_vectors))
        if prest == False:
            if i not in location_vectors:
                new_same_vectors.append(i)

    return location_vectors, new_same_vectors


def get_location(lines):
    asteroids = 0

    locations = get_asteroid_locations(lines)
    locations_asteroids = []
    print('LOCATIONS')
    print(locations)

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
                    # if present(x, y, location_vectors) == False:
                    location_vectors.append([x, y])
                else:
                    # location_vectors.append([x, y])
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
        print('Current vector:', str(len(location_vectors)), len(same_vectors), str(location_vectors), 'same verctors: ', same_vectors)
        vectors.append(location_vectors)

    # print('VECTORS')
    # for vector in vectors:
    #     print('Current vector:', str(len(vector)), str(vector))
    return(asteroids)


if __name__ == "__main__":
    unittest.main()
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))

    lines = []
    for line in file:
        lines.append(line.rstrip())

    asteroids = get_location(lines)
    print(asteroids)
