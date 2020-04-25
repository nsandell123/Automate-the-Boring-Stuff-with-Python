#This is a program to play rock paper scissors

#Use a control structure to play as many times as the user desire
userInput = ""
playerIndex = ["PRSP"]
computerToken = ""
while(userInput != "no"):
    #Ask user for their token
    userToken = input("Please enter R for rock, S for scissors, and P for paper:  ")
    while(not(isinstance(userToken,str)) or userToken != "R" or userToken != "S" or userToken != "P"):
        userToken = print("Please enter R for rock, S for scissors, and P for paper: ")
    
    #Generate a random Token 
    print("Testing Testing Testing")
    #Compare the two 

    #return who won

    #ask the user if they want to play again

    #keep a counter to store number of losses and wins