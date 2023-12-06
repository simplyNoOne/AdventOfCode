import math


def day6_base():
    with open('inputs/day6.txt') as f:
        times = [int(t) for t in f.readline().split(' ')[1:] if t != '']
        distances = [int(d) for d in f.readline().split(' ')[1:] if d != '']
    res = 1
    for t, d in zip(times, distances):
        min_t = 0
        max_t = 0
        for press in range(1, t):
            if (press + math.ceil(d/press)) <= t:
                if min_t == 0:
                    min_t = press
            else:
                if min_t != 0:
                    max_t = (press - 1)
                    break
        res *= (1 + max_t - min_t)
    return res


def check_time(time, dist, press):
    return (press + math.ceil(dist/press)) <= time


def get_min(time, dist):
    min_t = math.ceil(time/2)
    jump = math.ceil(time/2)
    while True:
        jump //= 2
        jump = 1 if jump == 0 else jump
        if check_time(time, dist, min_t):
            if check_time(time, dist, min_t - 1):
                min_t -= jump
            else:
                return min_t
        else:
            if check_time(time, dist, min_t + 1):
                return min_t + 1
            else:
                min_t += jump


def get_max(time, dist):
    max_t = math.ceil(time/2)
    jump = math.ceil(time/2)
    while True:
        jump //= 2
        jump = 1 if jump == 0 else jump
        if check_time(time, dist, max_t):
            if check_time(time, dist, max_t + 1):
                max_t += jump
            else:
                return max_t
        else:
            if check_time(time, dist, max_t - 1):
                return max_t - 1
            else:
                max_t -= jump


def day6_extra():
    with open('inputs/day6.txt') as f:
        times = [t for t in f.readline().split(' ')[1:] if t != '']
        distances = [d for d in f.readline().split(' ')[1:] if d != '']
        time = ""
        dist = ""
        for t in times:
            time += t
        for d in distances:
            dist += d
        time = int(time)
        dist = int(dist)
    res = 1 + get_max(time, dist) - get_min(time, dist)
    return res
