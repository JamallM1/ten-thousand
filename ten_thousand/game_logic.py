import random
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))
        return tuple(rolls)

    def calculate_score(tup):
        total = 0
        roll = Counter(tup).most_common()

        if roll[0][1] == 6:
            if roll[0][0] == 1:
                return 4000

            return int(roll[0][0]) * 400

        if roll[0][1] == 5:
            if roll[0][0] == 1:
                total += 3000

        if roll[0][1] == 4:
            if roll[0][0] == 1:
                total += 2000

        if roll[0][1] == 3:
            if roll[0][0] == 1:
                total += 1000

        if roll[0][1] == 2:
            if roll[0][0] == 1:
                total += 200

        if roll[0][1] == 1:
            if roll[0][0] == 1:
                total += 100

        return total


