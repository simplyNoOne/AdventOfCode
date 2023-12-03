import re
import operator, math
import math
from collections import deque

def lcm(a, b):
    return (a*b) // math.gcd(a,b)

def day11_base():
    f = open('inputs/day11.txt', 'r')
    worry = 0
    monkey_items = []
    monkey_rules = []
    monkey_inspections = []
    while True:
        info = f.readline()
        if not info:
            break
        if info.find('Monkey') != -1:
            monkey_inspections.append(0)
            items = re.split('Starting items: |, |\n', f.readline())
            monkey_items.append(deque([x for x in items if x != '' and x != '  '], maxlen=None))
            temp_rules = []
            for i in range(4):
                r = re.split(' |\n', f.readline())
                rules = [x for x in r if x != '']
                if rules[0] == 'Operation:':
                    temp_rules.append(rules[-2:])
                else:
                    temp_rules.append(rules[-1])
            monkey_rules.append(temp_rules)
    f.close()

    for i in range(20):
        for m in range(len(monkey_items)):
            mod = monkey_rules[m][0][1]
            rule = monkey_rules[m][0][0]
            div = int(monkey_rules[m][1])
            check_t = int(monkey_rules[m][2])
            check_f = int(monkey_rules[m][3])
            for x in range(len(monkey_items[m])):
                monkey_inspections[m] += 1
                worry = int(monkey_items[m][0])
                if mod == 'old':
                    i_mod = worry
                else:
                    i_mod = int(mod)
                if rule == '*':
                    worry *= i_mod
                else:
                    worry += i_mod
                worry = math.floor((worry/3))
                if worry % div == 0:
                    monkey_items[check_t].append(str(worry))
                else:
                    monkey_items[check_f].append(str(worry))
                monkey_items[m].popleft()
    monkey_inspections.sort()
    business = monkey_inspections[-1]*monkey_inspections[-2]
    print("Monkey business is " + str(business))


def day11_extra():
    print(part2(details))
    f = open('inputs/day11.txt', 'r')
    monkey_items = []
    monkey_rules = []
    monkey_inspections = []
    while True:
        info = f.readline()
        if not info:
            break
        if info.find('Monkey') != -1:
            monkey_inspections.append(0)
            items = re.split('Starting items: |, |\n', f.readline())
            monkey_items.append(deque([[x, 0] for x in items if x != '' and x != '  '], maxlen=None))
            temp_rules = []
            for i in range(4):
                r = re.split(' |\n', f.readline())
                rules = [x for x in r if x != '']
                if rules[0] == 'Operation:':
                    temp_rules.append(rules[-2:])
                else:
                    temp_rules.append(rules[-1])
            monkey_rules.append(temp_rules)
    f.close()

    for i in range(1000):
        mult = 1_000_000_000
        for m in range(len(monkey_items)):
            mod = monkey_rules[m][0][1]
            rule = monkey_rules[m][0][0]
            div = int(monkey_rules[m][1])
            check_t = int(monkey_rules[m][2])
            check_f = int(monkey_rules[m][3])
            for x in range(len(monkey_items[m])):
                monkey_inspections[m] += 1
                worry = int(monkey_items[m][0][0])
                big_worry = int(monkey_items[m][0][1]) + math.floor(worry/mult)
                worry = worry % mult
                if mod == 'old':
                    big_worry = 2*big_worry*worry + big_worry*big_worry*mult
                else:
                    i_mod = int(mod)
                    if rule == '*':
                        worry *= i_mod
                        big_worry *= i_mod
                    else:
                        worry += i_mod
                if lcm(big_worry*mult + worry, div) == div:
                    monkey_items[check_t].append([str(worry), str(big_worry)])
                else:
                    monkey_items[check_f].append([str(worry), str(big_worry)])
                monkey_items[m].popleft()
    monkey_inspections.sort()
    business = monkey_inspections[-1]*monkey_inspections[-2]
    print("Monkey business is " + str(business))



ops = {
    '+' : operator.add,
    '*' : operator.mul,
}

#I will not use regex. I will outlive the usefulness of regex
with open('inputs/day11.txt') as f:
    monkeys = f.read().strip().split('\n\n')
details = []
for detail in monkeys:
    stuff = detail.split("\n")
    index = int(stuff[0][7:len(stuff[0])-1])
    items = list(map(int, stuff[1][18:].split(", ")))
    operation = [stuff[2][23:].split(" ")[0], stuff[2][23:].split(" ")[1]]
    test = int(stuff[3][21:])
    trueMon = int(stuff[4][29:])
    falseMon = int(stuff[5][30:])
    trades = 0
    details.append([index, items, operation, test, trueMon, falseMon])

def part1(details):
    tradeArr = [0] * len(monkeys)
    for i in range(20):
        for monkey in details:
            for item in monkey[1]:
                multiplier = monkey[2][1]
                if monkey[2][1] == "old":
                    multiplier = item
                newItem = ops[monkey[2][0]](item, int(multiplier))//3
                if newItem%monkey[3]==0:
                    details[monkey[4]][1].append(newItem)
                else:
                    details[monkey[5]][1].append(newItem)
                tradeArr[details[monkey[0]][0]] += 1
            monkey[1] = []
    return sorted(tradeArr)[-1] * sorted(tradeArr)[-2]

lcmNum = 1
for i in details:
    lcmNum = lcm(lcmNum, int(i[3]))
print(lcmNum)

def part2(details):
    tradeArr = [0] * len(monkeys)
    for i in range(10000):
        for monkey in details:
            for item in monkey[1]:
                multiplier = monkey[2][1]
                if monkey[2][1] == "old":
                    multiplier = item
                newItem = ops[monkey[2][0]](item, int(multiplier))%lcmNum
                if newItem%monkey[3]==0:
                    details[monkey[4]][1].append(newItem)
                else:
                    details[monkey[5]][1].append(newItem)
                tradeArr[details[monkey[0]][0]] += 1
            monkey[1] = []
    return sorted(tradeArr)[-1] * sorted(tradeArr)[-2]


