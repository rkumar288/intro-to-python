# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".

name = input("What is your name ? ")
if (name == "Bob"):
  print("Welcome Bob!")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

name = input("What is your name ? ")
if (name != "Alice"):
  print("You're not Alice!")

# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in".
#   If they get it wrong, print "Password failure".

password = input("enter the password ")
if (password == "qwerty123"):
  print("You have successfully logged in")
else:
  print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

number = int(input("enter the number "))
if (number % 2 == 0):
  print("Even")
else:
  print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

number1 = int(input("enter ist number "))
number2 = int(input("enter second number "))
if (number1 + number2 > 21):
  print("Bust")
else:
  print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

length = int(input("enter the length "))
width = int(input("enter the width "))
if (length == width):
  print("square")
else:
  print("not square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years.
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

current_salary = int(input("enter the current_salary "))
years_of_exp = int(input("enter the years_of_exp "))
if (years_of_exp > 3):
  print("current_salary is ::" + str(current_salary) + " and bonus is :: " +
        str(current_salary * 0.1))
else:
  print("No bonus")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.

whole_number = int(input("enter the whole number "))
if (whole_number >= 0):
  print(whole_number * 3)
else:
  print(whole_number / 2)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob",
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

name = input("enter your name ")
if name == "Alice":
  print("Hello, Alice")
elif name == "Bob":
  print("You're not Bob! I'm Bob")
else:
  print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

age = int(input("enter your age "))
if age == 0:
  print("You're not born yet!")
elif age < 11:
  print("You're too young to go to this school")
elif age >= 11 and age <= 16:
  print("You can can come to this school")
else:
  print("You're too old for school")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

month = input("enter current month ")
if month == "March" or month == "April" or month == "May":
  print(month + " is in Spring")
elif month == "June" or month == "July" or month == "August":
  print(month + " is in summer")
elif month == "September" or month == "October" or month == "November":
  print(month + " is in Autumn")
elif month == "December" or month == "January" or month == "February":
  print(month + " is in Winter")
else:
  print("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

number1 = int(input("enter ist number "))
number2 = int(input("enter 2nd number "))
if number1 % 2 == 0 and number2 % 2 == 0:
  print("Both numbers are even")
elif number1 % 2 != 0 and number2 % 2 != 0:
  print("Both numbers are odd")
else:
  print("product of the two numbers is:: " + str(number1 * number2))

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

number1 = int(input("enter ist number "))
number2 = int(input("enter 2nd number "))
if number1 > number2:
  print("number1 is highest with value::" + str(number1))
elif number2 > number1:
  print("number2 is highest with value::" + str(number2))
else:
  print("both are equal")

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years,
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years.
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

current_salary = int(input("enter the current_salary "))
years_of_exp = int(input("enter the years_of_exp "))
if (years_of_exp > 7):
  print("current_salary is ::" + str(current_salary) + " and bonus is :: " +
        str(current_salary * 0.2))
elif (years_of_exp > 5):
  print("current_salary is ::" + str(current_salary) + " and bonus is :: " +
        str(current_salary * 0.15))
elif (years_of_exp >= 3 and years_of_exp <= 5):
  print("current_salary is ::" + str(current_salary) + " and bonus is :: " +
        str(current_salary * 0.1))
else:
  print("No bonus")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest.
#   If all three ages are the same, print that.

name1 = input("enter name of person1 ")
age1 = int(input("enter age of person1 "))
name2 = input("enter name of person2 ")
age2 = int(input("enter age of person2 "))
name3 = input("enter name of person3 ")
age3 = int(input("enter age of person3 "))

if age1 > age2 and age1 > age3:
  print(name1 + " is oldest with age " + str(age1))
elif age2 > age1 and age2 > age3:
  print(name2 + " is oldest with age " + str(age2))
elif age3 > age1 and age3 > age2:
  print(name3 + " is oldest with age " + str(age3))
else:
  print("three ages are the same")

if age1 < age2 and age1 < age3:
  print(name1 + " is youngest with age " + str(age1))
elif age2 < age1 and age2 < age3:
  print(name2 + " is youngest with age " + str(age2))
elif age3 < age1 and age3 < age1:
  print(name3 + " is youngest with age " + str(age3))
else:
  print("three ages are the same")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson1 = input("enter name of lesson 1 ")
marks1 = int(input("enter marks of lesson 1 "))
lesson2 = input("enter name of lesson 2 ")
marks2 = int(input("enter marks of lesson 2 "))
lesson3 = input("enter name of lesson 3 ")
marks3 = int(input("enter marks of lesson 3 "))

if marks1 > 80:
  print(lesson1 + " is having grade A")
elif marks1 >= 60 and marks1 <= 80:
  print(lesson1 + " is having grade B")
elif marks1 >= 50 and marks1 < 60:
  print(lesson1 + " is having grade C")
elif marks1 >= 45 and marks1 < 50:
  print(lesson1 + " is having grade D")
elif marks1 >= 25 and marks1 < 45:
  print(lesson1 + " is having grade E")
else:
  print(lesson1 + " is having grade F")

if marks2 > 80:
  print(lesson2 + " is having grade A")
elif marks2 >= 60 and marks2 <= 80:
  print(lesson2 + " is having grade B")
elif marks2 >= 50 and marks2 < 60:
  print(lesson2 + " is having grade C")
elif marks2 >= 45 and marks2 < 50:
  print(lesson2 + " is having grade D")
elif marks2 >= 25 and marks2 < 45:
  print(lesson2 + " is having grade E")
else:
  print(lesson2 + " is having grade F")

if marks3 > 80:
  print(lesson3 + " is having grade A")
elif marks3 >= 60 and marks3 <= 80:
  print(lesson3 + " is having grade B")
elif marks3 >= 50 and marks3 < 60:
  print(lesson3 + " is having grade C")
elif marks3 >= 45 and marks3 < 50:
  print(lesson3 + " is having grade D")
elif marks3 >= 25 and marks3 < 45:
  print(lesson3 + " is having grade E")
else:
  print(lesson3 + " is having grade F")
