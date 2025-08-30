from random import randint

def roll(sides: int, advantage: int = None,
         percentile: bool = False, minimum: int = 1) -> tuple[int, int]:
    """
    Roll a die and return the randomized result

    Args:
        sides      (int) : Number of sides on the die
        advantage  (bool): [Optional] Should the user be given advantage,
                            disadvantage or None. (Default: None)
        percentile (bool): [Optional] Should the die be returned as a
                            percentile (Default: False)
        minimum    (int) : [Optional] Minimum Number on the die (Default: 1)

    Returns:
        A tuple containing:
            - Int: Actual Rolled number
            - Int: None, unless advantage then other roll
    """
    roll_amount = randint(minimum, sides)

    if percentile:
        if roll_amount > 10:
            roll_amount -= 10
        roll_amount *= 10

    if not advantage == None:
        adv_roll = randint(minimum, sides)

        if percentile:
            if adv_roll > 10:
                adv_roll -= 10
            adv_roll *= 10

        if advantage == 1:
            if adv_roll > roll_amount:
                return (adv_roll, roll_amount)
            else:
                return (roll_amount, adv_roll)
        else:
            if adv_roll < roll_amount:
                return (adv_roll, roll_amount)
            else:
                return (roll_amount, adv_roll)

    return (roll_amount, None)

if __name__ == "__main__":
    print("Roll a D20: ", roll(20))
    print("Advantage: ", roll(20, 1))
    print("Disadvantage: ", roll(20, -1))
    print("Percentile: ", roll(20, None, True))
    print("ADV Percentile: ", roll(20, 1, True))
    print("DIS Percentile: ", roll(20, -1, True))
