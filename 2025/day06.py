# change this path to the input file
input_path = "2025/06_input.txt"


def part1():
    worksheet = []
    def read_file():
        with open(input_path, "r") as f:
            for line in f:
                worksheet.append(line.strip().split())
    read_file()
    grand_total = 0
    for col in range(len(worksheet[0])):
        col_values = list()
        for row in range(len(worksheet)):
            if row == len(worksheet) - 1:
                if worksheet[row][col] == '*':
                    answer = 1
                    for val in col_values:
                        answer *= val
                    grand_total += answer
                elif worksheet[row][col] == '+':
                    grand_total += sum(col_values)
            else:
                col_values.append(int(worksheet[row][col]))
    print(f"Part 1: {grand_total}")

def part2():
    worksheet = []
    def read_file():
        with open(input_path, "r") as f:
            for line in f:
                worksheet.append(line.strip("\n"))

    read_file()    
    grand_total = 0
    values = list()
    skip = False
    for col in range(len(worksheet[0]) - 1, -1, -1):
        if skip:
            skip = False
            continue
        col_val = 0
        for row in range(len(worksheet)):
            if row == len(worksheet) - 1:
                values.append(col_val)
                # input(f"Add new value: {col_val}")
                if worksheet[row][col] == '*':
                    answer = 1
                    for val in values:
                        answer *= val
                    grand_total += answer
                    # input(f"Values in columns: {values}, multiplied to get {answer}")
                    values = list()
                    skip = True
                elif worksheet[row][col] == '+':
                    grand_total += sum(values)
                    # input(f"Values in columns: {values}, summed to get {sum(values)}")
                    values = list()
                    skip = True
            elif worksheet[row][col] != ' ':
                col_val = col_val * 10 + int(worksheet[row][col])
    print(f"Part 2: {grand_total}")
    
part1()
part2()
