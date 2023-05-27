print("Welcome to my computer quiz!")

playing = input("Do you want to play this game? (y/n)")

s = 0

if playing != "y":
    quit()

print("Ok Let's continue! ")

q1 = input("What is the capital of Telangana? ")
if q1 == "hyderabad":
    print("Correct! You've been awarded with a point!")
    s = s+1
else:
    print("Wrong answer. No Points.")

q2 = input("What is the capital of AP? ")
if q2 == "vizag":
    print("Correct! You've been awarded with a point!")
    s = s+1
else:
    print("Wrong answer. No Points.")

q3 = input("What is the capital of Maharashtra? ")
if q3 == "mumbai":
    print("Correct! You've been awarded with a point!")
    s = s+1
else:
    print("Wrong answer. No Points.")



print("Game Over!")
print(f"Your total score is {s}")