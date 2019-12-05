import copy

output = 19690720

def count(n):
    for i in range(0, len(n), 4):
        k = str(n[i])
        if k == '1':
            n[n[i+3]] = n[n[i+1]] + n[n[i+2]]
        elif k == '2':
            n[n[i+3]] = n[n[i+1]] * n[n[i+2]]
        elif k == '99':
            break
        else:
            break
    return n[0]

def calc(n):
    for i in range(100):
        for j in range(100):
            k = copy.deepcopy(n)
            k[1] = i
            k[2] = j
            if count(k) == output:
                print('Yay!', i, j)
                return

if __name__ == "__main__":
    calc([1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,10,23,27,2,27,13,31,1,10,31,35,1,35,9,39,2,39,13,43,1,43,5,47,1,47,6,51,2,6,51,55,1,5,55,59,2,9,59,63,2,6,63,67,1,13,67,71,1,9,71,75,2,13,75,79,1,79,10,83,2,83,9,87,1,5,87,91,2,91,6,95,2,13,95,99,1,99,5,103,1,103,2,107,1,107,10,0,99,2,0,14,0])