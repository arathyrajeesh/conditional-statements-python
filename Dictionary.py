#Create a dictionary with 3 key-value pairs and print it.

mydict={
    "name" : "Arathy",
    "age" : "20",
}
print(mydict)


#Write a program to access the value of a given key in a dictionary.

mydict={
    "name" : "Arathy",
    "age" : "20",
}

print(mydict['name'])


#Add a new key-value pair to an existing dictionary.

mydict={
    "name" : "Arathy",
    "age" : "20",
}

mydict['place'] = 'Kannur'
print(mydict)


#Update the value of a specific key in a dictionary.

mydict={
    "name" : "Arathy",
    "age" : "20",
}
mydict['name'] = "Arathy tp"

print(mydict)


#Delete a key-value pair from a dictionary using del.
mydict={
    "name" : "Arathy",
    "age" : "20",
    "place" : "Kannur",
}
print("before deletion:" ,mydict)
del mydict ["place"]
print("after deletion:",mydict)


#Check if a key exists in a dictionary.
mydict={
    "name" : "Arathy",
    "age" : "20",
    "place" : "Kannur",
}

if "job" in mydict:
    print('name in ',mydict)
else:
    print("not in dictionary")


#Print all keys of a dictionary using a loop.

mydict={
    "name" : "Arathy",
    "age" : "20",
    "place" : "Kannur",
}

for i in mydict:
    print(i)
    
    
    
#Print all values of a dictionary using a loop.
mydict={
    "name" : "Arathy",
    "age" : "20",
    "place" : "Kannur",
}

for i in mydict:
    print(mydict[i])
    
    
    
#Write a program to find the length of a dictionary.

mydict={
    "name" : "Arathy",
    "age" : "20",
    "place" : "Kannur",
}
print(len(mydict))



#Clear all elements from a dictionary.

mydict={
    "name" : "Arathy",
    "age" : "20",
    "place" : "Kannur",
}
mydict.clear()
print(mydict)

