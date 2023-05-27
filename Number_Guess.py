import random 
g = random.randrange(1,100)
u = 0

while u != g:
    u = int(input("Enter a number: "))

    if u > g:
        print("Your num is greater than generated number.")

    elif u < g:
        print("Your num is less than generated number.")

    elif u == g:
        print("Correct!")