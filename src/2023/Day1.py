
def day1_base():
    f = open('inputs/day1.txt', 'r')
    inst_sum = 0
    while True:
        line = f.readline()
        if not line:
            break
        nums = [l for l in line if l.isdigit()]
        num = int(nums[0])*10 + int(nums[-1])
        inst_sum += num
    f.close()
    return inst_sum


def find_indices(main_string, substring):
    indices = []
    index = main_string.find(substring)
    while index != -1:
        indices.append(index)
        index = main_string.find(substring, index + 1)
    return indices


def day1_extra():
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    f = open('inputs/day1.txt', 'r')
    inst_sum = 0
    while True:
        line = f.readline()
        if not line:
            break
        min_pos = len(line)
        max_pos = -1
        min_num = 10
        max_num = -1
        for i, name in enumerate(num_list):
            pos = find_indices(line, name)
            if len(pos) > 0:
                if pos[0] < min_pos:
                    min_pos = pos[0]
                    min_num = i
                if pos[-1] > max_pos:
                    max_pos = pos[-1]
                    max_num = i
        if max_pos != -1:
            res_line = line[:min_pos] + str(min_num)
            if max_pos != min_pos:
                res_line += line[min_pos:max_pos] + str(max_num)
            res_line += line[max_pos:]
        else:
            res_line = line
        print(res_line)
        nums = [l for l in res_line if l.isdigit()]
        num = int(nums[0])*10 + int(nums[-1])
        inst_sum += num
    f.close()
    return inst_sum
