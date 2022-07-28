import random
from collections import Counter


class Banker:
    score = 0

    def __init__(self):
        pass

    @staticmethod
    def add_score(points):
        Banker.score += points

    @staticmethod
    def get_score():
        return Banker.score

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num):
        rolls = []
        while len(rolls) < num:
            rolls.append(random.randint(1, 6))

        return tuple(rolls)

    @staticmethod
    def calculate_score(tup):
        total = 0
        roll = Counter(tup).most_common()

        if len(tup) == 0:
            return total

        print(f"print roll: {roll}")

        # straight
        if len(roll) == 6:
            total += 1500

        #6 of a kind
        if roll[0][1] == 6:
            if roll[0][0] == 1:
                total += 4000
                return total
            total += int(roll[0][0]) * 400
            return total

        #5 of a kind
        elif roll[0][1] == 5:
            if roll[0][0] == 1:
                total += 3000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    total += 50

                elif roll[1][0] == 1:
                    total += 100

            else:
                total += int(roll[0][0]) * 300
                return total

        #4 of a kind
        elif roll[0][1] == 4:
            if roll[0][0] == 1:
                total += 2000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    total += 50 * roll[1][1]

                elif roll[1][0] == 1:
                    total += 100 * roll[1][1]

                elif roll[2][0] == 5:
                    total += 50 * roll[2][1]

                elif roll[2][0] == 1:
                    total += 100 * roll[2][1]

            else:
                total += int(roll[0][0]) * 200
                return total

        # double 3 of a kind
        elif len(roll) == 2:
            if roll[0][1] == 3 and roll[1][1] == 3:
                if roll[0][0] == 1:
                    total += 1000
                    return total + roll[1][0] * 100

                if roll[1][0] == 1:
                    total += 1000
                    return total + roll[0][0] * 100

                return roll[0][0] * 100 + roll[1][0] * 100

        # 3 of a kind
        elif roll[0][1] == 3:
            if roll[0][0] == 1:
                total += 1000

            elif len(roll) > 1:
                if roll[1][0] == 5:
                    total += 50 * roll[1][1]

                elif roll[1][0] == 1:
                    total += 100 * roll[1][1]

                elif roll[2][0] == 5:
                    total += 50 * roll[2][1]

                elif roll[2][0] == 1:
                    total += 100 * roll[2][1]

                elif roll[3][0] == 5:
                    total += 50 * roll[3][1]

                elif roll[3][0] == 1:
                    total += 100 * roll[3][1]

            else:
                total += int(roll[0][0]) * 100
                return total

        # 3 pairs
        elif len(roll) > 2:
            if roll[0][1] and roll[1][1] and roll[2][1] == 2:
                total += 1500
                return total

        # pair 1's
        elif roll[0][1] == 2 and roll[0][0] == 1:
            total += 200

        # pair 5's
        elif roll[0][1] == 2 and roll[0][0] == 5:
            total += 100

        elif len(roll) > 1:
            if roll[1][1] == 2 and roll[1][0] == 5:
                total += 100

        # single 1's
        elif roll[0][0] == 1:
            total += 100

        # single 5's
        elif roll[0][0] == 5:
            total += 50

        return total




def play_game():
    ans = intro()
    if ans == "y":
        start()
    else:
        leave_game()


def intro():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    return input("> ")


def leave_game():
    print("Ok. Maybe another time")


def start():
    min_round = 1
    max_round = 20
    while round <= max_round:
        result = start_round(round)

        if result == "q":
            break

        round += 1

    end_game()


def end_game():
    return print(f"Thanks for playing. You earned {Banker.get_score()} points")


def start_round(round):
    print(f"Starting round {round}")
    round_points = 0

    dice_shelf = GameLogic.dice_shelf()

    round_result = do_round(dice_shelf)
    choice = round_result[0]
    turn_points = round_result[1]
    round_points += turn_points

    if choice == "q":
        return "q"
    elif choice == "b":
        print(f"You banked {round_points} points in round {round}")
        Banker.add_score(round_points)
        print(f"Total score is {Banker.get_score()} points")

    return round_points


def do_round(shelf):
    while True:
        print(f"Rolling {shelf[1]} dice...")
        roll = do_turn(shelf[1])
        print(f"*** {display_roll(roll)} ***")

        keep = input("> ")

        if keep == "q":
            return "q", 0

        shelf = add_to_shelf(keep)

        turn_points = GameLogic.calculate_score(shelf[0])
        print(f"You have {turn_points} unstored points and {shelf[1]} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        return input("> "), turn_points


def do_turn(num):
    return GameLogic.roll_dice(num)


def display_roll(roll):
    roll_values = []
    for num in roll:
        roll_values.append(str(num))
    formatted_roll = " ".join(roll_values)
    return formatted_roll


def add_to_shelf(keep):
    return GameLogic.dice_shelf(keep)


if __name__ == '__main__':
    play_game()