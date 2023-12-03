import re
import numpy as np
from collections import deque

def day9_base():
    f = open("inputs/day9.txt", "r")
    codes = ['R', 'L', 'U', 'D']
    idents = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    H = [0, 0]
    T = [0, 0]
    move = [0, 0]
    tail_pos = deque()

    while True:
        instructions = f.readline()
        if not instructions:
            break
        vals = re.split('\n| ', instructions)
        for i, j in zip(codes, idents):
            if vals[0] == i:
                move = j
                break

        for x in range(int(vals[1])):
            prevH = H
            H = [a+b for a, b in zip(H, move)]
            for i, j in zip(H, T):
                if abs(i - j) > 1:
                    if prevH[0] == T[0] or prevH[1] == T[1]:
                        T = [a+b for a, b in zip(T, move)]
                        break
                    else:
                        comp = move.index(0)
                        chase = move[:]
                        chase[comp] = np.sign(H[comp] - T[comp])
                        T = [a+b for a, b in zip(T, chase)]
                        break
            if T not in tail_pos:
                tail_pos.append(T)
    f.close()
    print("Tail was found in " + str(len(tail_pos)))

def day9_extra():
    f = open("inputs/day9.txt", "r")
    codes = ['R', 'L', 'U', 'D']
    idents = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    rope = [[0, 0]]*10
    move = [0, 0]
    tail_pos = deque()

    while True:
        instructions = f.readline()
        if not instructions:
            break
        vals = re.split('\n| ', instructions)
        for i, j in zip(codes, idents):
            if vals[0] == i:
                move = j
                break

        for x in range(int(vals[1])):
            next_r = True
            prevR = rope[0]
            rope[0] = [a+b for a, b in zip(rope[0], move)]
            for r in range(len(rope)-1):
                prevT = []
                if not next_r:
                    break
                for i in range(len(rope[r])):
                    if abs(rope[r][i] - rope[r+1][i]) > 1:
                        if prevR[0] == rope[r+1][0] or prevR[1] == rope[r+1][1]:
                            prevT = rope[r+1][:]
                            rope[r+1] = [a+b for a, b in zip(rope[r+1], move)]
                            next_r = True
                            break
                        else:
                            prevT = rope[r+1][:]
                            comp = move.index(0)
                            chase = move[:]
                            chase[comp] = np.sign(rope[r][comp] - rope[r+1][comp])
                            rope[r+1] = [a+b for a, b in zip(rope[r+1], chase)]
                            next_r = True
                            break
                    else:
                        prevT = rope[r+1]
                        next_r = False
                prevR = prevT

            if rope[9] not in tail_pos:
                tail_pos.append(rope[9])
            #print(rope)

    f.close()
    print("Tail was found in " + str(len(tail_pos)))

def check():

    with open("../inputs/day9.txt", "r") as f:
        content = f.read().splitlines()

    visited_locations_1, visited_locations_2 = [[0, 0]], [[0, 0]]
    rope = [[0, 0] for _ in range(10)]

    def main(head_location, tail_location): # both methods work
        if True:
            if abs(tail_location[0] - head_location[0]) == 2:
                tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
                if abs(tail_location[1] - head_location[1]) >= 1:
                    tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
            elif abs(tail_location[1] - head_location[1]) == 2:
                tail_location[1] += [1, -1][tail_location[1] > head_location[1]]
                if abs(tail_location[0] - head_location[0]) >= 1:
                    tail_location[0] += [1, -1][tail_location[0] > head_location[0]]
        if False:
            if tail_location[0] - head_location[0] == 2:
                tail_location[0] -= 1
                if tail_location[1] - head_location[1] >= 1:
                    tail_location[1] -= 1
                elif tail_location[1] - head_location[1] <= -1:
                    tail_location[1] += 1
            elif tail_location[0] - head_location[0] == -2:
                tail_location[0] += 1
                if tail_location[1] - head_location[1] >= 1:
                    tail_location[1] -= 1
                elif tail_location[1] - head_location[1] <= -1:
                    tail_location[1] += 1
            elif tail_location[1] - head_location[1] == 2:
                tail_location[1] -= 1
                if tail_location[0] - head_location[0] >= 1:
                    tail_location[0] -= 1
                elif tail_location[0] - head_location[0] <= -1:
                    tail_location[0] += 1
            elif tail_location[1] - head_location[1] == -2:
                tail_location[1] += 1
                if tail_location[0] - head_location[0] >= 1:
                    tail_location[0] -= 1
                elif tail_location[0] - head_location[0] <= -1:
                    tail_location[0] += 1
        return tail_location

    for i in range(0, len(content)):
        for j in range(0, int(content[i][2:])):
            if content[i][0] == "U":
                rope[0][1] += 1
            elif content[i][0] == "D":
                rope[0][1] -= 1
            elif content[i][0] == "L":
                rope[0][0] -= 1
            elif content[i][0] == "R":
                rope[0][0] += 1
            for k in range(1, 10):
                rope[k] = main(rope[k-1], rope[k])
            if rope[1] not in visited_locations_1:
                visited_locations_1.append(rope[1][:])
            if rope[9] not in visited_locations_2:
                visited_locations_2.append(rope[9][:])
    print("Part 1:", len(visited_locations_1))
    print("Part 2:", len(visited_locations_2))
