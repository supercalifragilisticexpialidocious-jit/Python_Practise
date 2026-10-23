# #question 5 : WAP to input user's first name and print its length.

first_name = input("Enter your first name: ")
print(len(first_name))

#question 6 : WAP to find the occurence of '$' in a string.

str = "Hi, I have $100 in my wallet. Do you have any $?"
count = str.count('$')
print("The occurrence of '$' in the string is:", count)

#question 7 : WAP to check if a number entered by the user is even or odd.

num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")

#question 8 : WAP to find the greatest of three numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if(num1 >= num2 and num1 >= num3):
    print("The greatest number is:", num1)
elif(num2 >= num1 and num2 >= num3):
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)

#question 9 : WAP to check if a number is a multiple of 7 or not.

num = int(input("Enter a number: "))
if(num % 7 == 0):
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")