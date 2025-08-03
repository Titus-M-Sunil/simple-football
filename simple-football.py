import random

# Number of times player/computer has passed the ball
passCount = 0

# Asks for user input to decide if they choose odd/even
userOddEven = input('Choose odd/even: ')
print('You chose', userOddEven)

# Asks for number input to decide if the outcome is odd/even
userInput = int(input('\nEnter a number (1-4): '))

# Computer number input is chosen randomly
computerInput = random.randint(1, 4)
print('Computer chose', computerInput)

# Calculation to check is sum of computer and player input is odd/even
calculation = (computerInput + userInput) % 2