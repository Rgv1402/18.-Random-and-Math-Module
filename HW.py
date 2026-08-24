import random
import math
lucky_number = str(random.randint(1,10))
print("Your lucky number today is", lucky_number)

fun_choices = ["Reading", "Board Games", "Cycling", "Video Games", "Sports", "Spend time with Family/Friends"]
print("\nRandom fun thing to do today- ")
print(random.choice(fun_choices))
print()

secret_number = str(random.randint(1,5))
while True:
    guess = input("Guess the number!!(1-5): ")
    if guess == secret_number:
        print('You guessed RIGHT!!!\n')
        break
    else:
        print("Try again!\n")
        continue

num = float(input("Enter a decimal- "))

print(f"{num} rounded up is {math.ceil(num)}")
print(f"{num} rounded down is {math.floor(num)}")

num1 = int(input("\nEnter an integer - "))
num2 = int(input("Enter another negative integer - "))

print("\nBefore: ", num1, "and", num2)
print("After: ", math.copysign(num1,num2))

print("\nBefore: ", num2)
print("After: ", math.fabs(num2))

num01 = int(input("\nEnter an integer for GCD- "))
num02 = int(input("Enter another integer for GCD - "))

print("\nNumbers: ", num01, ",", num02)
print("GCD: ", math.gcd(num01,num02))





