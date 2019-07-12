from itertools import groupby
import json

def dimension_check(data: list) -> bool:
    return sum([1 for idx, line in enumerate(data) if len(data)==len(line)])==10


def content_check(data: list) -> bool:
    return sum([1 for line in data if set(line).issubset({1,0})]) == 10


def ring(data: list) -> list:
    data = [[0]*len(data[0])] + data + [[0]*len(data[0])]
    data = [[0] + i + [0] for i in data]
    return data


def adjacent(data: list) -> bool:
    diagonal = []
    adj = []
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            if data[i][j] == 1:
                diagonal.append(sum([data[i-1][j-1], data[i-1][j+1],
                                  data[i+1][j-1], data[i+1][j+1]]))
                adj.append(set([sum([data[i-1][j],data[i][j-1]]),
                      sum([data[i-1][j],data[i][j+1]]),
                      sum([data[i+1][j],data[i][j+1]]),
                      sum([data[i+1][j],data[i][j-1]])]))
    return sum([1 for i in adj if 2 in i]) + sum(diagonal) == 0


def count_one(data: list) -> int:
    adj = []
    for i in range(1, len(data)-1):
        for j in range(1, len(data)-1):
            if data[i][j] == 1:
                adj.append(set([sum([data[i-1][j],data[i][j-1]]),
                      sum([data[i-1][j],data[i][j+1]]),
                      sum([data[i+1][j],data[i][j+1]]),
                      sum([data[i+1][j],data[i][j-1]])]))

    return sum([i=={0} for i in adj])


def counter_2_to_4(data: list) -> dict:
    map = {(1, 2):0,
            (1, 3):0,
            (1, 4):0,
    }
    for line in data:
        grouped = [(k, sum(1 for i in g)) for k,g in groupby(line)]
        for item in grouped:
            if item in map:
                map[item] += 1
    return map


def rotate(data: list) -> dict:
    return counter_2_to_4(list(zip(*data)))


def collector(data: list) -> bool:
    collection = dimension_check(data) \
        and content_check(data) \
        and adjacent(ring(data))
    count_2 = counter_2_to_4(data)[(1, 2)] + rotate(data)[(1, 2)]
    count_3 = counter_2_to_4(data)[(1, 3)] + rotate(data)[(1, 3)]
    count_4 = counter_2_to_4(data)[(1, 4)] + rotate(data)[(1, 4)]
    count = (count_one(ring(data)), count_2, count_3, count_4) == (4, 3, 2, 1)
    return collection and count


def main(path: str) -> bool:
    with open(path, "r") as inp:
        try:
            bord = json.loads(inp.read())
            return collector(bord)
        except:
            return False

#print(main("battleship_board.txt"))

#print(adjacent(ring([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0
#, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])))
