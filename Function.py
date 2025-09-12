#Python Function programs

#Write a function to add two numbers and return the result.

def add(a,b):
    
    return(a+b)

print(add(2,3))


#Write a function that takes a string and prints it in reverse.


def rev(word):

    print(word[::-1])
    
a = "Hello, World!"
rev(a)



#Write a function to find the square of a number.


def square(number):
    
    print(number*number)

a=int(input('enter a number'))
square(a)


#Write a function to check if a number is even or odd.

def even(number):
    
    if number%2==0:
        print("even number")
    else:
        print('odd number')
        
a=int(input('enter a number'))
even(a)



#Write a function to calculate the factorial of a number.

def fact(n):
    if n== 0 or n==1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

a=int(input("enter a number want sto find factorial: "))
print("factorial: ",fact(a))


# Functions with Parameters

# Write a function that takes a name as input and prints "Hello, <name>!".

d=str(input('enter a name:'))
def input(name):
    
    print( "Hello " + name)

input(d)


#Write a function that accepts a list and returns the sum of its elements.


def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum   

a = [1, 2, 3, 4, 5, 6, 7]
print(sum_list(a)) 




#Write a function that takes two numbers and returns the maximum.


def num(a,b):
    if a>b:
        return a
    else:
        return b
    

print(num(2,44))



#Write a function to check if a string is a palindrome.


def palindrome(a):
    if a == a[::-1]:
        print("Yes")
    else:
        print("No")
        
        
word='mala'
palindrome(word)



#Write a function to count the vowels in a given string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels('good morning'))



# Functions with Return Values

#Write a function to calculate the area of a circle given the radius.

def area(radius):
    pi=3.14
    return pi* radius *radius

print(area(2))


#Write a function that returns the largest element from a list.


def largest(num):
    large= num[0]   
    for i in num:
        if i > large:
            large = i
    return large

a = [1, 2, 3, 4, 5, 6, 7]
print("Largest element is:", largest(a))



#Write a function to check if a number is prime.


def prime(num):
    if num<2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(prime(5))



#Write a function to generate the Fibonacci series up to n terms.


def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = 7
print(f"Fibonacci series up to {n} terms:", fibonacci(n))




#Write a function to convert Celsius to Fahrenheit.

def fahrenheit(c):
    f = (9/5*c+32)
    return f

c = 23
print("celsius to fahrenheit.",fahrenheit(c))



