# ------------------------ VITAL MESSAGE GAME ------------------------

# In this game, the player assumes control of a soldier in a dystopian future who must stop an alien lanser missile from hitting the
# Earth by intercepting their code of activation (wich we refer to as 'alien code').

# The player choses the level of the game's difficulty and then we generate the alien code based on the chosen difficulty level.

# The code will be displayed on the screen for a limited time. The time which the alien code will be displayed will depend on the
# difficulty chosen by the player. The player must memorize the screen duing that time

# Then the alien code is erased from the screen and the player must type the code as they remember.
# If the player gets it right, then he wins the game and saves his poeple.
# If the player fails, then it's game over and he and his group suffer enourmous damage.


# LET'S GO!


# Importing modules.

import random
import string
import time
import os

# Defining functions and other useful tools.

# Picking up the letters in the ascii alfabeth for us to generate our random alien code in the game.
words = string.ascii_uppercase


# This funcion converts and also treats a string inserted by the user in an int number.
# It returns the converted number.
def converts_and_treats_str_in_int(n):
    count = 0

    os.system('cls')
    print(game_header)
    while True:
        try:
            n = int(n)
            return n
    
        except Exception:
            count += 1
            if count == 1:
                print("Insert a valid number, that replaces {}".format(n))
            n = input(">>> ")

# This funcion validades and checks if the player typed a valid difficulty level. If not, it acts together with the former function to 
# correct the entry into a valid value.
# It returns the corrected difficulty level.
def difficulty_validador(difficulty):
    error_count = 0

    while True:

        invalid_difficulty = difficulty < 4 or difficulty > 10
        valid_difficulty = 4 <= difficulty <= 10

        if invalid_difficulty:

            error_count += 1
            first_error = error_count == 1
            if first_error:
                difficulty = input("Type a matching difficulty level (4 to 10)!\n>>> ")
            elif not first_error:
                difficulty = input(">>> ")

            try:
                difficulty = converts_and_treats_str_in_int(difficulty)
            except:
                continue

        elif valid_difficulty:

            if error_count > 0:
                os.system('cls')
                print(game_header)
                print("............APPLYING CHANGES...........")
                time.sleep(1.5)

            return difficulty

# This funcion generates the alien code, using the random method. 
# It returns the alien code.
def alien_code_generator():

    alien_code = ''
    
    # The code will be the lenght of the chosen difficulty + 1.
    for n in range(0, difficulty + 1):

        # For each time that we generate a digit for the alien code, we will be rolling a dice to determine if we will generate 
        # a random string or int number.

        # Rolling the dice. It has two values (1 and 2)
        dice = random.randint(1, 2)

        if dice == 1:   # If the dice rolls 1, then we generate a random word from the ascii alfabeth and add it to the alien code.
            digit = random.choice(words)
            alien_code += digit
        elif dice == 2: # If the dice rolls 2, then we generate a random int number from 0 to 9 and add it to the alien code
            digit = str(random.randint(0, 9))
            alien_code += digit

    return alien_code

# This funcion creates a header for the game. It receives a title as a argument wich will be displayed at the center of the header.
# Returns a string.
def header(header):
    if len(header) < 15:
        return f"***********************************************\n\n\t\t{header.upper()}\nauthor: kvtana\n\n***********************************************\n"
    else:
        return f"***********************************************\n\n\t{header.upper()}\nauthor: kvtana\n\n***********************************************\n"


# --------------------------------------------------

# Coding te actual game:

story_message = "The year is 2139, aliens from afar attacked the Earth 40 years ago and you're a soldier in one of the last remaining resistance forces in Earth.\n\nYou are tasked with intercepting the message which contains the code of detonation of an alien nuclear laser system.\nShall you fail, nobody knows what will happen, but the doom is almost certain.\n\nEveryone's depending on you, soldier.....\n"
while True:

    # Displaying the game's header.
    game_header = header("VITAL MESSAGE")
    print(game_header)

    # Displaying the games's story explanation to the player.
    print(story_message)

    # Receiving difficulty level choice from player.
    difficulty = input('-> Choose difficulty (4-10)\n>>> ')

    # Converting player entry in int.
    difficulty = converts_and_treats_str_in_int(difficulty)

    # Validating the difficulty choice.
    difficulty = difficulty_validador(difficulty)

    os.system("cls")

    # Generating the alien code.
    alien_code = alien_code_generator()

    # Printing the alien code on screen. The "time.sleep" function will allow for it to be displayed at a determined time, based on difficulty.
    print(f"-----------------------------------------------\n\nMEMORIZE THE ALIEN LAZER CODE: {alien_code}\n\n-----------------------------------------------")
    time.sleep(0.5 * difficulty)    # Alien code screen time = 0.5 * chosen difficulty.
    # This will allow limited time for the player to memorize the code.

    os.system('cls')
    print(game_header)

    # Receiving the player response.
    print("------------------------------------------------------------------\n\nTYPE THE MESSAGE SHOWN AND INTERRUPT THE LASER FROM HITTING!")
    user_response = input(">>> ").upper().strip() # Transfering the player response to uppercase (upper()) and eliminating the spaces on the edges (strip()).
    print("\n\n------------------------------------------------------------------")

    # Validating the player response.
    if user_response == alien_code: # If correct, then the player wins the game and a winning message is displayed.
        os.system("cls")
        print(header("MESSAGE IS CORRECT\n\tYou saved your people!!!"))
        time.sleep(3)
    elif user_response != alien_code:   # If wrong, then the player losses and a loaing message is displayed.
        os.system("cls")
        print("*****************************************************************\n\n..........................YOU LOST........................\n\nThe laser hit and blow away your main food and weapon resourses.\n\tFrom now on, everything is on a dark note...\n\n*****************************************************************")
        time.sleep(3)

    # Giving the player the choice to restart the game or not.
    print("\nDo you wanna repeat? 1 - YES   2 - NO")
    continue_or_not = input(">>> ")
    if continue_or_not.startswith("1"): # If the player choses to continue, then the terminal is cleared and the loop resumes to it's start.
        os.system("cls")
        continue
    else:   # If the player choses to quit, then the loop is broken.
        os.system("cls")
        break

# Thank you message for those who played the game.
print(game_header)
print("THANK YOU FOR PLAYING!!!!\nkvtana sends compliments.")
