def game():
    import random 

    print("Welcome to Rock Paper Scissors game in Python!")
    options = ("rock","paper","scissors")

    user = None 
    computer = random.choice(options)


    while user not in options:
        user = input("Enter your choice in R/P/S- ")

    print(f"Player : {user}")
    print(f"Computer : {computer}")

    if computer == user:
        print("It's a tie! ")

    if computer == "rock":
        if user == "paper":
            print("User Wins!")
        elif user == "scissors":
            print("Computer Wins!")

    if computer == "paper":
        if user == "rock":
            print("Computer Wins!")
        elif user == "scissor":
            print("User Wins!")

    if computer == "scissor":
        if user == "paper":
            print("Computer Wins!")
        elif user == "rock":
            print("User Wins!")

print("Do you want to play this game? y/n ")
choice = input("Enter y/n ")
if choice == "y":
    game()
else:
    quit()