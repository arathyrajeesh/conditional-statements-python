
#Write a function to find the grade of a student from marks.

def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

marks = int(input("Enter marks: "))
print("Grade:", grade(marks))