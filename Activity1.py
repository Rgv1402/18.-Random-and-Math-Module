import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number from 0-9 and you have to guess it!")

while playing:
    guess = (input("Enter your guess (0-9): "))
    if guess == number:
        print("You've won the game!!")
        print("The number was", number)
        break
    else:
        print("Try again! Wrong guess!\n")
        
