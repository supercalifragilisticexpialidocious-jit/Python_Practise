# question 1 : Write a program to add two numbers entered by user.
a = int(input("Enter a : "))
b = int(input("Enter b : "))

print("The sum of a and b is:", a + b)

#question 2 : Write a progra to input side of a square and find area.

side = float(input("Enter the side of square: "))

area = side * side
print("The area of square is:", area)

#question 3 : WAP to input 2 floating point numbers and find their average.

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
average = (num1 + num2) / 2
print("The average of", num1, "and", num2, "is:", average)

#question 4 : WAP to input 2 int numbers, a and b. print true if a is greater than or equal to b, if not print false.

a = int(input('a : '))
b = int(input('b : '))

print(a >= b)
