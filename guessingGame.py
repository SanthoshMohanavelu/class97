import random
number = random.randint(1,9)
guess = None  
chances = 0



while chances < 5:
    guess = int(input("Enter a number between 1 and 9: "))

    if guess < number:
        print("Your number is too low")
        chances += 1
    elif guess > number:
        print("Your number was too high")
        chances += 1
    else: 
        guess = number
        print("You got it correct")
    chances += 1

    if not chances < 5:
        print("You lose!!! the correct number is", number)




