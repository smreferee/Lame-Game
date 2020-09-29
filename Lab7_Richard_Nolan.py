################################################
#This is Lab 6 for COSC 1336 by Richard Nolan  # 
#The program will display a menu, ask a menu   #
#choice, and process a function based on the   #
#choice.                                       #
################################################

import random

# Define global constants for the menu options
MAKE_CHANGE = 1
HIGH_CARD = 2
DEAL_HAND = 3
SAVE_DREAM_HAND = 4
DISPLAY_DREAM_HAND = 5
QUIT = 6

def main():

    # Welcome the user
    welcome()
    
    # Get the first menu choice
    choice = menu()

    # Once the user chooses to quit, do not contiue
    # to display the menu
    while choice != QUIT:

        # Check the choice and play the game chosen
        if choice == MAKE_CHANGE:
            make_change()
        elif choice == HIGH_CARD:
            high_card()
        elif choice == DEAL_HAND:
            deal_hand()
        elif choice == SAVE_DREAM_HAND:
            save_dream_hand()
        elif choice == DISPLAY_DREAM_HAND:
            display_dream_hand()

        # Get the next menu choice
        choice = menu()

#############################################################
# Function:	welcome                                     #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function welcomes the user and         #
#               displays a program description              #
#############################################################
def welcome():
    # Display program description
    print('\n******************************************************')
    print('*   Welcome to the Lame Game computer gaming room    *')
    print('*                                                    *')
    print('* This program display a game menu:                  *')
    print('* 1. Make Change                                     *')
    print('* 2. High Card                                       *')
    print('* 3. Deal Hand                                       *')
    print('* 4. Save Dream Hand                                 *')
    print('* 5. Display Dream Hand                              *')
    print('* 6. Quit                                            *')
    print('*                                                    *')
    print('* Prompts for option and plays the game chosen.      *')
    print('******************************************************\n')

#############################################################
# Function:	menu                                        #
# Inputs:	none                                        #
# Outputs:	a valid menu choice                         #
# Description:	This function will display the game menu,   #
#               reads the choice, validates the choice      #
#               and returns it                              #
#############################################################
def menu():
    
    try:
        # Display the menu and read the choice
        print("\n\nLame Game Main Menu")
        print("-------------------")
        print("1. Make Change")
        print("2. High Card")
        print("3. Deal Hand")
        print("4. Save Dream Hand")
        print("5. Display Dream Hand")
        print("6. Quit")
        choice = int(input("\nEnter choice: "))
        
       # Check for invalid input
        while choice < MAKE_CHANGE or choice > QUIT:
            print("Invalid option...")
            # Display the menu and read the choice again
            print("\n\nLame Game Main Menu")
            print("-------------------")
            print("1. Make Change")
            print("2. High Card")
            print("3. Deal Hand")
            print("4. Save Dream Hand")
            print("5. Display Dream Hand")
            print("6. Quit")
            choice = int(input("\nEnter choice again: "))
        
    except ValueError:
        print("Error: Invalid data entered")
        # Set choice to 0 because an error has occurred
        # Function must always return a value, even
        # if there were an error
        choice = 0

    except Exception as error_msg:
        print("Error:", error_msg)
        # Set choice to 0 because an error has occurred
        # Function must always return a value, even
        # if there were an error
        choice = 0        

    # Pass back the user's choice
    return choice



#############################################################
# Function:	make_change                                 #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will read a purchase amount   #
#               and a payment amount and display the change #
#               due and the breakdown of the change into    #
#               number of dollars, quarters, dimes, nickels #
#               and pennies                                 #
#############################################################

