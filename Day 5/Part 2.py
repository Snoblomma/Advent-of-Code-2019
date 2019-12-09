import unittest


class TestTEST(unittest.TestCase):
    def test(self):
        instructions = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(calc(instructions), [
                         3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8])

    def test2(self):
        instructions = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        self.assertEqual(calc(instructions), [
                         3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8])

    def test3(self):
        instructions = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        self.assertEqual(calc(instructions), [3, 3, 1108, -1, 8, 3, 4, 3, 99])

    def test4(self):
        instructions = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        self.assertEqual(calc(instructions), [3, 3, 1107, -1, 8, 3, 4, 3, 99])

    def test5(self):
        instructions = [3, 12, 6, 12, 15, 1,
                        13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        self.assertEqual(calc(instructions), [
                         3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9])

    def test6(self):
        instructions = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        self.assertEqual(calc(instructions), [
                         3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])

    def test7(self):
        instructions = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                        1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                        999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        self.assertEqual(calc(instructions), [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                                              1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                                              999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99])


def add_to_length(a):
    while len(a) < 5:
        a = '0' + a
    return a


def calc(n):
    position = 0
    print(n)

    def get_parameter(parameter, mode):
        if mode == '0':
            return int(n[parameter])
        elif mode == '1':
            return int(parameter)

    while True:
        step = 4
        k = str(n[position])
        print('k', k)
        if k == '1':
            n[n[position+3]] = n[n[position+1]] + n[n[position+2]]
        elif k == '2':
            n[n[position+3]] = n[n[position+1]] * n[n[position+2]]
        elif k == '3':
            n[n[position+1]] = int(input())
            step = 2
        elif k == '4':
            print('OUTPUT')
            print(n[n[position+1]])
            step = 2
        elif k == '5':
            if int(n[position+1]) != 0:
                # n[position] = n[position+2]
                position = n[position+2]
                step = 0
            else:
                step = 3
        elif k == '6':
            if int(n[position+1]) == 0:
                # n[position] = n[position+2]
                position = n[position+2]
                print('position', position)
                step = 0
            else:
                step = 3
            # step = 3
        elif k == '7':
            if int(n[position+1]) < int(n[position+2]):
                n[n[position+3]] = 1
            else:
                n[n[position+3]] = 0

        elif k == '8':
            if int(n[position+1]) == int(n[position+2]):
                n[n[position+3]] = 1
            else:
                n[n[position+3]] = 0

        elif k == '99':
            break
        else:
            opcode = k[-2:]
            modes1 = add_to_length(k)
            modes = modes1[:3]

            print('opcode', opcode)

            if int(opcode) == 1:
                p1 = get_parameter(n[position+1], modes[2])
                p2 = get_parameter(n[position+2], modes[1])
                n[n[position+3]] = p1 + p2
            elif int(opcode) == 2:
                p1 = get_parameter(n[position+1], modes[2])
                p2 = get_parameter(n[position+2], modes[1])
                n[n[position+3]] = p1 * p2
            elif int(opcode) == 3:
                p1 = get_parameter(n[position+1], modes[2])
                n[p1] = int(input())
                step = 2
            elif int(opcode) == 4:
                p1 = get_parameter(n[position+1], modes[2])
                print('OUTPUT')
                print(p1)
                step = 2
            elif int(opcode) == 5:
                p1 = get_parameter(n[position+1], modes[2])
                p2 = get_parameter(n[position+2], modes[1])
                if int(p1) != 0:
                    position = p2
                    step = 0
                else:
                    step = 3
            elif int(opcode) == 6:
                p1 = get_parameter(n[position+1], modes[2])
                p2 = get_parameter(n[position+2], modes[1])
                if int(p1) == 0:
                    # n[position] = n[position+2]
                    position = p2
                    step = 0
                else:
                    step = 3
            elif int(opcode) == 7:
                p1 = get_parameter(n[position+1], modes[2])
                p2 = get_parameter(n[position+2], modes[1])
                if int(p1) < int(p2):
                    n[n[position+3]] = 1
                else:
                    n[n[position+3]] = 0
            elif int(opcode) == 8:
                p1 = get_parameter(n[position+1], modes[2])
                p2 = get_parameter(n[position+2], modes[1])
                if int(p1) == int(p2):
                    n[n[position+3]] = 1
                else:
                    n[n[position+3]] = 0

        position += step
        # print(n)

    return(n)


if __name__ == "__main__":
    # unittest.main()
    calc([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])