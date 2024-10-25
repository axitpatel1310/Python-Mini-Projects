import random

def roll_dice():
    return random.randint(1,6)

def dice_simulator():
    while True:
        roll = input("Roll the dice (Yes/No): ").lower()
        if roll == 'yes':
            result= roll_dice()
            print(f"you rolled the {result}")
        elif roll == 'no':
            print(f"Have a Good Day")
            break
        else:
            print('invalid')

dice_simulator()