# VARIABLE - stores a single piece of data

#Syntax: name = data
score = 0
name = "Bob"
health = 5
pizza_topping = "pineapple"

# LOOPS - repeats code for a given amount of times or until a condition is met

# FOR LOOP - repeats code for a # of times

#Syntax: for i in range(#):
           #code here

# for = logic statement
# i = loop variables, labels which iteration we're on in the loop
# in  
# range(#) = a function that will repeat the loop for the number of times defined in the parenthesis.

# for i in range(4):
#   print("hello")

# for i in range(4):
#   print("bye")

# for i in range(4):
#   for i in range(5):
#     print("yikes")

#WHILE LOOP - will repeat code until a condition is met, or its condition turns false

# while pizza_topping == "pineapple":
#   for i in range(4):
#     print("yum")
#   print("cheese")
#   pizza_topping = "pepperoni"

#CONDITIONALS - if/else statements test of a condition is true then do an action, if it is not, do something else

#SYNTAX: 
# if - first condition to test
# elif - secondary condition to test, can have unlimited amount of elif
# else - the last condition to test
  
# num = input('give me a number: ')
# used integer function to turn num frm a string data type to an integer
# num = int(num)

# if num > 5:
#   print("greater than 5")
# elif num < 5:
#   print("less than 5")
# else:
#   print("equal to 5")

# Write a Python program to test if a number is positive or negative. The program will ask the user to input a number, then it will
# display what the number is.

num = int(input("provide a number: "))

if num > 0:
  print(str(num) + " is positive")
elif num < 0:
  print("negative")
else:
  print("zero")

