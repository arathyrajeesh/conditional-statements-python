#Write a program to find the largest and smallest number in a list.

a = [45,78,209,89,5,67]
small = a[0]
large= a[0]

for i in a[0:]:  
    if i < small:
        small = i
    if i > large:
        large = i

print(f"The smallest number is: {small}")
print(f"The largest number is: {large}")



#Write a program to remove duplicates from a list.

fruits=['apple','orange','banana','apple','grapes','orange']
print(fruits)
fruit=list(set(fruits))
print(f'after remove duplicates:{fruit}')


fruits=['apple','orange','banana','apple','grapes','orange']
fruit=[]

for i in fruits:
    if i not in fruit:
        fruit.append(i)
print(fruit)


#Write a program to reverse a list without using built-in functions. 

a = [1, 2, 3, 4, 5]

rev = a[::-1]

print(rev)


#Write a program to count how many times each element occurs in a list.

order = ['apple', 'orange', 'banana', 'apple', 'grapes', 'orange']

count = []   

for item in order:
    if item not in count:
        count.append(item)

for fruit in count:
    print(f"{fruit}: {order.count(fruit)}")



#Write a program to separate odd and even numbers from a list.

num = [1,2,3,4,5,6,7,8,9,10]

odd = []
even = []
for i in num [0:]:  
    if i % 2 == 0:
        even.append(i)
    if i % 2 != 0:
        odd.append(i)
        
print(f"The odd number is: {odd}")
print(f"The even number is: {even}")