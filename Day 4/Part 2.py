regex_alternating_repetitive_digit_pair = r"(\d)(?=\1)"

import re

def solve(start, end):
    count = 0

    for i in range(start, end+1):
        string = str(i)
        all_matching = re.findall(regex_alternating_repetitive_digit_pair, string)
        if len(all_matching) > 0:
            if ''.join(sorted(string)) == string:
                s = set(all_matching)  
                for item in s:
                    if string.count(item) == 2:
                        count += 1
                        break
                    
    print(count)


if __name__ == "__main__":
    solve(172851, 675869)