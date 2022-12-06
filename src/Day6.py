from collections import deque


def day6_base(length):
    f = open("../inputs/day6.txt", "r")
    start =length-1
    buffer = f.read()
    prevs = deque()
    for a in range(length-1):
        prevs.append((buffer[a]))
    search = True
    while search:
        if not buffer[start]:
            print ("fuck")
            break
        for a in range(length-1, 0, -1):
            if buffer[start] == prevs[a-1]:
                prevs.popleft()
                prevs.append(buffer[start])
                start += 1
                break
            if a == 1:
                search = False
        prevs, start, search = check_repeats(prevs, buffer, start, length-1, search)

    start +=1
    print("Start of signal packet at: " + str(start))
    f.close()


def day6_extra(length):     #a slightly better optimized version?
    f = open("../inputs/day6.txt", "r")
    start = length-1
    buffer = f.read()
    prevs = deque()
    for a in range(length-1):
        prevs.append((buffer[a]))
    search = True
    while search:
        if not buffer[start]:
            print ("fuck")
            break
        for a in range(length-1, 0, -1):
            if buffer[start] == prevs[a-1]:
                for i in range(a):
                    prevs.popleft()
                    prevs.append(buffer[start + i])
                start += a
                break
            if a == 1:
                search = False
        prevs, start, search = check_repeats(prevs, buffer, start, length-1, search)
    start +=1
    print("Start of message packet at: " + str(start))
    f.close()


def check_repeats(prevs, buffer, start, length, search):
    for a in range(length):
        for b in range(a):
            if prevs[a] == prevs[b]:
                prevs.popleft()
                prevs.append(buffer[start])
                start +=1
                return prevs, start, True

    return prevs, start, search
