import string

def day3_base():
    sum_priorities = 0
    occurences = [0]*52
    letters = string.ascii_letters
    f = open("inputs/day3.txt", "r")
    while True:
        rucksack = f.readline()
        if not rucksack:
            break
        comp_size = int(len(rucksack)/2)
        comp1 = rucksack[:comp_size]
        comp2 = rucksack[comp_size:]
        for letter in comp1:
            priority = letters.index(letter)
            if occurences[priority] == 0:
                occurences[priority] = 1
        for letter in comp2:
            priority = letters.index(letter)
            if occurences[priority] == 1:
                sum_priorities += priority + 1
                occurences = [0]*52
                break

    f.close()
    print("sum of priorities: "+str(sum_priorities))

def day3_extra():
    badges_priorities = 0
    letters = string.ascii_letters
    occurences = [0]*52
    f = open("inputs/day3.txt", "r")
    while True:
        elf1 = f.readline()
        if not elf1:
            break
        elf2 = f.readline()
        elf3 = f.readline()

        for let in elf1:
            if let == "\n":
                break
            priority = letters.index(let)
            if occurences[priority] == 0:
                occurences[priority] = 1
        for let in elf2:
            if let == "\n":
                break
            priority = letters.index(let)
            if occurences[priority] == 1:
                occurences[priority] = 2
        for let in elf3:
            if let == "\n":
                break
            priority = letters.index(let)
            if occurences[priority] == 2:
                badges_priorities += priority + 1
                occurences = [0]*52
                break
    f.close()
    print("sum of badge priorities: "+str(badges_priorities))
