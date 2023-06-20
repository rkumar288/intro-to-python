# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.

fruits = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(fruits)

# 2. Add "Grapes" to the list and print the list.

fruits.append("Grapes")
print(fruits)

# 3. Change "Pears" to "Strawberries" and print the list.
fruits[2] = "Strawberries"
print(fruits)

# 4. Remove "Apples" from the list and print the list.
del (fruits[0])
print(fruits)

# 5. Print out the current length of the list.
#print(len(fruits))
# 6. Order the list alphabetically.
fruits.sort()

# 7. Print out the list again.
print(fruits)
# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
for x in fruits:
  print(x)

#2. Print the numbers 1 to 100 (including the number 100).
print("number 1 to 100")
for number in range(1, 101):
  print(number)

# 3. Print all odd numbers from 1 to 100.
print("odd number 1 to 100")
for number in range(1, 101):
  if (number % 2):
    print(number)

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
print("The modern olympics started in 1896")
not_held = [1916, 1940, 1944, 2020]
for olympics_year in range(1896, 2023, 4):
  if (olympics_year not in not_held):
    print(olympics_year)

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
list = [1, 3, 2, 4, 5, 7, 9, 12, 17, 19]
even_count = 0
odd_count = 0
for x in list:
  if (x % 2):
    odd_count = odd_count + 1
  else:
    even_count = even_count + 1

print("even_count is ::" + str(even_count))
print("odd_count is ::" + str(odd_count))

# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.

list = ["Rakesh", "Raheja", "Sonu", "Raks", "Engineer"]
for x in list:
  print("Hello " + x)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
str = "supercalifragilisticexpialidocious"
for i in range(len(str)):
  print(str[i])

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.

numbers_list = [1, 2, 3, 4, 5]
list2 = []
for number in numbers_list:
  list2.append(number * number)
print(list2)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.

list = ["Rakesh", "Raheja", "Sonu", "Raks", "Engineer"]
dr_list = []
for x in list:
  dr_list.append("Dr. " + x)
print(dr_list)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz".
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```

for number in range(1, 101):
  if (number % 3 == 0 and number % 5 == 0):
    print("FizzBuzz")
  elif (number % 3 == 0):
    print("Fizz")
  elif (number % 5 == 0):
    print("Buzz")
  else:
    print(number)
