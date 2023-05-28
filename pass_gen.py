import random
def pas():
    print("Welcome to the password generator!")
    print("An ideal password should contain characters, numbers and special characters.")
    sc = ("!","@","#")
    scp = random.choice(sc)

    c = ("a","b","c","d","e")
    c1 = random.choice(c)
    c2 = random.choice(c)
    c3 = random.choice(c)

    n = ("1","2","3","4","5","6","7","8")
    n2 = random.choice(n)
    n3 = random.choice(n)
    n1 = random.choice(n)
    n4 = random.choice(n)

    p0 = c1+c2+c3+n1+n2+n3+n4+scp

    print(f"Your special generated password is {p0}")

m = input("Do you want to generate a password? y/n ")
if m == "y":
    pas()
elif m == "n":
    quit()
else:
    print("Invalid choice")
    