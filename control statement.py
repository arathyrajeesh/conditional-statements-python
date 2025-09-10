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