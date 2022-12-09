from collections import deque

# a better way with no classes and a simple algorithm, still doesn't look like Python, it's hard getting used to it after writing in i C based languages
def day8_base():
    f = open("../inputs/day8.txt", "r")
    file = f.read()
    temp = file.split("\n")
    temp.pop()
    ROW_LEN = len(temp[0])
    chart = [[]]*len(temp)
    for i in range(len(temp)):
        chart[i] = [int(x) for x in str(temp[i])]
    f.close()

    tree_count = 0
    max_left = -1
    max_right = -1
    max_up = [-1] * ROW_LEN
    max_down = [-1] * ROW_LEN
    added = deque()

    for i in range(len(chart)):
        max_left = -1
        max_right = -1
        for j in range(ROW_LEN):
            # calculate visible trees in a single row
            if (chart[i][j] > max_left):
                if added.count([i, j]) == 0:
                    tree_count += 1
                    added.append([i, j])
                max_left = chart[i][j]
            if (chart[i][-(j + 1)] > max_right):
                if added.count([i, ROW_LEN-(j+1)]) == 0:
                    tree_count += 1
                    added.append([i, ROW_LEN-(j+1)])
                max_right = chart[i][-(j + 1)]
            # calculate visible trees in a single column
            if chart[i][j] > max_up[j]:
                if added.count([i, j]) == 0:
                    tree_count += 1
                    added.append([i, j])
                max_up[j] = chart[i][j]
            if chart[-(i+1)][j] > max_down[j]:
                if added.count([ROW_LEN-(i+1), j]) == 0:
                    tree_count += 1
                    added.append([ROW_LEN-(i+1), j])
                max_down[j] = chart[-(i+1)][j]

    print("Trees visible: " + str(tree_count))


# less efficient way with classes and lots of code that hardly looks Pythonic
def day8_extra():
    f = open("../inputs/day8.txt", "r")
    file = f.read()
    temp = file.split("\n")
    temp.pop()
    SIZE = len(temp[0])
    f.close()

    chart = [[]]*SIZE
    for i in range(SIZE):
        chart[i] = [int(x) for x in str(temp[i])]
    woods = Forest(chart)
    print("Best spot score count: " + str(woods.find_spot()))


class Forest:
    count = 0
    best_spot = 0

    def __init__(self, file):
        size = len(file)
        self.woods = [[Tree for x in range(size)] for y in range(size)]
        for i in range(0, size):
            for j in range(0, size):
                self.woods[i][j] = Tree(file[i][j], i, j)

    def find_spot(self):
        for row in self.woods:
            for t in row:
                spot = t.calc_spot(self.woods)
                if spot > self.best_spot:
                    self.best_spot = spot
        return self.best_spot


class Tree:

    def __init__(self, height, pos_x, pos_y):
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def calc_spot(self, woods):
        spot_score = 1
        if self.pos_x == 0 or self.pos_x == len(woods) -1:
            return 0
        if self.pos_y == 0 or self.pos_y == len(woods) -1:
            return 0
        side_score = 0
        for i in range(self.pos_x-1, -1, -1):
            if woods[i][self.pos_y].height >= self.height:
                side_score += 1
                break
            else:
                side_score +=1
        spot_score *= side_score
        side_score = 0
        for i in range (self.pos_x+1, len(woods)):
            if woods[i][ self.pos_y].height >= self.height:
                side_score += 1
                break
            else:
                side_score += 1
        spot_score *= side_score
        side_score = 0
        for i in range(self.pos_y-1, -1, -1):
            if woods[self.pos_x][i].height >= self.height:
                side_score += 1
                break
            else:
                side_score += 1
        spot_score *= side_score
        side_score = 0
        for i in range (self.pos_y+1, len(woods)):
            if woods[self.pos_x][ i].height >= self.height:
                side_score += 1
                break
            else:
                side_score += 1
        spot_score *= side_score
        return spot_score
