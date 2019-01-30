from collections import Counter
from pprint import pprint

def check2(counts):
    return 2 in counts.values()

def check3(counts):
    return 3 in counts.values()

counts = []
hastwo = 0
hasthree = 0

with open("day2-input","r") as day2_input:
    lines = day2_input.readlines()
    lines = [x.strip() for x in lines] 
    [ counts.append(Counter(line)) for line in lines ]
    pprint(counts)

    for curr in counts:
        if check2(curr):
            hastwo = hastwo + 1

        if check3(curr):
            hasthree = hasthree + 1


    answer = hastwo * hasthree
    print("hastwo: {} hasthree: {} answer: {}".format(hastwo, hasthree, answer))
