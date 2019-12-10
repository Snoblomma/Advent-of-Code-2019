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
        # print(k)
        k1 = k[0]
        k2 = k[1]
        if k1 not in d.keys():
            d[k2] = 1
        else:
            # count += copy.deepcopy(d[k1])+1
            d[k2] = copy.deepcopy(d[k1])+1

    print(d)
    for i in d.values():
        count += i
    print(count)
    # for i in d:
    #     print(i)
    return(count)


if __name__ == "__main__":
    unittest.main()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))
    n = []
    for line in file:
        n.append(line.rstrip())

    calc_orbits(n)