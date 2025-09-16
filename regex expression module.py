import re

text = "My age is 20"
result = re.search(r"\d+",text)
if result:
    print("Number found:",
result.group())