import unittest
import os
import copy


class TestCalcOrbit(unittest.TestCase):
    def test(self):
        instructions = ['COM)B',
                        'B)C',
                        'C)D',
                        'D)E',
                        'E)F',
                        'B)G',
                        'G)H',
                        'D)I',
                        'E)J',
                        'J)K',
                        'K)L',
                        'K)YOU',
                        'I)SAN']
        self.assertEqual(calc_orbits(instructions), 4)

def get_fisrt_common_item(x, y):
    for i in x:
        for j in y:
            if i == j:
                return i, x.index(i), y.index(i)
    return None, None, None

def calc_orbits(n):
    d = {}
    count = 0
    for item in n:
        k = item.split(')')
        d[k[1]] = k[0]

    orbit1 = []
    orbit2 = []
    point1 = 'SAN'
    while d[point1] != 'COM':
        point1 = d[point1]
        orbit1.append(point1)

    point2 = 'YOU'
    while d[point2] != 'COM':
        point2 = d[point2]
        orbit2.append(point2)

    item, loc1, loc2 = get_fisrt_common_item(orbit1, orbit2)
    return(loc1 + loc2)

if __name__ == "__main__":
    # unittest.main()
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))
    n = []
    for line in file:
        n.append(line.rstrip())

    calc_orbits(n)
