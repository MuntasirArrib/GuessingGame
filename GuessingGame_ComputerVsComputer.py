import random

def machine_guess(x):
    low = 1
    high = x
    GuessingNumber = random.randint(low, high)
    print(f'Player 1 number is {GuessingNumber}')
    guess = 0

    while guess != GuessingNumber:
        if low != high:
            guess = random.randint(low,high)
            print(f'Player 2 guessed {guess}')
        else: 
            guess = high  
        if guess > GuessingNumber:
            high = guess - 1
            print(f"Too high, player2, now guess a number between {high} and {low}")
        elif guess < GuessingNumber:
            low = guess + 1
            print(f"too low, player2, now guess a number between {high} and {low}")
    print("Yay the game is over!")

        
machine_guess(10)
        