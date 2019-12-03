import os
import math

sum_of_all = 0

def calc(n):
    global sum_of_all
    sum_of_all += math.floor(n/3) - 2

if __name__ == "__main__":
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'part1.txt'))
    for line in file: 
        calc(int(line))

    print(sum_of_all)