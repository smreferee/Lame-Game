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
        print('High Card Game')

        #Player Names
        Player_1 = input("Enter Player 1's name: ")
        Player_2 = input("Enter Player 2's name: ")

        #Draw random cards
        card_1 = random.randint(1,13)
            if card_1 == 1:
            face_1 = 'Ace'
            elif card_1 == 2:
            face_1 =('Two')
            elif card_1 == 3:
            face_1 = ('Three')
            elif card_1 == 4:
            face_1 =('Four')        
            elif card_1 == 5:
            face_1 =('Five')        
            elif card_1 == 6:
            face_1 =('Six')       
            elif card_1 == 7:
            face_1 =('Seven')        
            elif card_1 == 8:
            face_1 =('Eight')        
            elif card_1 == 9:
            face_1 =('Nine')
            elif card_1 == 10:
            face_1 =('Ten')        
            elif card_1 == 11:
            face_1 =('Jack')        
            elif card_1 == 12:
            face_1 =('Queen')     
            elif card_1 == 13:
            face_1 =('King')
        card_2 = random.randint(1,13)

        #Print Players' names and cards
        print(Player_1, 'drew a', face_1)
        print(Player_2, 'drew a', face_2)

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
    
