import os
import unittest


class TestGetMessage(unittest.TestCase):
    def test(self):
        line = '0222112222120000'
        self.assertEqual(get_message(line, 2, 2), '0110')


def get_message(encoded, width, height):
    area = width*height
    layers = []

    for i in range(0, len(encoded), area):
        layer = encoded[i:i+area]
        layers.append(layer)

    final_layer = ''

    for i in range(area):
        for j in range(len(layers)):
            pixel = layers[j][i]
            if pixel != '2':
                final_layer += pixel
                break

    print('MESSAGE')

    for i in range(0, len(final_layer), width):
        row = final_layer[i:i+width]
        print(row)

    return(final_layer)


if __name__ == "__main__":
    # unittest.main()
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'input.txt'))
    encoded = ''
    for line in file:
        encoded += line.rstrip()

    password = get_message(encoded, 25, 6)
