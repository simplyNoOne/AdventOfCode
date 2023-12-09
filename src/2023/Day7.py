
def make_nested():
    nested = []
    dimension_size = 13

    for _ in range(dimension_size):
        level_1 = []
        for _ in range(dimension_size):
            level_2 = []
            for _ in range(dimension_size):
                level_3 = []
                for _ in range(dimension_size):
                    level_4 = [[] for _ in range(dimension_size)]
                    level_3.append(level_4)
                level_2.append(level_3)
            level_1.append(level_2)
        nested.append(level_1)
    return nested


def day7_base():
    with open('inputs/day7.txt') as f:
        hands = [[h[: 5], int(h[6:])] for h in f.read().split("\n") if h != ""]
    print(hands)

    h5oak = make_nested()
    h4oak = make_nested()
    hfh = make_nested()
    h3oak = make_nested()
    h2p = make_nested()
    h1p = make_nested()
    hhc = make_nested()
    d = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

    def emplace(hand_bid):
        cont = h5oak
        if unique == 5:
            cont = hhc
        if unique == 4:
            cont = h1p
        if unique == 3:
            cont = h2p if max_o == 2 else h3oak
        if unique == 2:
            cont = hfh if max_o == 3 else h4oak

        cont[seq[0]][seq[1]][seq[2]][seq[3]][seq[4]] = hand_bid

    for h in hands:
        cards = [0] * 13
        seq = []
        unique = 0
        max_o = 0
        for c in h[0]:
            id = d[c]
            if cards[id] == 0:
                unique += 1
            cards[id] += 1
            if cards[id] > max_o:
                max_o = cards[id]
            seq.append(id)
        emplace(h[1])

    sum_total = 0
    rank = 1
    sum_part, rank = sum_ranks(rank, hhc)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h1p)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h2p)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h3oak)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, hfh)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h4oak)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h5oak)
    sum_total += sum_part

    return sum_total



def day7_extra():
    with open('inputs/day7.txt') as f:
        hands = [[h[: 5], int(h[6:])] for h in f.read().split("\n") if h != ""]
    print(hands)

    h5oak = make_nested()
    h4oak = make_nested()
    hfh = make_nested()
    h3oak = make_nested()
    h2p = make_nested()
    h1p = make_nested()
    hhc = make_nested()
    d = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}

    def emplace(hand_bid):
        cont = h5oak
        if unique == 5:
            cont = hhc
        if unique == 4:
            cont = h1p
        if unique == 3:
            cont = h2p if max_o == 2 else h3oak
        if unique == 2:
            cont = hfh if max_o == 3 else h4oak

        cont[seq[0]][seq[1]][seq[2]][seq[3]][seq[4]] = hand_bid

    for h in hands:
        cards = [0] * 13
        seq = []
        unique = 0
        jokers = 0
        max_o = 0
        for c in h[0]:
            id = d[c]
            if c == 'J':
                jokers += 1
            elif cards[id] == 0:
                unique += 1
            cards[id] += 1
            if cards[id] > max_o:
                max_o = cards[id]
            seq.append(id)
        max_o += jokers
        emplace(h[1])

    sum_total = 0
    rank = 1
    sum_part, rank = sum_ranks(rank, hhc)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h1p)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h2p)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h3oak)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, hfh)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h4oak)
    sum_total += sum_part
    sum_part, rank = sum_ranks(rank, h5oak)
    sum_total += sum_part

    return sum_total


def sum_ranks(rank, cont):
    sum_b = 0
    for n1 in cont:
        if not n1 :
            continue
        for n2 in n1:
            if not n2:
                continue
            for n3 in n2:
                if not n3:
                    continue
                for n4 in n3:
                    if not n4:
                        continue
                    for n5 in n4:
                        if not n5:
                            continue
                        sum_b += rank * n5
                        rank += 1
    return sum_b, rank


