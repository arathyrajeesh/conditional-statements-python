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
