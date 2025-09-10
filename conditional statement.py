#Check Even or Odd

a=10
if a%2==0:
    print(a ,"is even number")
else:
    print(a ,"is odd number")
    
    
#Positive, Negative, or Zero 

a=-4
if a>0:
    print(a,"is positive number")
elif a<0:
    print(a,"is negative number")
else:
    print(a)


#Find the Largest of Two Numbers

a=8
b=10
if a<b:
    print(a,'is less than',b)
else:
    print(a,"is greater than",b)
    
    
    
#Find the Largest of Three Numbers 

a=10
b=5
c=18

if a>=b and a>=c:
    print(f'{a}')
elif b>=a and b>=c:
    print(f'{b}')
else:
    print(f'{c}')
    
    


#Grade Calculation

a=int(input('enter mark'))
if(a >= 100) :
    print("Grade A")
elif(a >= 75) :
    print("Grade B")
elif(a >= 50) :
    print("Grade c")
else:
    print("Fail")
    
    
    
#Leap Year Check

a=int(input('enter a year'))

if (a%4==0) and (a%100!=0) or (a%400==0):
    print(f'{a} is leap year')
else:
    print('not leap year')
    
    
    
    
#Voting Eligibility

a=int(input('enter your age'))

if(a>=18):
    print('eligible for vote')
else:
    print('not eligible for vote')



#Check Vowel or Consonant

vowel=['a','e','i','o','u']

word=str(input('enter a character:'))

if word in vowel:
    print('vowels are here')
else:
    print('consonant')




#Simple Calculator 

a=int(input('enter first num:'))
b=int(input('enter second num:'))
c=input("enter operator '+','-','*','/': ")

if c=='+':
    print(f'value is :{a+b}')
elif c=='-':
    print(f'value is :{a-b}')
elif c=='/':
    print(f'value is :{a/b}')
elif c=='*':
    print(f'value is :{a*b}')
else:
    print('invalid operator')
    
    
    
# Traffic Light System

signal = input("Enter the traffic signal (Red/Yellow/Green): ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")

