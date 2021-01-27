import random

def main():
    
    # from the user, get the number of dice rolls to perform
    dice_rolls = int( input('How many dice would you like to roll?') )
    
    # from the user, get the number of sides each dice has
    dice_sides = int( input('How many sides are the dice?') )
    
    # create a variable to hold the sum of all dice rolls
    dice_sum = 0

    for _ in range(0, dice_rolls):
        # generate a random number to roll a die
        roll = random.randint(1,dice_sides)
        
        # check if the rolled value is critical fail
        if roll == 1:
            # print critical failure
            print('You rolled a 1! Critical Fail')
        elif roll == 6:
            # print critical success
            print('You rolled a 6! Critical Success!')
        else:
            # print what you rolled
            print(f'You rolled a {roll} !')

        # add this value to the sum variable
        dice_sum += roll

    # print the total value rolled by dice
    print( f'You have rolled a total of {dice_sum}' )


if __name__== "__main__":
    main()
