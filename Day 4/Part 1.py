regex_alternating_repetitive_digit_pair = r"(\d)(?=\1)"

import re

def solve(start, end):
    count = 0

    for i in range(start, end+1):
        string = str(i)
        if len(re.findall(regex_alternating_repetitive_digit_pair, string)) > 0:
            if ''.join(sorted(string)) == string:
                count += 1
    print(count)


if __name__ == "__main__":
    solve(172851, 675869)