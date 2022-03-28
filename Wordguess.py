import random
import math

lower = int(input("Enter Lowest number u want to guess form:- "))
upper = int(input("Enter Higest number u want ot guess form:- "))

limit = random.randint(lower, upper)
print("\n\t You got only ", round(math.log(upper - lower + 1, 2)),
      " chances to guess that number! What is that number!\n", limit)

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number : "))

    if limit == guess:
        print(" NO! u beat me in  ", count, " tries :==(")
        break

    if limit == guess + 1:
        print("You'r very close")

    if limit == guess - 1:
        print("You'r very close")

    elif limit > guess:
        print("You guessed too small! Try a higher number --")
    elif limit < guess:
        print("You Guessed too high! Try a lower number ++")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number was %d" % limit)
    print("\t HEHEH! u lost. Play it once more to win, which u won't 😏")
