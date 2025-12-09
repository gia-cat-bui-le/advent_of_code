# change this path to the input file
input_path = "2025/04_input.txt"
diagram = []
max_rolls = 4

def part1():
    count_spot = 0
    for i, row in enumerate(diagram):
        for j, val in enumerate(row):
            if val == ".":
                continue
            count_roll = 0
            for r in range(max(0, i-1), min(len(diagram), i+2)):
                for c in range(max(0, j-1), min(len(row), j+2)):
                    if diagram[r][c] == "@" or diagram[r][c] == "x":
                        count_roll += 1
                    if count_roll > max_rolls:
                        break
                if count_roll > max_rolls:
                    break
            if count_roll <= max_rolls:
                diagram[i][j] = "x"
                count_spot += 1
                
    return count_spot

def part2():
    count_remove_rolls = 0
    
    while True:
        n_rolls_removed = part1()
        if n_rolls_removed == 0:
            break
        count_remove_rolls += n_rolls_removed
        # print(f"After removing {n_rolls_removed} rolls:")
        # for row in diagram:
        #     print(row)
        for i, row in enumerate(diagram):
            for j, val in enumerate(row):
                if val == "x":
                    diagram[i][j] = "."

    return count_remove_rolls

with open(input_path, "r") as f:
    for line in f:
        diagram.append(list(line.rstrip("\n")))


print("Part 1:", part1())
print("Part 2:", part2())
# print(f"Part 1: new diagram: {diagram}")