import re

# change this path to the input file
input_path = "2025/02_input.txt"
list_id = []

def is_ID_invalid_part1(id):
    id_str = str(id)
    len_str = len(id_str)
    if len_str % 2 != 0:
        return False
    if id_str[:(len_str//2)] == id_str[(len_str//2):]:
        print(f"invalid id {id}, {id_str[:(len_str//2)]}, {id_str[(len_str//2):]}")
    return id_str[:(len_str//2)] == id_str[(len_str//2):]

def is_ID_invalid_part2(id):
    id_str = str(id)
    len_id = len(id_str)
    for len_sub_str in range(1, len_id//2 + 1):
        if len_id % len_sub_str != 0:
            continue
        ref_str = id_str[:len_sub_str]
        is_invalid = True
        for start in range(len_sub_str, len_id, len_sub_str):
            end = start + len_sub_str
            chk_sub_str = id_str[start:end]
            if chk_sub_str != ref_str:
                is_invalid = False
                break

        if is_invalid:
            print(f"invalid id: {id}")
            return True
    return False

def day2(list_id):
    sum_invalid_id = 0
    for idx in range(0, len(list_id), 2):
        for id in range(int(list_id[idx]), int(list_id[idx + 1]) + 1):
            # if is_ID_invalid_part1(id):
            #     sum_invalid_id += id
            if is_ID_invalid_part2(id):
                sum_invalid_id += id

    return sum_invalid_id


with open(input_path, "r") as f:
    for line in f:
        list_id.extend(re.findall(r'\d+', line))
    print(list_id)

print(day2(list_id))