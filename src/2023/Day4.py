import re
from collections import deque

def day4_base():
    with open('inputs/day4.txt') as f:
        winnings = 0
        while card := f.readline():
            segments = re.split(r'[:|\n]', card)[1:]
            winning = [num for num in segments[0].split(' ') if num != '']
            elfs = [num for num in segments[1].split(' ') if num != '']
            card_val = 1
            for w in winning:
                if w in elfs:
                    card_val *= 2
            card_val = int(card_val / 2)
            winnings += card_val

        return winnings


def day4_extra():
    with open('inputs/day4.txt') as f:
        scratchcards = 0
        card_q = [1]
        while card := f.readline():
            segments = re.split(r'[:|\n]', card)[1:]
            winning = [num for num in segments[0].split(' ') if num != '']
            elfs = [num for num in segments[1].split(' ') if num != '']
            card_val = 0
            print(winning)

            print(elfs)
            for w in winning:
                if w in elfs:
                    card_val += 1
            reps = card_q.pop(0)
            scratchcards += reps
            for i in range(card_val):
                if len(card_q) > i:
                    card_q[i] += reps
                else:
                    card_q.append(1 + reps)
            if len(card_q) == 0:
                card_q.append(1)
            # print(card_q[0:10])
            print(card_val)
        return scratchcards
