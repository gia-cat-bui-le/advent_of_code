# change this path to the input file
input_path = "2025/07_input.txt"


diagram = []

def read_file():
    global diagram
    with open(input_path, "r") as f:
        for line in f:
            diagram.append(list(line.strip()))

    # print(diagram)

def part1():
    read_file()
    count_split = 0
    for i in range(1, len(diagram)):
        # print(f"Processing row {i}")
        for j, char in enumerate(diagram[i]):
            if char == '.' and (diagram[i-1][j] == '|' or diagram[i-1][j] == 'S'):
                diagram[i][j] = '|'
            elif char == '^' and (diagram[i-1][j] == '|' or diagram[i-1][j] == 'S'):
                count_split += 1
                if diagram[i][j-1] == '.':
                    diagram[i][j-1] = '|'
                if diagram[i][j+1] == '.':
                    diagram[i][j+1] = '|'
        # print(f"After row {i}, count split: {count_split}, diagram is:")
        # for row in diagram: 
        #     print(''.join(row))

    print(f"Part 1: {count_split}")

def part2():
    global diagram
    read_file()
    n_timeline = [[0] * len(diagram[0]) for _ in range(len(diagram))]

    def get_n_timeline(r, c):
        nonlocal n_timeline
        if r >= len(diagram) - 1:
            return 1
        print(f"At row {r}, col {c}")
        # print(n_timeline)
        if n_timeline[r][c] != 0:
            return n_timeline[r][c]
        
        n_tl = 0
        if diagram[r + 1][c] == '.':
            n_tl += get_n_timeline(r + 1, c)
        if diagram[r + 1][c] == '^':
            if diagram[r + 1][c - 1] == '.':
                n_tl += get_n_timeline(r + 1, c - 1)
            if diagram[r + 1][c + 1] == '.':
                n_tl += get_n_timeline(r + 1, c + 1)

        n_timeline[r][c] = n_tl
        return n_tl
    
    count_timeline = get_n_timeline(0, diagram[0].index('S'))
    print(f"Part 2: {count_timeline}")

# part1()
part2()
