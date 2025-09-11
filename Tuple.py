#Write a program to find the maximum and minimum values in a tuple.

num=(30,25,3,94,5,46,67)

max= num[0]
min = num[0]

for num in num:
    if num > max:
        max = num
    if num < min:
        min = num

print("Maximum value:", max)
print("Minimum value:", min)



#Write a program to check if a given element exists in a tuple.

numbers = (10, 20, 30, 40, 50)

a = int(input("Enter a number to search: "))

if a in numbers:
    print(f"{a} exists ")
else:
    print(f"{a} does not exist")



#Write a program to count the number of times a specific value occurs in a tuple.

numbers = (10, 20, 30, 20, 40, 20, 50, 50, 50, 50)

a = int(input("Enter a number to count: "))

count = 0
for i in numbers:
    if i == a:
        count += 1

print(f"{a} occurs {count} times")



#Write a program to concatenate two tuples and print the result.

a = ('hello ')
b = ('world')
c = a + b
print(c)


#Write a program to slice a tuple and display only alternate elements.

numbers = (10, 20, 30, 40, 50, 60, 70)

a = numbers[::2]

print("Original tuple:", numbers)
print( a)
