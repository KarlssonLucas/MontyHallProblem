import Algorithm
import random
from Door import Door

doorlist = []


##
#  CONTROLLERS FOR USER TO AFFECT THE ALGORITHM
##

alwayschange = True
iterations = 100000
doors = 3


def main():
    createdoors(doors)
    Algorithm.runalgorithm(doorlist, iterations, alwayschange)


def createdoors(amountdoors):
    for i in range(amountdoors):
        doorlist.append(Door(i, "goat"))
    carbehinddoor = random.randint(0, amountdoors - 1)
    doorlist[carbehinddoor].contains = "car"


main()
