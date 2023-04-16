import random

n = random.randint(1, 100)
t = 1

while n > 1:
    r = int(input("Guess a number between 1 and 100: "))
    if r > n:
        print("Too high, try again")
        t +=1
    if r < n:
        print("Too low, try again")
        t +=1
    if r == n:
        print(f"You got it! It only took you {t} times!")

