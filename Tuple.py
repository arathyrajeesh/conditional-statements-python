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

