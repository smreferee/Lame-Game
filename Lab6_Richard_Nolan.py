################################################
#This is Lab 6 for COSC 1336 by Richard Nolan  # 
#The program will display a menu, ask a menu   #
#choice, and process a function based on the   #
#choice.                                       #
################################################



#import module for High Card

import random

#Main Function
def main():

    # Initialize menu option
    user_choice = menu()

    # Loops until user quits program
    while user_choice != 6:

        # User Choice 1 goes to 'Make Change'
        if user_choice == 1:
            print ('You selected Make Change.')
            print()
            make_change()
            print()
        # User Choice 2 goes to 'High Card'
        elif user_choice == 2:
            print ('You selected High Card.')
            print()
            high_card()
            print()
        # User Choice 3 goes to 'Deal Hand'
        elif user_choice == 3:
            print ('You selected Deal Hand.')
            print()
            deal_hand()
            print()
        # User Choice 3 goes to 'Save Dream Hand'
        elif user_choice == 4:
            print ('You selected Save Dream Hand.')
            print()
            save_dream_hand()
            print()
        # User Choice 3 goes to 'Display Dream Hand'
        elif user_choice == 5:
            print ('You selected Display Dream Hand.')
            print()
            display_dream_hand()
            print()   
        # Reprompt for new selection    
        user_choice = menu()

#############################################################
# Function:	menu                                        #
# Inputs:	none                                        #
# Outputs:	a valid menu choice                         #
# Description:	This function will display the game menu,   #
#               reads the choice, validates the choice      #
#               and returns it                              #
#############################################################

# Display the menu and check for valid choice
def menu():
    print("\nWelcome to Lame Game Room")
    print("-------------------------------------")
    print("1. Make Change")
    print("2. Play High Card")
    print("3. Deal Hand")
    print("4. Make Dream Hand")
    print("5. Display Dream Hand")
    print("6. Quit")
    choice = int(input("\nEnter Choice: "))
    

    # Validate user menu choice
    while (choice < 1) or (choice > 6):
        print("Invalid option")
        print("-------------------------------------")
        print("1. Make Change")
        print("2. Play High Card")
        print("3. Deal Hand")
        print("4. Save Dream Hand")
        print("5. Display Dream Hand")
        print("6. Quit")
        choice = int(input("Choose again: "))

    #Valid Choice Return
    return (choice)

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
    print (player_1, 'was dealt:', end=" "), display_face_value(card_1)
    print (player_2, 'was dealt:', end=" "), display_face_value(card_2)

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
    
    #Randomly Deal Hand
    card_1 = random.randint(1,13)
    card_2 = random.randint(1,13)
    card_3 = random.randint(1,13)
    card_4 = random.randint(1,13)
    card_5 = random.randint(1,13)

    #Call Face Values
    print('You were dealt: ')
    display_face_value(card_1)
    display_face_value(card_2)
    display_face_value(card_3)
    display_face_value(card_4)
    display_face_value(card_5)

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
    
    try:
        # Get user's card choice, validate card, and add value to dream_hand list
        dream_1 = int(input('Enter the value of your first card: '))
        while dream_1 < 1 or dream_1 > 13: 
            dream_1 = int(input('ERROR: Please enter a number from 1 to 13: '))
        
        dream_2 = int(input('Enter the value of your second card: '))
        while dream_2 < 1 or dream_2 > 13: 
            dream_2 = int(input('ERROR: Please enter a number from 1 to 13: '))

        dream_3 = int(input('Enter the value of your third card: '))
        while dream_3 < 1 or dream_3 > 13: 
            dream_3 = int(input('ERROR: Please enter a number from 1 to 13: '))

        dream_4 = int(input('Enter the value of your fourth card: '))
        while dream_4 < 1 or dream_4 > 13: 
            dream_4 = int(input('ERROR: Please enter a number from 1 to 13: '))

        dream_5 = int(input('Enter the value of your last card: '))
        while dream_5 < 1 or dream_5 > 13: 
            dream_5 = int(input('ERROR: Please enter a number from 1 to 13: '))
      
        # Prompt and read user choice for filename
        print()
        filename = str(input('Please name the file to be saved: '))

        # Open the file for writing
        outfile = open(filename, 'w')

        # Write user's card choices to the file
        dream_1 = str(dream_1) + '\n'
        outfile.write(dream_1)
        dream_2 = str(dream_2) + '\n'
        outfile.write(dream_2)
        dream_3 = str(dream_3) + '\n'
        outfile.write(dream_3)
        dream_4 = str(dream_4) + '\n'
        outfile.write(dream_4)
        dream_5 = str(dream_5) + '\n'
        outfile.write(dream_5)
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

    try: 
        # Prompt and read the filename to open
        filename = str(input('Enter the name of the file you want to display: '))
        print()

        # Open the file for reading
        infile = open(filename, 'r')

        # Read and convert lines
        dhcard_1 = infile.readline()
        dhcard_1 = int(dhcard_1.rstrip('\n'))
        dhcard_2 = infile.readline()
        dhcard_2 = int(dhcard_2.rstrip('\n'))
        dhcard_3 = infile.readline()
        dhcard_3 = int(dhcard_3.rstrip('\n'))
        dhcard_4 = infile.readline()
        dhcard_4 = int(dhcard_4.rstrip('\n'))
        dhcard_5 = infile.readline()
        dhcard_5 = int(dhcard_5.rstrip('\n'))

        # Close the file
        infile.close()

        #Display Dream Hand
        print('Your Dream Hand is: ')
        display_face_value(dhcard_1)
        display_face_value(dhcard_2)
        display_face_value(dhcard_3)
        display_face_value(dhcard_4)
        display_face_value(dhcard_5)
        
    except FileNotFoundError:
        print ('Error: The file \'',filename, '\' was not found.', sep='')

main()
