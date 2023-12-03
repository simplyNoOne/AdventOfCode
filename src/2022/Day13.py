import ast

def day13_base():
    f = open('inputs/day13.txt', 'r')
    buffer = f.read().split('\n')
    f.close()
    buffer.pop()
    buffer = [x for x in buffer if x]

    data = []
    for l in buffer:
        data.append(ast.literal_eval(l))
    sum_s = 0
    for i in range(0, int(len(data)), 2):
        res1, res2 = analyze(data[i], data[i+1])
        if res2:
            sum_s += (i/2 + 1)
    print("The sum of indices: " + str(sum_s))


def day13_extra():
    f = open('inputs/day13.txt', 'r')
    buffer = f.read().split('\n')
    f.close()
    buffer.pop()
    buffer = [x for x in buffer if x]
    data = []
    for l in buffer:
        data.append(ast.literal_eval(l))
    dividers = [[[2]], [[6]]]
    data += dividers
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            res1, res2 = analyze(data[j], data[j-1])
            if res2:
                temp = data[j][:]
                data[j] = data[j-1]
                data[j-1] = temp[:]
    x = [data.index(x) + 1 for x in dividers]
    key = x[0]*x[1]
    print("Decoder key is " + str(key))

def analyze(data1, data2):
    if len(data1) == 0 and len(data2) == 0:
        return False, False
    elif len(data1) == 0 and len(data2) != 0:
        return True, True
    elif len(data1) != 0 and len(data2) == 0:
        return True, False

    max_i = 0
    for e in range(min(len(data1), len(data2))):
        el1 = data1[e]
        el2 = data2[e]
        if isinstance(el1, list) == isinstance(el2, list):
            if not isinstance(el1, list):
                if el1 != el2:
                    return True, el1 < el2
            else:
                res1, res2 = analyze(el1, el2)
                if res1:
                    return res1, res2
        else:
            if isinstance(el1, list):
                res1, res2 = analyze(el1, [el2])
                if res1:
                    return res1, res2
            else:
                res1, res2 = analyze([el1], el2)
                if res1:
                    return res1, res2
        max_i = e+1
    if len(data1) == max_i and len(data2) == max_i:
        return False, False
    elif len(data1) == max_i:
        return True, True
    elif len(data2) == max_i:
        return True, False
