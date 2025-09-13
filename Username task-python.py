#Make a Username Generator from first and last names.


import random

def username_generator(first_name, last_name):
    
    first_name = first_name.lower()
    last_name = last_name.lower()

    first_part = first_name[:3] 

    username = f"{first_part}{last_name}"

    username += str(random.randint(10, 99))
    
    username += random.choice(['@', '/', '$'])  

    return username

first = input('Enter first name: ')
last = input('Enter last name: ')

username = username_generator(first, last)
print(f" username for {first} {last}: {username}")
