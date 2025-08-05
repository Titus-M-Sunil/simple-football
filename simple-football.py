"""
===================================================== GAME RULES =====================================================
1. User is asked to choose odd or even.
2. If the outcome was equal to User's choice, they receive the ball.
3. If the outcome was the opposite, Computer receives the ball.
4. After the game has started, User and Computer gets to choose numbers 1 to 4.
5. When the choices of User and Computer does not match, the ball is passed to the next player of respective team.
6. When the choices of User and Computer is equal the ball is blocked and is received by who did not have the ball.
7. The ball can be passed upto four times by either teams after which it is time to score the goal.
8. At the time of goal scoring the number choices is reduced to only 5 or 6 as the inputs.
9. This means there is always a 50/50 chance to score a goal.
10. When the User scores a goal, the scoreboard is updated and the game restarts with ball belonging to Computer.
11. Vice versa if the Computer scores a goal.
12. When the User's ball is saved by the Computer, game restarts with ball belonging to Computer.
13. Vice versa if the User saves a goal.
======================================================================================================================
"""

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

# Function for choosing who gets the ball first
def footOrBallSelection():
    if (calculation == 0): # even
        print('Outcome was even')
        if (userOddEven == 'even'):
            print('You get the ball first.')
            return 'ball'
        elif (userOddEven == 'odd'):
            print('Computer gets the ball first.')
            return 'BALL'
        
    elif (calculation != 0): # odd
        print('Outcome was odd')
        if (userOddEven == 'even'):
            print('Computer gets the ball first.')
            return 'BALL'
        elif (userOddEven == 'odd'):
            print('You get the ball first.')
            return 'ball'

# When player has the ball 
def playerStartGame(passCount): 
    playerHasBall = True
    while(True):
        playerPassBall = userInputFunction()
        computerPassBall = random.randint(1, 4)
        print('Computer choice =', computerPassBall)
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

# When computer has the ball
def computerStartGame(passCount): 
    playerHasBall = False
    while(True):
        playerPassBall = userInputFunction()
        computerPassBall = random.randint(1, 4)
        print('Computer choice =', computerPassBall)
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
        print('Computer choice =', computerPassBall)
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
        print('Computer choice =', computerPassBall)
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
    playerStartGame(passCount)
elif (selection == 'BALL'):
    computerStartGame(passCount)