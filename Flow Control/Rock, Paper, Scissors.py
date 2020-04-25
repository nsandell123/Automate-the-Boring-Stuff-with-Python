# This is a program to play rock paper scissors
import random
#This variable determines whether to keep playing the game. 
userInput = "default"
#This variable holds the value of R, P, or S for the user
userToken = "default"
#This string is used to determine the winner of the game
playerIndex = "PRSP"
#This list stores one string that the computer randomly chooses
computerToken = []
#this is the string inside the list pulled out
updatedComputerToken = ""
#This counts how many times the user has played
counter = 0
userInput = input("Do you want to play a game of rock paper scissors? ")

while userInput == "yes":
    while any([not(isinstance(userToken, str)), userToken not in ("R", "S", "P")]):
        userToken = input("Please enter R for rock, S for scissors, and P for paper: ")
        counter+=1
    # after the user has entered the right one, make sure you get computer input
    computerToken = random.choices(playerIndex, [0.165, 0.33, 0.33, 0.165], k=1)
    updatedComputerToken = updatedComputerToken.join(computerToken)
    # return who won
    location = playerIndex.find(userToken)
    if updatedComputerToken == playerIndex[location + 1]:
        print("The computer has entered: " + updatedComputerToken)
        print("Congratulations, you won")
        userToken = "reset"
        userInput = input("Do you want to play again? ")
        if(userInput != "yes"):
            print("You have played " + str(counter) + " time(s)")
    elif userToken == updatedComputerToken:
        print("The computer has entered: " + updatedComputerToken)
        print("It is a tie")
        userToken = "reset"
        userInput = input("Do you want to play again? ")
        if(userInput != "yes"):
            print("You have played " + str(counter) + " time(s)")
    else:
        print("The computer has entered: " + updatedComputerToken)
        print("You have lost")
        userToken = "reset"
        userInput = input("Do you want to play again? ")
        if(userInput != "yes"):
            print("You have played " + str(counter) + " time(s)")

