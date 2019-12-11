import unittest
import os
import copy

class TestCalcOrbit(unittest.TestCase):
    def test(self):
        instructions = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F',
                        'B)G',  'G)H', 'D)I',  'E)J', 'J)K', 'K)L']
        self.assertEqual(calc_orbits(instructions), 42)


def calc_orbits(n):
    d = {}
    count = 0
    for item in n:
        k = item.split(')')
        d[k[1]] = k[0]
    
    for item in d.keys():
        k = item
        temp = 1
        while d[k] != 'COM':
            k = d[k]
            temp +=1
        count += temp

    return(count)


if __name__ == "__main__":
    # unittest.main()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))
    n = []
    for line in file:
        n.append(line.rstrip())

    calc_orbits(n)