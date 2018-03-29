print("Welcome to Test Your Knowledge!\n")
name = input("What is your name?: ").title()
print("\nHello " + name + ", I hope you will enjoy this short quiz!\n")
print("The rules are very simple.\nThere are three choices for each question."
      "\nYou should select the letter corresponding to the correct answer."
      "\nYou only get one attempt at the answer, so think carefully."
      "\nGood luck!\n\n")

score = 0

print("1. How many days are there in an average year?:\n")
print("A. 365")
print("B. 366")
print("C. 360")
print("")

number1 = "A"
response1 = input("Your answer: ").upper()

if response1 != number1:
    print("That is incorrect!")
else:
    print("Well done! " + response1 + " is the correct answer.")
    score = score + 1

print("Your current score is " + str(score) + " out of 3.\n")

print("2. Which is the coolest programming language in the universe?:\n")
print("A. PhP")
print("B. Python")
print("C. Other")
print("")

number2 = "B"
response2 = input("Your answer: ").upper()

if response2 != number2:
    print("That is incorrect!")
else:
    print("Well done! " + response2 + " is the correct answer.")
    score = score + 1

print("Your current score is " + str(score) + " out of 3.\n")

print("3. Which country will rise like a phoenix?:\n")
print("A. Russia")
print("B. Qatar")
print("C. Zimbabwe")
print("")

number3 = "C"
response3 = input("Your answer: ").upper()

if response3 != number3:
    print("That is incorrect!")
else:
    print("Well done! " + response3 + " is the correct answer.")
    score = score + 1

print("Your total score is " + str(score) + " out of 3.")
if score > 2:
    print("That is excellent stuff!")
elif score > 1:
    print("Very good!")
else:
    print("You can certainly do better!")

print("\nThank you for playing!")