def make_change():
        print("\n Make Change")
        print("------------")
        #Read the amount of the purchase
        price = float(input('\nEnter the amount of the purchase: '))

        #Read the amount of the payment
        paid = float(input('Enter the amount of payment: '))

        #Check to see if the payment is enough to cover the purchase
        if paid < price:
            print('You did not pay enough')
            
        else:

            #Calculate the change due
            change = paid - price

            #Display the change due
            print('\nChange due: ',format(change,'.2f'))
            print('This breaks down into:')
            dollars = int(change//1)
            print('\tDollars:\t',dollars)
            change = int(((change - dollars) + .005)* 100)
            quarters = change // 25
            print('\tQuarters:\t',quarters)
            change = change - (quarters * 25)
            dimes = change // 10
            print('\tDimes:\t\t',dimes)
            change = change - (dimes * 10)
            nickels = change // 5
            print('\tNickels:\t',nickels)
            change = change - (nickels * 5)
            pennies = change
            print('\tPennies:\t',pennies)
            print()
            
#############################################################
# Function:	high_card                                   #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will read the name of each of #
#               2 players deal 2 cards to each player and   #
#               determine who wins:                         #
#               the player with the highest card            #
#############################################################

def high_card():
    print("\n High Card")
    print("-----------")

    #Prompt for and read players' names
    player_1 = input('Enter the first player\'s name: ')
    player_2 = input('Enter the second player\'s name: ')

    #Randomly generate card values
    card_1 = random.randint(1,13)
    card_2 = random.randint(1,13)

    #Display the player names and their card's face value
    print (player_1, 'was dealt:', end=" ")
    display_face_value(card_1)
    print (player_2, 'was dealt:', end=" ")
    display_face_value(card_2)

    #Calculate and display victor
    if card_1 > card_2:
        print (player_1, 'is the winner!')
    elif card_2 > card_1:
        print (player_2, 'is the winner!')
    else:
        print ('It\'s a tie!')

#############################################################
# Function:	face_value                                  #
# Inputs:	integer card value                          #
# Outputs:	none                                        #
# Description:	This function will display the face value   #
#               of a numeric card                           #
#############################################################

def display_face_value(value):
    if value == 1:
        print ('Ace')
    elif value == 2:
        print ('Two')
    elif value == 3:
        print ('Three')
    elif value == 4:
        print ('Four')        
    elif value == 5:
        print ('Five')        
    elif value == 6:
        print ('Six')       
    elif value == 7:
        print ('Seven')        
    elif value == 8:
        print ('Eight')        
    elif value == 9:
        print ('Nine')
    elif value == 10:
        print ('Ten')        
    elif value == 11:
        print ('Jack')        
    elif value == 12:
        print ('Queen')     
    elif value == 13:
        print ('King')

#############################################################
# Function:	deal_hand                                   #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will deal a five card hand    #
#               using a random number function then         #
#               displays the face value of each card        #
#############################################################
        
def deal_hand():

    # Create hand_list list
    hand_list = []

    # Randomly generate card values and store them to hand_list 
    card_1 = random.randint(1,13)
    hand_list.append(card_1)
    card_2 = random.randint(1,13)
    hand_list.append(card_2)
    card_3 = random.randint(1,13)
    hand_list.append(card_3)
    card_4 = random.randint(1,13)
    hand_list.append(card_4)
    card_5 = random.randint(1,13)
    hand_list.append(card_5)

    # Pass hand_list to display_hand()
    display_hand(hand_list)


#############################################################
# Function:	save_dream_hand                             #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will ask the user to input    #
#               the five cards for a dream hand, and then   #
#               save the input to a file.                   #
#############################################################

def save_dream_hand():
    print ('You get to build your dream hand of 5 cards! \nAce (1) is low, and King (13) is high.')

    # Create dream_hand list
    dream_hand = []
    
    try:
        # Get user's card choice, validate card, and add value to dream_hand list
        dream_1 = int(input('Enter the value of your first card: '))
        while dream_1 < 1 or dream_1 > 13: 
            dream_1 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_1)
        
        dream_2 = int(input('Enter the value of your second card: '))
        while dream_2 < 1 or dream_2 > 13: 
            dream_2 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_2)

        dream_3 = int(input('Enter the value of your third card: '))
        while dream_3 < 1 or dream_3 > 13: 
            dream_3 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_3)

        dream_4 = int(input('Enter the value of your fourth card: '))
        while dream_4 < 1 or dream_4 > 13: 
            dream_4 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_4)

        dream_5 = int(input('Enter the value of your last card: '))
        while dream_5 < 1 or dream_5 > 13: 
            dream_5 = int(input('ERROR: Please enter a number from 1 to 13: '))
        dream_hand.append(dream_5)
      
        # Prompt and read user choice for filename
        print()
        filename = str(input('Please name the file to be saved: '))
        # Open the file for writing
        outfile = open(filename, 'w')
        # Write user's card choices to the file
        for line in dream_hand:
            line = str(line) + '\n'
            outfile.write(line)
        # Close the file
        outfile.close()

        print ('Your dream hand was saved to ', filename, '.', sep='')

    except ValueError:
        print()
        print('ERROR: You must enter a number from 1 to 13.')
                        
    
#############################################################
# Function:	display_dream_hand                          #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will ask the user to input    #
#               their saved file with an existing dream     #
#               hand and displays the dream hand.           #
#############################################################

def display_dream_hand():

    # Create display_dream_hand list
    dream_hand = []

    try: 
        # Prompt and read the filename to open
        filename = str(input('Enter the name of the file you want to display: '))
        print()
        # Open the file for reading
        infile = open(filename, 'r')
        # Read and add lines to display_dream_hand list
        for line in infile:
            # Convert line to integer and remove newline character
            line = int(line.rstrip('\n'))
            # Add line to dream_hand list
            dream_hand.append(line)
        # Close the file
        infile.close()

        display_hand(dream_hand)
        
    except FileNotFoundError:
        print ('Error: The file \'',filename, '\' was not found.', sep='')

# Display Hand accepts a list as input and passes
# the items one at a time to display_face_value()
def display_hand(a_list):
    for item in a_list:
        display_face_value(item)

main()
