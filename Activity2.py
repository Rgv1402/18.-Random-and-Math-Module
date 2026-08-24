import random

while True:
    user_action = input("Enter Rock, Paper or Scissor: ").lower().strip()
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, and the computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players chose {user_action}! It's a tie")
    elif user_action == "rock":
        if computer_action == "scissor":
            print("Rock smashes scissors! You win!!")
        else:
            print("Paper covers rock. You lose!")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("Scissor cuts Paper! You win!!")
        else:
            print("Rock smashes scissor. You lose!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!!")
        else:
            print("Scissor cuts paper. You lose!")
    else:
        print("Invalid choice. Try again\n")
        continue

    play_again = input("Play again (y/n): ")
    if play_again != "y":
        break