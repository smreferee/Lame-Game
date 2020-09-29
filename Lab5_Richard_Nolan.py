################################################
#This is Lab 5 for COSC 1336 by Richard Nolan  # 
#The program will display a menu, ask a menu   #
#choice, and play the Change Game if selected. #
################################################



#import module for High Card

import random

#Main Function
def main():

    # Initialize menu option
    user_choice = menu()

    # Loops until user quits program
    while user_choice != 4:

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
        # Reprompt for new selection    
        user_choice = menu()

#############################################################
# Function:	welcome                                     #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function welcomes the user and         #
#               displays a program description              #
#############################################################

# Display the menu and check for valid choice
def menu():
    print("\nWelcome to Lame Game Room")
    print("-------------------------------------")
    print("1. Make Change")
    print("2. Play High Card")
    print("3. Deal Hand")
    print("4. Quit")
    choice = int(input("\nEnter Choice: "))
    
#############################################################
# Function:	menu                                        #
# Inputs:	none                                        #
# Outputs:	a valid menu choice                         #
# Description:	This function will display the game menu,   #
#               reads the choice, validates the choice      #
#               and returns it                              #
#############################################################

    # Validate user menu choice
    while (choice < 1) or (choice > 4):
        print("Invalid option")
        print("-------------------------------------")
        print("1. Make Change")
        print("2. Play High Card")
        print("3. Deal Hand")
        print("4. Quit")
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

#MAKE CHANGE
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

#HIGH CARD
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

#Print face value of the dealt cards based on the random number;
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
        
#DEAL HAND
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
# Function:	deal_hand                                   #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will deal a five card hand    #
#               using a random number function then         #
#               displays the face value of each card        #
#############################################################
 

main()
