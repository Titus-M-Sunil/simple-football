import random

# Number of times player/computer has passed the ball
passCount = 0
userOddEven = ""

# User input to choose odd/even
while (userOddEven == ""):
    userOddEven = input('Choose odd/even: ')
    if (userOddEven == "odd" or userOddEven == "even"):
        break
    else:
        print("Invalid input.\n")
        userOddEven = ""

print('You chose', userOddEven)

# Number input function (from 1 to 4) 
def userInputFunction():
    userInput = 0
    while (userInput == 0 or userInput == ""):
        try:
            userInput = input('\nEnter a number (1-4): ')
            if (int(userInput) > 0 and int(userInput) < 5):
                return int(userInput)
            else:
                print("Invalid input, you can only choose number 1 to 4.")
                userInput = 0
        except ValueError:
            print("Invalid input! You must enter a number.")

userInput = userInputFunction()

# Computer number input (from 1 to 4) is chosen randomly
computerInput = random.randint(1, 4)
print('Computer chose', computerInput)

# Calculation to check if sum of computer and player input is odd/even
calculation = (computerInput + userInput) % 2

def footOrBallSelection():
    if (calculation == 0): # even
        print('Outcome was even')
        if (userOddEven == 'even'):
            userFootBall = input('You get to play first. Choose (foot/ball): ')
            # print(userFootBall)
            return userFootBall
        elif (userOddEven == 'odd'):
            print('Computer plays first.')
            return 'BALL'
        
    elif (calculation != 0): # odd
        print('Outcome was odd')
        if (userOddEven == 'even'):
            print('Computer plays first.')
            return 'BALL'
        elif (userOddEven == 'odd'):
            userFootBall = input('You get to play first. Choose (foot/ball): ')
            # print(userFootBall)
            return userFootBall
        
def playerStartGame(passCount): # When player has the ball
    playerHasBall = True
    while(True):
        playerPassBall = userInputFunction()
        computerPassBall = random.randint(1, 4)
        print('computer pass =', computerPassBall)
        if (playerPassBall == computerPassBall):
            passCount = 0
            print('Computer received the ball.')
            computerStartGame(passCount)
        elif (playerPassBall != computerPassBall):
            passCount += 1
            print(f"{passCount} pass successful.")
            if (passCount == 4):
                print('Time to score a goal for the player.')
                passCount = 0
                scoreGoal(playerHasBall)
            continue

def computerStartGame(passCount): # When computer has the ball
    playerHasBall = False
    while(True):
        playerPassBall = userInputFunction()
        computerPassBall = random.randint(1, 4)
        print('computer pass =', computerPassBall)
        if (playerPassBall == computerPassBall):
            passCount = 0
            print('Player received the ball.')
            playerStartGame(passCount)
        elif (playerPassBall != computerPassBall):
            passCount += 1
            print(f"{passCount} defense unsuccessful.")
            if (passCount == 4):
                print('Time to score a goal for the computer.')
                passCount = 0
                scoreGoal(playerHasBall)
            continue

def scoreGoal(playerHasBall): # After the player or computer has reached 4 passes
    if (playerHasBall):
        playerPassBall = int(input('\nEnter a number (5 or 6): '))
        computerPassBall = random.randint(5, 6)
        print('computer pass =', computerPassBall)
        if (playerPassBall != computerPassBall):
            print('You have scored a GOAAALLLLL!!!')
            displayScore(True)
            computerStartGame(passCount)
        elif (playerPassBall == computerPassBall):
            print('The ball was saved by the computer.')
            computerStartGame(passCount)
            
    elif (not playerHasBall):
        playerPassBall = int(input('\nEnter a number (5 or 6): '))
        computerPassBall = random.randint(5, 6)
        print('computer pass =', computerPassBall)
        if (playerPassBall != computerPassBall):
            print('Computer has scored a GOAAALLLLL!!!')
            displayScore(False)
            playerStartGame(passCount)
        elif (playerPassBall == computerPassBall):
            print('The ball was saved by the player.')
            playerStartGame(passCount)
   
score = {
    'player': 0,
    'computer': 0
}

def displayScore(point): # Updation of score after goal
          
    if (point):
        score["player"] += 1
    elif (not point):
        score["computer"] += 1
        
    print(score)
    
selection = footOrBallSelection()
if (selection == 'ball'):
    print('Player has the ball.')
    playerStartGame(passCount)
elif (selection == 'BALL' or selection == 'foot'):
    print('Computer has the ball.')
    computerStartGame(passCount)