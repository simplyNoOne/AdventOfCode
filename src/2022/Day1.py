def day1_base():
    f = open("inputs/day1.txt", "r")
    elfs_cals = 0
    max_cals = 0
    while True:
        line = f.readline()
        if not line:
            break
        if line != "\n":
            elfs_cals += int(line)
        else:
            if elfs_cals > max_cals:
                max_cals = elfs_cals
            elfs_cals = 0
    print("Top elf's calories: " + str(max_cals))
    f.close()

def day1_extra():
    f = open("inputs/day1.txt", "r")
    elfs_cals = 0
    max1_cals = 0
    max2_cals = 0
    max3_cals = 0
    while True:
        line = f.readline()
        if not line:
            break
        if line != "\n":
            elfs_cals += int(line)
        else:
            if elfs_cals > max3_cals:
                if elfs_cals > max2_cals:
                    max3_cals = max2_cals
                    if elfs_cals > max1_cals:
                        max2_cals = max1_cals
                        max1_cals = elfs_cals
                    else:
                        max2_cals = elfs_cals
                else:
                    max3_cals = elfs_cals
            elfs_cals = 0

    print("Calories from top 3 elves: " + str(max1_cals + max2_cals + max3_cals))
    f.close()
