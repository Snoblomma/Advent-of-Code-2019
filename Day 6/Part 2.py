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
        self.assertEqual(calc_orbits(instructions), 42)


def calc_orbits(n):
    d = {}
    count = 0
    for item in n:
        k = item.split(')')
        d[k[1]] = k[0]

    k2 = []
    k3 = []
    k11 = 'SAN'
    while d[k11] != 'COM':
        k11 = d[k11]
        k2.append(k11)

    k21 = 'YOU'
    while d[k21] != 'COM':
        k21 = d[k21]
        k3.append(k21)

    print(k2)
    print(k3)

    return(count)


if __name__ == "__main__":
    unittest.main()
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))
    n = []
    for line in file:
        n.append(line.rstrip())

    calc_orbits(n)
