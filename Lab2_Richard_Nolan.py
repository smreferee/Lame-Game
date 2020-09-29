################################################
#This is Lab 2 for COSC 1336 by Richard Nolan  # 
#The program will display program information, # 
#ask and display the user name, display a menu,#
#and finally confirm the menu choice.          #
################################################

#Introduction to the program
print('Hi! Welcome to the Lame Game!')
print("This is the introduction, where you'll be asked your name.")
print('Finally, you will select a menu option, and that choice will be confirmed.')


#Username query
name = input('What is your name? ')
print (name)

#Game Menu
print("GAME MENU")
choice = int(input('1.Make Change\
             2.High Card\
             3.Quit\
            Choice:'))


#Menu Choice Response
print(name,', you chose menu option ',choice,".", sep='');
