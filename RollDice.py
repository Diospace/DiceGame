""""""" Roll Dices Game"""""""""
"""A DiE RANGE FROM NUMBERS 1 TO 6, FOR A ROLL OF TWO DIE,
THE USER MAKE A BET FROM THE AMOUNT IN HIS BANK, AND ALSO MAKE A POINT,
****the point is a nummber choices by user,this can be a sum of two die guess by user before the dice is roll and this number guess is valid from 2 to 12****
THE USER HAVE 5 TIMES TO MAKE IS POINT, IF LAPSE THE GAME END AND USER COULD NOT MET IS POINT HE LOSE HIS BET AND THE AMOUNT IS SUNSTRACTED FROM BANK
"""

import random
import string


DICE_LIST=[1,2,3,4,5,6]
DIE_ONE=0
DIE_TWO= 0
DICE_TOTAL=0
BANK_CHIPS=100
TOTAL_CHANCE=5
SUM_DIE=0


def roll_choice():
    """get ramdom number from DICE_LIST
    save DICE_LIST in dice_list
    and get one value as a choice from dice_list
    """
    dice_list= DICE_LIST
    return random.choice(dice_list)

def get_die():
    """get the Two die from roll_choice function
    get DIE_ONE and DIE_TWO and save in a list DIE_ROLLED list
    """
    DIE_ROLLED =[]
    DIE_ONE =roll_choice()
    DIE_TWO= roll_choice()
    DIE_ROLLED.append(DIE_ONE)
    DIE_ROLLED.append(DIE_TWO)
    return  DIE_ROLLED

def print_die(die_list):
    """print each die value
      get each die value from a list of length 2
       """
    list =die_list
    for i in list:
        print(i)

def Sum_die(die_list):
    """Sum the value of die
          get each die value from a list of length 2
          and sum the values
           """
    sum=0
    list = die_list
    for i in list:
        sum+=i
    return sum

def Check_TRYAGAIN_INPUT(try_again ):
    """Check try again input
    if try_again input is YES, break and move on,
    if NO, exit and end game
    if not valid, then input try_again value.
               """
    while try_again != "yes" or try_again != "no":

        if try_again == "yes":
            break
        elif try_again == "no":
            print("Thanks for Playing")
            exit(0)
        else:
            print('your answer should be "yes" or "no"')
        try_again = input("Roll the Dice 5 times Again?")


def Roll_Play():
    """Roll_play function, plays the dices games,
    for the game goes on if bank_chips is not Zero
    if bank_chips ==0 the game break or exit(0)
    for a point made, the  bet is double and it is added to bank_chips
    ask to reply after 5 roll, if YES, then the game goes on if No. exit the Game
    """
    bank_chips=BANK_CHIPS
    chance=TOTAL_CHANCE

    while bank_chips is not 0:
        rem_chance = TOTAL_CHANCE
        init_chance = 1
        print("You have five Rolls to make your Point")
        print("Your bet cannot exceed the amount you have left in your bank.")
        print("You have", str(bank_chips), " chips in your banks.")
        user_bank_chips = int(input("Place your bet::"))

        if user_bank_chips > bank_chips:
            while user_bank_chips> bank_chips:
                print("You have ", str(bank_chips), " in bank, you can't bet with ", str(user_bank_chips))
                user_bank_chips = int(input("Place your bet::"))

        user_point = int(input("What is your point? "))
        if user_point < 2 or user_point > 12:
            while user_point <2 or user_point >12:
                print("Invalid point, your point should be from 2 to 12")
                user_point = int(input("What is your point?"))
        print("\n")
        print("Rolling The Dices... ")

        print("Roll number ", str(init_chance), " of ", str(chance))
        Die_list = get_die()
        print(" The Values are:")
        print_die(Die_list)
        print("You Rolled ", str(Sum_die(Die_list)))
        print("Your Point is ", str(user_point))

        if bank_chips ==0:
            break

        else:
            if Sum_die(Die_list) != user_point:
                for i in range(chance - 1):
                    print("You did not make your point.")
                    rem_chance = chance - init_chance
                    print("You have ", str(rem_chance), " more Rolls to make your point.")
                    print("\n")
                    print("Rolling The Dices... ")
                    init_chance += 1

                    print("Roll number ", str(init_chance), " of ", str(chance))
                    Die_list = get_die()
                    print(" The Values are:")
                    print_die(Die_list)
                    print("You Rolled ", str(Sum_die(Die_list)))
                    print("Your Point is ", str(user_point))
                    if Sum_die(Die_list) == user_point:
                        user_bank_chips *= 2
                        bank_chips += user_bank_chips
                        print(".......You Won......,\t You Score ", bank_chips)
                        break

                    if init_chance == chance:
                        print("You have no more Roll")
                        print("\t")
                        print("Sorry, You lost your bet -", str(user_bank_chips))
                        bank_chips  -=user_bank_chips
                        if bank_chips == 0:
                            print("Oops, you don't have any more money in your Bank..")
                            exit(0)

            else:
                user_bank_chips *=2
                bank_chips +=user_bank_chips
                print(".......You Won......,\t You Score ",bank_chips)
        print("\t")
        try_again = input("Roll the Dice 5 times Again?")
        Check_TRYAGAIN_INPUT(try_again )



def Dice_Game():
    """Call the Roll_Play function"""
    Roll_Play()
    # print("This is a dice game")

if __name__ == "__main__":

    Dice_Game()



get_die()