################################################
#This is Lab 4 for COSC 1336 by Richard Nolan  # 
#The program will display a menu, ask a menu   #
#choice, and play the Change Game if selected. #
################################################

#import module for High Card
import random

#Introduction to the program
print('Hi! Welcome to the Lame Game!')


#Game Menu
print("GAME MENU")
print('1. Make Change')
print('2. High Card')
print('3. Quit')
choice = int(input('Choice: '))

#Invalid Option
if (choice>3 or choice<1):
    print('Invalid Option!');

else:
    while choice != 3:

###MenuChoiceResponses

    #Change Game
        if (choice==1):
            print ('Make Change!')
    
        #Queries for money owed and paid
        owed = float(input('Customer owes: '))
        paid = float(input('Customer paid: '))
    
            #Insufficient payment message
        if paid < owed:
            print("You didn't pay enough!")
        else:
        
            #Prints Change
            change = float(format(paid-owed,'.2f'))
            print('$',change, sep='')
    
            #Prints Change Denomination
            print (int(change//1), "dollars")
            change = change%1
            print (int(change//.25), "quarters")
            change = change%.25
            print (int(change//.10), "dimes")
            change = change%.10
            print (int(change//.05), "nickles")
            change = change%.05
            print (round(change/.01), "pennies")
    
       #High Card Notice   
        elif (choice==2):
        print('High Card')

    #Sentinel Check
    print("GAME MENU")
    print('1. Make Change')
    print('2. High Card')
    print('3. Quit')
    choice = int(input('Choice: '))

    #Invalid Option
    (choice>3 or choice<1):
    print('Invalid Option!');

#Exit Game
(choice==3):
    
