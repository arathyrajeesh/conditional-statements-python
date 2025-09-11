#For Loop 

#Write a program to print numbers from 1 to 10 using a for loop.

for x in range(11):
    print(x)
    
    
#Write a program to print the multiplication table of a given number.

a=int(input('enter a number : '))

print(f"\nMultiplication Table of {a}")
for i in range(1, 11):
    print(f"{a} x {i} = {a * i}")
    
    
#Write a program to print all even numbers from 1 to 50.

for x in range(50):
    if x%2==0:
        print(f'{x}',end=" ")


#Write a program to calculate the sum of numbers from 1 to 100 using a for loop.

sum = 0

for i in range(1, 101):
    sum += i

print("\nThe sum of numbers from 1 to 100 is:", sum)


#Write a program to print the square of numbers from 1 to 10.


for i in range(1, 11):
    print(f"The square of {i} is {i*i}")


#while loop

#Write a program to print numbers from 10 down to 1 using a while loop.

num = 10

while num >= 1:
    print(num)
    num -= 1
    
    
#Write a program to calculate the factorial of a given number using a while loop.

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is: {factorial}")




#Write a program to print the first 10 natural numbers using a while loop.

num = 1

while num <= 10:
    print(num)
    num += 1
    
    


#Write a program to reverse a given number using a while loop.

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10         # Get the last digit
    reverse = reverse * 10 + digit  # Append digit to reversed number
    num //= 10               # Remove the last digit

print("Reversed number is:", reverse)




#Write a program to find the sum of digits of a given number using a while loop.

num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10        # find the last digit
    sum_digits += digit     # Add digit to sum
    num //= 10              # Remove the last digit

print("The sum of digits is:", sum_digits)




#Nested For Loop

#Write a program to print a right-angled triangle pattern of * with 5 rows.

rows = 5

for i in range(1, rows + 1):
    for j in range(1,i+1):
        print(end="*")
    print()
    
    



#Write a program to print a multiplication table from 1 to 5 using nested for loops.

for i in range(1, 6):  #for numbers 1 to 5
    print(f"\nMultiplication Table of {i}:")
    for j in range(1, 11):  # for 1 to 10
        print(f"{i} x {j} = {i * j}")




#Write a program to print a square pattern of numbers (1 to 5).

n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()  



#Write a program to print a pyramid pattern of *

rows = 5

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()  


#Write a program to print numbers in triangular form

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  
    
    
    
    
#Break Statement 

#Write a program to print numbers from 1 to 10, but stop if the number is 5.

for num in range(1, 11):
    if num == 5:
        break   
    print(num)
    
    
    
#Write a program to search for a given digit in a number; stop when found.


digit = int(input("Enter a digit: "))
search = int(input("Enter a number to search: "))

found = False

while digit > 0:
    num = digit % 10   
    if num == search:
        print("Item found")
        found = True
        break          
    digit //= 10

if not found:
    print("Item not found")

    
# Write a program to read characters from a string and stop when a is found.

word = input("Enter a string: ")

for char in word:
    if char == 'a':
        print("Found 'a' ")
        break
    print(char)
    
    
    
#Write a program to print a multiplication table of 7 but stop when the result exceeds 50.

num = 7
for i in range(1, 11):  
    result = num * i
    if result > 50:      
        break
    print(f"{num} x {i} = {result}")



#Write a program to find the first divisor of a number (greater than 1).

num =int(input('enter a number'))

for i in range(2,num+1):
    if num%i==0:
        print(i)
        break
    

#Continue Statement

#Write a program to print numbers from 1 to 10 but skip 5.

for num in range(1, 11):
    if num == 5:
        continue   
    print(num)
    
    
    
    
#Write a program to print all numbers from 1 to 20 except even numbers.

for i in range(1,21):
    if i % 2== 0:
        continue
    print(i)
    
    
    

#Write a program to print characters in a string except for vowels.


text = input("Enter a string: ")
vowels = "aeiouAEIOU"

for i in text:
    if i in vowels:
        continue  
    print(i, end="")  


#Write a program to calculate the sum of numbers from 1 to 10, skipping multiples of 3.

total = 0

for num in range(1, 11):
    if num % 3 == 0:
        continue  
    total += num


print("The sum is:", total)



#Write a program to print multiplication table of 6, skipping multiples of 12.

for i in range(1, 11):
    a = 6 * i
    if a % 12 == 0:
        continue  
    print(f"6 x {i} = {a}")