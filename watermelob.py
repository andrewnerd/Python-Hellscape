import Andrewnerd
import time
import random
import math

min = random.randrange(1, 100)
max = random.randrange(min + 1, min * 10)
x = random.randrange(min, max)



answer = int(input(f"IM thinking of a NUMBER from {min} to {max}. WHAT IS IT? : "))
before = time.time()

while answer != x:
    if answer / x < 0.1 or answer / x > 10:
        print("you arent ANYWHERE CLOSE LOL try agian")
    elif answer > x:
        print("guess a SMALLER number")
    elif answer < x:
        print("guess a MORE LARGER number")

    answer = int(input("try again: "))

after = time.time()
time_passed = round(after - before, 3)
print(f"You guessed the number in {time_passed} seconds!!!!")