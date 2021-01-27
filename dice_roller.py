import random

dice_rolls = 2
dice_sum = 0

def main():
    # tell python that dice_rolls and doce_sum are global variables
    global dice_sum, dice_rolls

    for _ in range(0, dice_rolls):
        # generate a random number to roll a die
        roll = random.randint(1,6)
    
        # print what you rolled
        print(f'You rolled a {roll} !')

        # add this value to the sum variable
        dice_sum += roll

    # print the total value rolled by dice
    print( f'You have rolled a total of {dice_sum}' )


if __name__== "__main__":
    main()
