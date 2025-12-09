import re

n_dial = 100
cur_dial = 50
actual_pass = 0

# change this path to the input file
input_path = "2025/day01_input.txt"

with open(input_path, "r") as f:
    for line in f:
        direction = line[0]
        step = int(re.findall(r'\d+', line)[0])
        # print(step)
        if direction == 'L':
            cur_dial -= step
        else:
            cur_dial += step
        cur_dial %= n_dial
        print(cur_dial)
        actual_pass += 1 if cur_dial == 0 else 0

print(f"actual pass: {actual_pass}")