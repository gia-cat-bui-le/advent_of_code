# change this path to the input file
input_path = "2025/03_input.txt"

def find_max_bank_jolts_with_n_batteries(bank, n):
    if n == 1:
        list_max_jolts = [0] * len(bank)
        list_max_jolts[-1] = bank[-1]
        for i in range(len(bank) - 2, -1, -1):
            list_max_jolts[i] = max(list_max_jolts[i + 1], bank[i])
        return list_max_jolts
    
    list_max_jolts_n_1 = find_max_bank_jolts_with_n_batteries(bank, n - 1)
    list_max_jolts = [0] * len(bank)
    for i in range(len(bank) - n, -1, -1):
        list_max_jolts[i] = max(bank[i] * 10 ** (n - 1) + list_max_jolts_n_1[i + 1], list_max_jolts[i + 1])

    return list_max_jolts
    

def part1():
    joltage = 0
    with open(input_path, "r") as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            bank_jolts = find_max_bank_jolts_with_n_batteries(bank, 2)
            # print(f"bank:       {bank}")
            # print(f"bank jolts: {bank_jolts}, max: {max(bank_jolts)}")
            joltage += max(bank_jolts)

    return joltage

def part2():
    joltage = 0
    with open(input_path, "r") as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            bank_jolts = find_max_bank_jolts_with_n_batteries(bank, 12)
            # print(f"bank:       {bank}")
            # print(f"bank jolts: {bank_jolts}, max: {max(bank_jolts)}")
            joltage += max(bank_jolts)

    return joltage

print(f"part 1: {part1()}")
print(f"part 2: {part2()}")