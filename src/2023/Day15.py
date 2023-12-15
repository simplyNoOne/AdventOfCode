def day15_base():
    with open('inputs/day15.txt') as f:
        sections = f.readline().split("\n")[0].split(',')
    sum_h = 0
    hash_mult = 17
    hash_bound = 256
    for s in sections:
        value = 0
        for c in s:
            value += ord(c)
            value *= hash_mult
            value = value % hash_bound
        sum_h += value
    return sum_h


def day15_extra():
    with open('inputs/day15.txt') as f:
        sections = f.readline().split("\n")[0].split(',')
    # sections = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(',')
    focusing_power = 0
    hash_mult = 17
    hash_bound = 256
    boxes = []
    for _ in range(hash_bound):
        boxes.append([])

    for s in sections:
        value = 0
        add = False
        if len(s.split('=')) == 2:
            s = s.split('=')
            add = True
        else:
            s = s.split('-')
        for c in s[0]:
            value += ord(c)
            value *= hash_mult
            value = value % hash_bound
        if add:
            found = False
            for idx, pair in enumerate(boxes[value]):
                if pair[0] == s[0]:
                    boxes[value][idx][1] = int(s[1])
                    found = True
                    break
            if not found:
                boxes[value].append([s[0], int(s[1])])
        else:
            boxes[value] = [item for item in boxes[value] if item[0] != s[0]]

    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focusing_power += ((1 + i) * (j + 1) * lens[1])
    return focusing_power

