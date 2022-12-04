
def day4_base():
    f = open("../inputs/day4.txt", "r")
    contains_count = 0
    while True:
        pair = f.readline()
        if not pair:
            break
        assignments = pair.split(",")
        elf1 = assignments[0].split("-")
        elf2 = assignments[1].split("-")
        ref = [0]*4 #[1b>=2b, 1e<=2e, 1b<=2b, 1e>=2e]
        if int(elf1[0]) >= int(elf2[0]):
            ref[0] = 1
        if int(elf1[1]) <= int(elf2[1]):
            ref[1] = 1
        if int(elf1[0]) <= int(elf2[0]):
            ref[2] = 1
        if int(elf1[1]) >= int(elf2[1]):
            ref[3] = 1
        if (ref[0] + ref[1]) == 2 or (ref[2] + ref[3]) == 2:
            contains_count+=1
    print("count of repeats: " + str(contains_count))
    f.close()

def day4_extra():
    f = open("../inputs/day4.txt", "r")
    overlap_count = 0
    while True:
        pair = f.readline()
        if not pair:
            break
        assignments = pair.split(",")
        elf1 = assignments[0].split("-")
        elf2 = assignments[1].split("-")
        cond1 = int(elf1[0]) >= int(elf2[0]) and (int(elf1[0]) <= int(elf2[1]))
        cond2 = int(elf1[1]) >= int(elf2[0]) and (int(elf1[1]) <= int(elf2[1]))
        cond3 = int(elf2[0]) >= int(elf1[0]) and (int(elf2[0]) <= int(elf1[1]))
        cond4 = int(elf1[1]) >= int(elf2[0]) and (int(elf1[1]) <= int(elf2[1]))
        if cond1 or cond2 or cond3 or cond4:
            overlap_count += 1

    print("count of all overlaps: " + str(overlap_count))
    f.close()
