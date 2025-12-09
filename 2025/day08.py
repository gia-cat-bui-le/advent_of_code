# change this path to the input file
input_path = "2025/08_input.txt"


boxes_pos = []
MAX_CONNECTED_P1 = 1000

def read_file():
    global boxes_pos
    with open(input_path, "r") as f:
        for line in f:
            boxes_pos.append([int(x) for x in line.strip().split(',')])

    # print(boxes_pos)

def get_distance_boxes():
    distances = []
    for i in range(len(boxes_pos)):
        tmp_dist = []
        for j in range(len(boxes_pos)):
            tmp_dist.append((boxes_pos[i][0] - boxes_pos[j][0]) ** 2
                            + (boxes_pos[i][1] - boxes_pos[j][1]) ** 2
                            + (boxes_pos[i][2] - boxes_pos[j][2]) ** 2)
        distances.append(tmp_dist)
    return distances

def get_list_dist_boxes():
    distances_boxes = get_distance_boxes()
    list_dist_boxes = []
    for i in range(len(distances_boxes)):
        for j in range(i + 1, len(distances_boxes)):
            list_dist_boxes.append((distances_boxes[i][j], i, j))

    return list_dist_boxes

def part1():
    list_dist_boxes = sorted(get_list_dist_boxes(), key=lambda x: x[0])
    # print(list_dist_boxes)
    list_circuit = [[i] for i in range(len(boxes_pos))]
    list_belong_circuit = [i for i in range(len(boxes_pos))]

    for i in range(MAX_CONNECTED_P1):
        dist, box1, box2 = list_dist_boxes[i][0], list_dist_boxes[i][1], list_dist_boxes[i][2]
        # print(f"Processing boxes {box1} and {box2} with distance {dist}")
        if list_belong_circuit[box1] != list_belong_circuit[box2]:
            merged_circuit = list_belong_circuit[box1]
            old_circuit = list_belong_circuit[box2]
            for b in list_circuit[old_circuit]:
                list_belong_circuit[b] = merged_circuit
                list_circuit[merged_circuit].append(b)
            list_circuit[old_circuit] = []
        #     print(f"\tConnected box {box1} and box {box2}, total connected: {n_connected}")
        #     print(f"\tnew circuit: {list_circuit}")
        #     print(f"\tbelong circuit: {list_belong_circuit}")
        # else:
        #     print(f"\tBox {box1} and box {box2} are already in the same circuit")
        #     pass

    n_boxes_in_circuit = [len(circuit) for circuit in list_circuit]
    n_boxes_in_circuit.sort(reverse=True)
    # print(n_boxes_in_circuit)
    print(f"Part 1: {n_boxes_in_circuit[0] * n_boxes_in_circuit[1] * n_boxes_in_circuit[2]}")

def part2():
    list_dist_boxes = sorted(get_list_dist_boxes(), key=lambda x: x[0])
    # print(list_dist_boxes)
    list_circuit = [[i] for i in range(len(boxes_pos))]
    list_belong_circuit = [i for i in range(len(boxes_pos))]

    for dist, box1, box2 in list_dist_boxes:
        # print(f"Processing boxes {box1} and {box2} with distance {dist}")
        if list_belong_circuit[box1] != list_belong_circuit[box2]:
            merged_circuit = list_belong_circuit[box1]
            old_circuit = list_belong_circuit[box2]
            for b in list_circuit[old_circuit]:
                list_belong_circuit[b] = merged_circuit
                list_circuit[merged_circuit].append(b)
            list_circuit[old_circuit] = []
            if len(list_circuit[merged_circuit]) >= len(boxes_pos):
                ret = boxes_pos[box1][0] * boxes_pos[box2][0]
                break
        #     print(f"\tConnected box {box1} and box {box2}, total connected: {n_connected}")
        #     print(f"\tnew circuit: {list_circuit}")
        #     print(f"\tbelong circuit: {list_belong_circuit}")
        # else:
        #     print(f"\tBox {box1} and box {box2} are already in the same circuit")
        #     pass

    print(f"Part 2: {ret}")


read_file()
part1()
part2()
