import random

def guessing_game():
    print("Guess a no. from 1 to 100")
    num_to_guess = random.randint(1,100)
    attempt = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempt += 1
            if guess < num_to_guess:
                print("Too Low")
            elif guess > num_to_guess:
                print("Too High")
            elif guess == num_to_guess:
                print("Perfect")
        except:
            print("enter a valid number")        

guessing_game()