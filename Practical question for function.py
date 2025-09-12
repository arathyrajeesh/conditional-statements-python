
#Write a function to find the grade of a student from marks.

def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

marks = int(input("Enter marks: "))
print("Grade:", grade(marks))




#Write a function to check if a given year is a leap year.

def leap_year(year):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        print(f'{year} is leap year')
    else:
        print('not leap year')
        
        
years = int(input("Enter year: "))
leap_year(years)



#Write a function that accepts a list of numbers and returns only the even numbers.


def even_numbers(list):
    evens = []
    for i in list:
        if i % 2 == 0:
            evens.append(i)
    return evens

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:", even_numbers(a))


#Write a function to calculate simple interest.

def interest(principal, rate, time):
    a = (principal * rate * time) / 100
    return a

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

print("Simple Interest:", interest(p, r, t))


#Write a function that simulates a calculator (add, subtract, multiply, divide).

def calculator(a, b, operator):
    
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "not Divided by zero!"
    else:
        return "Invalid operator!"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print("Result:", calculator(num1, num2, op))



