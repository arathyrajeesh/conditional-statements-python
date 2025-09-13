#Design a Password Strength Checker that evaluates a given password.


import re
def password_checker(password):
    
    if not password:
        print('you must enter a password')
        
    length=0
    error=[]
    
    if len(password)>=5:
        length +=1
    else:
        error.append("Password must be at least 8 characters")
        
    if re.search(r"[A-Z]",password):
        length+=1
    else:
        error.append("Add at least one uppercase letter.")
        
    if re.search(r"[a-z]",password):
        length+=1
    else:
        error.append("Add at least one lowercase letter.")
        
    if re.search(r"\d", password):
        length += 1
    else:
        error.append("Add at least one digit.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        length += 1
    else:
        error.append("Add at least one special character.")
    
    if length == 5:
        return " Strong Password!"
    elif length >= 3:
        return " Medium Strength Password. Suggestions: " + ", ".join(error)
    else:
        return " Weak Password. Suggestions: " + ", ".join(error)


a = input("Enter a password: ")
print(password_checker(a))




import re
def passwordCheck(inputPassword):    
    length_check = len(inputPassword) >= 8
    character = re.search(r"[.?!@&]", inputPassword) is not None
    uppercase = re.search(r"[A-Z]", inputPassword) is not None
    lowercase = re.search(r"[a-z]", inputPassword) is not None
    number = re.search(r"[0-9]", inputPassword) is not None    
    if length_check and character and uppercase and lowercase and number:
        print(" Strong password")
    else:
        print(" Weak password")
password =input('enter a password:')
passwordCheck(password)
