import os
import unittest


class TestPasswordDecode(unittest.TestCase):
    def test(self):
        line = '123456789012'
        self.assertEqual(get_password(line, 3, 2), 1)


def get_password(encoded, width, height):
    area = width*height
    layers = []
    min_0 = area
    count_1 = 0
    count_2 = 0
    for i in range(0, len(encoded), area):
        layer = encoded[i:i+area]
        count_0 = layer.count('0')
        if count_0 < min_0:
            min_0 = count_0
            count_1 = layer.count('1')
            count_2 = layer.count('2')
        layers.append(layer)

    return(count_1*count_2)


if __name__ == "__main__":
    # unittest.main()
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))
    encoded = ''
    for line in file:
        encoded += line.rstrip()

    password = get_password(encoded, 25, 6)
