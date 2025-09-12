#Write a program to add multiple elements into a set.

a={1,2,3}
a.update([4,5,6])
print(a)



#Write a program to remove an element from a set if it is present.

a={1,2,3,4,5,6,7,8}
print("current set :",a)
b=int(input('enter a number wants to remove:'))

a.remove(b)
print(f"after remove item :{a}")



#Write a program to find the union, intersection, and difference of two sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"set1:{set1} set2:{set2}")
union = set1.union(set2)
print(f"after union:{union}")

#intersection

intersection_set = set1.intersection(set2)
print(f"after intersection:{intersection_set}")


#difference 

diff = set1.difference(set2)
print(f"difference:{diff}")



#Write a program to check if one set is a subset of another.

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check set1 is a subset of set2
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is NOT a subset of set2")

# Check set2 is a subset of set1
if set2.issubset(set1):
    print("set2 is a subset of set1")
else:
    print("set2 is NOT a subset of set1")



#Write a program to find all elements that are present in exactly one of the two sets.

set = {1,3,5,6}
set1 = {2,3,4,5,6,7}
c = set.difference(set1)
d = set1.difference(set)
print(f"set1: {set}")
print(f"set2: {set1}")
e = c.union(d)
print(f"common elements of 2 set :{e}")