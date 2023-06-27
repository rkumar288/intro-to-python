# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.

import random

for number in range(10):
  print(random.random())

# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .

to_guess = 7

guess = None
while (guess != to_guess):
  guess = int(input("Enter a number ? "))

print("Wow lucky number 7!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre.
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.

width = int(input("Enter width of rectangle in cm ? "))
height = int(input("Enter height of rectangle in cm ? "))
area = (width * height)
print(
  str(width) + "cm" + " x " + str(height) + "cm" + " = " + str(area) + "cm2" +
  " = " + str(round(area / 10000)) + "m2")

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
#   If they get it wrong, print "Password failure" and then ask them to enter it again.
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".

guesses = 3
guess = None

count = 3
while guess != "qwerty123" and guesses > 0:
  password = input("Enter password ? ")
  if password == "qwerty123":
    print("You have successfully logged in")
    break
  else:
    print("Password failure")
  guesses -= 1

if guesses == 0:
  print("System Locked!")

# 5. Add up all the numbers from 1 to 500 and print the answer.

sum = 0
for number in range(1, 501):
  sum += number
print(sum)

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list.
#   Find the index at which the user entered the number 99.

list = []
for x in range(10):
  list.append(int(input("enter a number to add in list::")))
print(list.index(99))

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36

for x in range(1, 16):
  print(str(x) + " x " + "18" + " = " + str(x * 18))

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.

number = 1
while number < 101:
  print(number)
  number += 1

# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lessons = 3

while lessons > 0:
  lesson_name = input("enter name of lesson ")
  marks = int(input("enter marks of lesson "))

  if marks > 80:
    print(lesson_name + " is having grade A")
  elif marks >= 60 and marks <= 80:
    print(lesson_name + " is having grade B")
  elif marks >= 50 and marks < 60:
    print(lesson_name + " is having grade C")
  elif marks >= 45 and marks < 50:
    print(lesson_name + " is having grade D")
  elif marks >= 25 and marks < 45:
    print(lesson_name + " is having grade E")
  else:
    print(lesson_name + " is having grade F")

  lessons -= 1

# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name

import random

price_drawlist = []
person_to_add = None
while person_to_add != "":
  person_to_add = input("enter the name of people who entered a prize draw:: ")
  price_drawlist.append(person_to_add)

print("the winner is:: " + random.choice(price_drawlist))

# 11. Create a rock, paper, scissors game which is run against computer.
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice.
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games

import random

game_count = 3
user_won = 0
comp_won = 0
while (game_count > 0):
  user_choice = input("Choose rock, paper or scissors :: ").lower()
  computer_choice = random.choice(["rock", "paper", "scissors"])
  game_count -= 1

  if (user_choice == "rock"):
    if (computer_choice == "scissors"):
      user_won += 1
    else:
      comp_won += 1

  if (user_choice == "paper"):
    if (computer_choice == "rock"):
      user_won += 1
    else:
      comp_won += 1

  if (user_choice == "scissors"):
    if (computer_choice == "paper"):
      user_won += 1
    else:
      comp_won += 1

if (user_won == comp_won):
  print("its a draw")
elif user_won > comp_won:
  print("You won!!")
else:
  print("You lost!!")
