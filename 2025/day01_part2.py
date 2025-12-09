n_dial = 100
cur_dial = 50
actual_pass = 0

# change this path to the input file
input_path = "2025/day01_input.txt"

with open(input_path, "r") as f:
    for line in f:
        direction = line[0]
        step = int(line[1:])
        for _ in range(step):
            if direction == 'L':
                cur_dial -= 1
            else:
                cur_dial += 1
            cur_dial %= n_dial
            if cur_dial == 0:
                print(f"pass at: {line}")
                actual_pass += 1

print(f"actual pass: {actual_pass}")