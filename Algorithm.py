import random

probabilitytowin = 0
currentdoor = 0
global wins


def runalgorithm(doorlist, iterations, alwayschange):
    wins = 0
    for i in range(iterations):
        currentdoor = random.randint(0, len(doorlist) - 1)
        if doorlist[currentdoor].contains != "car" and alwayschange:
            wins += 1
        elif doorlist[currentdoor].contains == "car" and not alwayschange:
            wins += 1

    print(wins / iterations)
