import re
def day5_base():        #probably better optimized, strings appended instead of being rewritten
    f = open("inputs/day5.txt", "r")
    top_creates = ""
    crate_stacks = [""]*9
    while True:
        it = 0
        line_ptr = 1
        line =f.readline()
        if line[line_ptr].isdigit():
            f.readline()
            break
        while line_ptr < len(line):
            if line[line_ptr].isalpha():
                crate_stacks[it] = line[line_ptr] + crate_stacks[it]
            it+=1
            line_ptr = 4*it + 1

    while True:
        line = f.readline()
        if not line:
            break
        inst = re.findall(r'\d+', line)
        indexes = []
        for i in inst:
            indexes.append(int(i))
        amount = indexes[0]
        for i in range(amount):
            crate_stacks[indexes[2]- 1] += crate_stacks[indexes[1]-1][-1]
            crate_stacks[indexes[1] -1] = crate_stacks[indexes[1]-1][:-1]

    for stack in crate_stacks:
        top_creates += stack[-1]

    print("Tops crates: " + top_creates)
    f.close()

def day5_extra():       #worse computation complexity, strings rewritten with every move
    f = open("inputs/day5.txt", "r")
    top_creates = ""
    crate_stacks = [""]*9
    while True:
        it = 0
        line_ptr = 1
        line =f.readline()
        if line[line_ptr].isdigit():
            f.readline()
            break
        while line_ptr < len(line):
            if line[line_ptr].isalpha():
                crate_stacks[it] += line[line_ptr]
            it+=1
            line_ptr = 4*it + 1

    while True:
        line = f.readline()
        if not line:
            break
        inst = re.findall(r'\d+', line)
        indexes = []
        for i in inst:
            indexes.append(int(i))
        amount = indexes[0]

        crate_stacks[indexes[2]- 1] = crate_stacks[indexes[1]-1][:amount] + crate_stacks[indexes[2]- 1]
        crate_stacks[indexes[1] -1] = crate_stacks[indexes[1]-1][amount:]

    for stack in crate_stacks:
        top_creates += stack[0]

    print("Tops crates: " + top_creates)
    f.close()
