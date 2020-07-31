#####################################################
# COSC 1336 Lab 9                                   #
# Lab 9                                             #
#                                                   #
# This program gives the user a menu of card games  #
# to play.  It will continue to offer the games     #
# unitl the user chooses to quit.                   #
#                                                   #
# Currently available games:                        #
#    1. Make Change                                 #
#    2. High Card                                   #
#    3. Deal Hand                                   #
#    4. Save Dream Hand                             #
#    5. Display Dream Hand                          #
#####################################################

import card_Nolan
import random

# Define global constants for the menu options
MAKE_CHANGE = 1
HIGH_CARD = 2
DEAL_HAND = 3
SAVE_DREAM_HAND = 4
DISPLAY_DREAM_HAND = 5
WORD_GAME = 6
QUIT = 7

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
        elif choice == WORD_GAME:
            display_word_game()

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
    print('* 6. Word Game                                       *')
    print('* 7. Quit                                            *')
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
        print("6. Word Game")
        print("7. Quit")
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
            print("6. Word Game")
            print("7. Quit")
            choice = int(input("\nEnter choice again: "))
        
    except ValueError:
        print("Error: Invalid data entered")
        # Set choice to 0 because an error has occurred
        # Function must always return a value, even
        # if there were an error
        choice = 0
        
    except Exception as err:
        print("Error: ", err)
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

    # Read the amount of the purchase
    price = float(input('\nEnter the amount of the purchase '))

    # Read the amount of the payment
    paid = float(input('Enter the amount of payment '))

    # Check to see if the payment is enough to cover the purchase
    if paid < price:
        print('You did not pay enough')
        
    else:

        # Calculate the change due
        change = paid - price

        # Display the change due
        print('\nChange due: ',format(change,'.2f'))
        #print('   unformatted: ',change)
        print('This breaks down into:')

        # Calculate the number of dollars due
        dollars = int(change//1)
        print('\tDollars:\t',dollars)

        # Isolate the change amount and convert it to an integer.
        # To account for precesion lost converting to an integer,
        # force rounding of the 100ths digit by adding .005
        # to the change portion
        change = int(((change - dollars) + .005)* 100)
        #print('change is now ',change)

        # Calculate the number of quaters due
        quarters = change // 25
        print('\tQuarters:\t',quarters)
        change = change - (quarters * 25)

        # Calculate the number of dimes due
        dimes = change // 10
        print('\tDimes:\t\t',dimes)
        change = change - (dimes * 10)

        # Calculate the number of nickels due
        nickels = change // 5
        print('\tNickels:\t',nickels)
        change = change - (nickels * 5)

        # The number of pennies due will be all that is left
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
    print("High Card")
    print("----------")

    # Prompt for user's names
    player1 = input("What is your first name player one? ")
    player2 = input("What is your first name player two? ")

    # Deal two cards: Generate random card between 1 and 13
    player1_card = card_Nolan.Card()
    player2_card = card_Nolan.Card()
    player1_card.deal()
    player2_card.deal()

    # Display the cards
    print("Card for ", player1, ": ", player1_card, end=' ')
    print("Card for ", player2, ": ", player2_card, end=' ')
    

    # Check to see which card was higher,
    # or if the game is a draw
    if player1_card.get_value() > player2_card.get_value():
        print("Congratulations ", player1, ", You Won!")
    elif player2_card.get_value() > player1_card.get_value():
        print("Congratulations ", player2, ", You Won!")
    else:
        print("The game is a draw; both cards are the same")

#############################################################
# Function:	deal_hand                                   #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will deal a five card hand    #
#               using a random number function then         #
#               displays the face value of each card        #
#############################################################
def deal_hand():
    # Create an empty list
    hand = []
    
    print("Deal Hand")
    print("------------")

    # Deal a five card hand: Generate 5 random cards between 1 and 13
    Card1 = card_Nolan.Card()
    Card1.deal()
    hand.append(Card1)
    Card2 = card_Nolan.Card()
    Card2.deal()
    hand.append(Card2)
    Card3 = card_Nolan.Card()
    Card3.deal()
    hand.append(Card3)
    Card4 = card_Nolan.Card()
    Card4.deal()
    hand.append(Card4)
    Card5 = card_Nolan.Card()
    Card5.deal()
    hand.append(Card5)

    # Display the 5-card hand
    display_hand(hand)

    # Display the total value of the hand
   

###############################################################
# Function:	display_hand                                  #
# Inputs:	5-card hand                                   #
# Outputs:	none                                          #
# Description:	This function displays the face value of a    #
#               5-card hand given the hand of cards as a list #
###############################################################
def display_hand(hand):
    # Go through each card and display the face value
     
        print (hand[0:5])

#############################################################
# Function:	hand_stats                                  #
# Inputs:	5-card hand                                 #
# Outputs:	none                                        #
# Description:	This function displays the total value of   #
#               the cards in a 5-card hand and the average  #
#               given the hand of cards as a list           #
#############################################################


##############################################################
# Function:	save_dream_hand                              #
# Inputs:	none                                         #
# Outputs:	none                                         #
# Description:	This function get a file name from the user  #
#               and their favorite 5-card hand, and saves    #
#               the cards in the file.  The cards are given  #
#               by numeric value:                            #
#               Ace = 1                                      #
#               Two = 2 ... Ten = 10                         #
#               Jack = 11                                    #
#               Queen = 12                                   #
#               King = 13                                    #
##############################################################
def save_dream_hand():

    print("Save Dream Hand")
    print("------------------")

    # Create empty list
    hand = []

    try:
        # Prompt user for 5 cards (numeric value)
        # and store in a list
        for x in range(5):
            card =  int(input("Enter a card (1-13): "))
            # Error check card, must be between 1 and 13
            while card < 1 or card > 13:
                print("Error: card must be between 1 and 13")
                card =  int(input("Enter a card (1-13): "))
            # Add valid card to hand            
            hand.append(card)

        # Get file name from user
        file_name = input("Enter the file name: ")
        outfile = open(file_name, 'w')
    
        # Write the numeric value of each card to a file
        for card in hand:
            outfile.write(str(card) + '\n')

        # Close file
        outfile.close()
        print("Your dream hand as been saved\n")

    # Error trap for invalid value for card
    except ValueError:
        print("Error: Invalid input")

    except Exception as err:
        print("Error: ", err)

###################################################################
# Function:	display_dream_hand                                #
# Inputs:	none                                              #
# Outputs:	none                                              #
# Description:	This function reads and displays the 5-card hand  #
#               stored in the file given by the user and displays #
#               the face value of the card.                       #
###################################################################    
def display_dream_hand():

    print("Display Dream Hand")
    print("---------------------")

    # Create empty list
    hand = []
    
    try:
        # Get file name from user
        file_name = input("Enter the file name: ")
        infile = open(file_name, 'r')

        # Read the cards from the file into a list
        hand = infile.readlines()
           
        # Close file
        infile.close()

        # Convert each card to an integer
        index = 0
        while index < len(hand):
            hand[index] = int(hand[index])
            index += 1
        
        # Display the 5-card hand
        display_hand(hand) 

    # Check for invalid file name
    except FileNotFoundError:
        print("Error: File does not exist")
        
    except Exception as err:
        print("Error: ", err)        
        
#############################################################
# Function:	display_face_value                          #
# Inputs:	integer card value                          #
# Outputs:	none                                        #
# Description:	This function will display the face value   #
#               of a numeric card                           #
#############################################################
def display_face_value(value):
    # Make a list of valid card face values
    # Joker is position 0, since the card values
    # start at 1, not 0
    cards = ['Joker','Ace','Two','Three','Four','Five','Six',
             'Seven','Eight','Nine','Ten','Jack','Queen','King']
    # Display the face value of the card passed in
    print(cards[value])

#############################################################
# Function:	check_word                                  #
# Inputs:	letter, guess, word                         #
# Outputs:	none                                        #
# Description:	This function will check the letters in the #
#               for the word game.                          #
#############################################################

#Function that checks the letters in the word
def check_word(letter, guess, word):
  
   # Iterating over string
   for i in range(0, len(word)):
       # Checking for existence of letters
       if word[i] == letter:
           # Updating guess string
           guess = guess[:i] + letter + guess[i+1:];
  
   # Return updated string
   return guess;
  
#############################################################
# Function:	display_word_game                           #
# Inputs:	none                                        #
# Outputs:	none                                        #
# Description:	This function will play the word game with  #
#               the user.                                   #
#############################################################
  
def display_word_game():
      
   # Reading words  
   word = input("\n Enter a word: ");
  
   # Printing new line
   print("\n" * 100);
  
   # String that holds already guessed characters
   guessedChars = "";
  
   # Storing word length
   wordLen = len(word);
  
   # Forming guess string as a series of astreicks
   guess = '*' * wordLen;
  
   # Iterate till entire word is guessed
   while 1:
       # Reading a letter
       letter = input("\n Enter a letter: ");
      
       # If already guessed
       if letter in guessedChars:
           print("\n You have already guessed " + letter + " \n");
      
       else:
           # Checking word
           guess = check_word(letter, guess, word);
          
           # Updating guessed Characters
           guessedChars = guessedChars[:] + letter
      
           # Printing updated guess string
           print("\n So far you have: \n\n\t" + guess);
  
       # If all letters are guessed correctly
       if '*' not in guess:
           # Printing Message
           print("\n Correct! \n");
           return;

main();
