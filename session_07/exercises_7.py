# # Session 7 Exercises

# ## Section A
# # 1. Write a function that prints your name


def hello():
  print("Hello !!")


hello()

# # 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".


def hello(name):
  print("Hello " + name + "!!")


hello("Rakesh")

# # 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.


def hello(name):
  print("Hello " + name + "!!")


list = ["Alice", "Bob", "Charlie"]
for x in list:
  hello(x)


# # 4. Write a function that prints the area of two passed in parameters.
def area(x, y):
  print("area is " + str(x * y))


area(3, 4)
area(5, 6)

# # 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.


def print_list(inputList):
  for x in inputList:
    print("item is " + x)


print_list(["Alice", "Bob", "Charlie"])

# # 6. Put the following into a function that accepts age as a parameter:
# #     1. If they are younger than 11, print "You're too young to go to this school".
# #     2. If they are between 11 and 16, print "You can can come to this school".
# #     3. If they are over 16, print 'You're too old for school".
# #     4. If they are 0, print "You're not born yet!".


def ageCheck(x):
  if x == 0:
    print("You're not born yet!")
  elif x < 11:
    print("You're too young to go to this school")
  elif x >= 11 and x <= 16:
    print("You can can come to this school")
  else:
    print("You're too old for school")


ageCheck(0)
ageCheck(7)
ageCheck(14)
ageCheck(21)

# # <---------------------------------------------------------------------------------------------->

# ## Section B
# # 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).


def oddCheck(x):
  if x % 2 == 0:
    return False
  else:
    return True


number = int(input("Enter number:: "))
if oddCheck(number):
  print("this number is odd")
else:
  print("this number is even")

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.


def reverse(str):
  return str[::-1]


word = input("Enter word :: ")
print(reverse(word))

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```


def recursiveFunc(n):
  print('*' * n)
  if n > 1:
    recursiveFunc(n - 1)


number = int(input("Enter number :: "))
recursiveFunc(number)

# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".


def padlock(str):
  if (str == "passcode"):
    return "Unlock"
  else:
    return "Locked"


password = input("Enter password :: ")
print(padlock(password))

# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.


def multiples_3_and_5(limit):

  sum = 0

  for i in range(0, limit + 1):
    if limit < 0:
      print("The limit must be greater than 0")
    if i % 3 == 0:
      sum += i
      print(sum)
    elif i % 5 == 0:
      sum += i
      print(sum)


number = int(input("Enter number :: "))
print(multiples_3_and_5(number))

# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.


def is_prime(num):
  count = 0

  for i in range(2, num):
    if (num % i == 0):
      count = count + 1
      break

  if (count == 0 and num != 1):
    print(str(num) + " is a Prime Number")
    return True
  else:
    print(str(num) + " is not a Prime Number")
    return False


is_prime(6)
is_prime(99)
is_prime(83)

# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.


def pallindrome(word):
  reverse_word = word[::-1]
  if word == reverse_word:
    print(True)
  else:
    print(False)


pallindrome("strognsgag")
pallindrome("abba")

# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not.
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.


def pallindrome_sen(sentence):
  formatted_sen = sentence.lower()
  new_sentence = formatted_sen.replace(' ', '')
  rev_sentence = new_sentence[::-1]
  if new_sentence == rev_sentence:
    print(True)
  else:
    print(False)


pallindrome_sen("The cat sat on the mat")
pallindrome_sen("A nut for a jar of tuna")
