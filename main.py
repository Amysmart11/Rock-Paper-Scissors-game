import random


comp_wins = 0
player_wins = 0

def Choose_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "R"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "P"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "S"
    else:
        print("Input invalid")
        Choose_option()
    return user_choice

def Computer_option():
    comp_choice = random.randint (1,3)
    if comp_choice == 1:
        comp_choice = "R"
    elif comp_choice == 2:
        comp_choice = "P"
    else:
        comp_choice = "S"
    return comp_choice

while True:
    print("")
    user_choice = Choose_option()
    comp_choice = Computer_option()
    print("")

    if user_choice == "R":
        if comp_choice == "R":
            print("You chose Rock. The computer chose Rock. It's a tie!")
        elif comp_choice == "P":
            print("You chose Rock. The computer chose Paper. You lose!")
            comp_wins += 1

        elif comp_choice == "S":
            print("You chose Rock. The computer chose Scissors. You win!")
            player_wins += 1        

    elif user_choice == "P":
        if comp_choice == "R":
            print("You chose Paper. The computer chose Rock. You win!")
            player_wins += 1
        elif comp_choice == "P":
            print("You chose Paper. The computer chose Paper. It's a tie!")
        elif comp_choice == "S":
            print("You chose Paper. The computer chose Scissors. You lose!")
            comp_wins += 1

    elif user_choice == "S":
        if comp_choice == "R":
            print("You chose Scissors. The computer chose Rock. You lose!")
            comp_wins += 1

        elif comp_choice == "P":
            print("You chose Scissors. The computer chose Paper. You win!")
            player_wins += 1
        elif comp_choice == "S":
            print("You chose Scissors. The computer chose Scissors. It's a tie!")
        
    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n): ")
    if user_choice in ("Y", "Yes", "y", "yes"):
        pass
    elif user_choice in ("N", "No", "n", "no"):
        break
    else:
        break
