# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable.
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
width = 10
height = 15
area = width * height

print("Rectangle of width " + str(width) + " and height " + str(height) +
      " has an area of " + str(area))

# 2. Write code that prints the length of the string, 'python'.
print(len("python"))

# 3. Print out the first and third letter of the word 'python'.
print("python"[0])
print("python"[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name = input("What is your name ? ")
print("Hello, " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = input("Enter your age ? ")
age_after_15_years = int(age) + 15
print("In 15 years age will be : " + str(age_after_15_years))

# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old.
#   In 15 years time you will be <age_in_15_years_time>`.

# name = input("What is your name ? ")
# age = input("Enter your age ? ")
age_after_15_years = int(age) + 15
print("Hello, " + name + " you are currently " + age +
      " years old and In 15 years age will be : " + str(age_after_15_years))

# 7. Ask the user to enter their hometown, print it out in uppercase letters.

hometown = input("What is your hometown ? ")
print(hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

colour = input("What is your favourite colour ? ")
print(len(colour))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
month = input("Which month it is ? ")
weather = input("How is the weather ? ")
print("It is " + month + " and it is" + weather + " today")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string:
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
month = input("which month it is ? ")
temp1 = int(input("Enter temperatures entry 1 : "))
temp2 = int(input("Enter temperatures entry 2 : "))
temp3 = int(input("Enter temperatures entry 3 : "))
temp4 = int(input("Enter temperatures entry 4 : "))
temp5 = int(input("Enter temperatures entry 5 : "))
average_temperature = temp1 + temp2 + temp3 + temp4 + temp5 / 5
print("It is " + month + " and the average temperature is " +
      str(average_temperature) + " degrees celsius")

# 11. Print out the above sentence but make the month upper case.

print("It is " + month.upper() + " and the average temperature is " +
      str(average_temperature) + " degrees celsius")

# 12. Create a variable that holds your favourite animals and print it out.
#    Make sure the animals are all on different lines and tabbed.
animals = 'sparrow parrot birds'

# 13. Ask the user to enter their name as well as a number.
#    Print out the uppercase character at that position in the string.

name = input("What is your name? ")
number = int(input("choose one number ? "))
print(name[number].upper())

# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
string = 'WelcometoPython'
print(len(string))
print(string[1:14:2])
