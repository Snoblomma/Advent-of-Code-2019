import os
import math

sum_of_all = 0

def calc(n):
    if n==0:
        return
    else:
        global sum_of_all
        k = math.floor(n/3) - 2
        n = k if k > 0 else 0
        sum_of_all += n
        calc(n)

if __name__ == "__main__":
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'part2.txt'))
    for line in file: 
        calc(int(line))
        
    print(sum_of_all)