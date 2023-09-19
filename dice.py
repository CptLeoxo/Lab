import random

class Dice:
    def dice_roll(self):
        rolls = []
        rolls.append(random.randrange(1, 7)) # Add first dice roll
        rolls.append(random.randrange(1, 7)) # Add seconf dice roll
        if rolls[0] == rolls[1]: # If index 0 == index 1, add same number to list
            rolls.append(rolls[0])
            rolls.append(rolls[0])
        print(rolls)
        return rolls


