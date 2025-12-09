# change this path to the input file
input_path = "2025/05_input.txt"

ranges = []
food_id = []

def part1():
    fresh_ingr = 0
    for fid in food_id:
        for left, right in ranges:
            if left <= fid <= right:
                fresh_ingr += 1
                break
    print(f"Part 1: {fresh_ingr}")

def part2():
    merged_ranges = sorted(ranges, key=lambda x: x[0])
    # print(f"Sorted ranges: {merged_ranges}")
    # merge ranges
    i = 0
    while i < len(merged_ranges) - 1:
        left1, right1 = merged_ranges[i]
        left2, right2 = merged_ranges[i + 1]
        if right1 + 1 >= left2:
            merged_ranges[i] = (left1, max(right1, right2))
            del merged_ranges[i + 1]
        else:
            i += 1
    # print(f"Merged ranges: {merged_ranges}")
    # count total number of fresh ingredients
    total_fresh = 0
    for left, right in merged_ranges:
        total_fresh += right - left + 1
    print(f"Part 2: {total_fresh}")

def read_file():
    with open(input_path, "r") as f:
        reading_ranges = True
        for line in f:
            # read ranges
            if reading_ranges:
                if line.strip() == "":
                    reading_ranges = False
                    continue
                parts = line.strip().split("-")
                ranges.append((int(parts[0]), int(parts[1])))
            else:
                food_id.append(int(line.strip()))

read_file()
part1()
part2()
