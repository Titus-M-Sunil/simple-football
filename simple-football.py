import random

# Number of times player/computer has passed the ball
passCount = 0

# User input to choose odd/even
userOddEven = input('Choose odd/even: ')
print('You chose', userOddEven)

# Number input (from 1 to 4) to decide if the outcome is odd/even
userInput = int(input('\nEnter a number (1-4): '))

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