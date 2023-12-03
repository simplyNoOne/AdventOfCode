def day2_base():

    f = open("inputs/day2.txt", "r")
    mymove = ['X', 'Y', 'Z']
    opponent = ['A', 'B', 'C']

    score = 0
    while True:
        line = f.readline()
        if not line:
            break;
        score += mymove.index(line[2])+1
        if(mymove.index(line[2]) == opponent.index(line[0])):
            score+=3
        elif((opponent.index(line[0]) + 1 == mymove.index(line[2])) or (opponent.index(line[0]) == mymove.index(line[2]) + 2)):
            score += 6
    f.close()
    print("My score: "+ str(score))

def day2_extra():

    f = open("inputs/day2.txt", "r")
    mymove = ['X', 'Y', 'Z']
    opponent = ['A', 'B', 'C']

    score = 0
    while True:
        line = f.readline()
        if not line:
            break;
        score += mymove.index(line[2])*3
        mod = mymove.index(line[2]) -1
        temp = opponent.index(line[0])+mod
        if temp < 0:
            temp = 2
        elif temp == 3:
            temp = 0
        temp += 1
        score += temp
    f.close()
    print("My score: "+ str(score))
