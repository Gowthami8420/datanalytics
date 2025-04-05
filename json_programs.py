import functools
import json#json to python
x='{"name":"Gowthami","age":22}'#json
z=json.loads(x)
print(z["name"])
print(z["age"])




#Dictionary to JSON format
x={"name":"Gowthami","age":22}
y=json.dumps(x)
print(y)#json format



#Regex
import re
x="The rain chennai"        #^ starting .*every thing in between $ending
y=re.search("^The.*chennai$",x)
if y:
    print("Yes The match is correct")
else:
    print("Not matching with the pattern")
    
    
x="The rain in chennai"
y=re.findall("ai",x)
print(y)

z=re.search("\s",x)#/s means whitespace
print(z)
z=re.split("\s",x)#/s means splitted withe the white space
print(z)

#Replace all white space with $
z=re.sub("\s","$",x)
print(z)



pattern=r"\d+"  #This pattern matches one or more digits
text="There are 123 apples"
match=re.search(pattern,text)
if match:
    print("Match found:",match.group())
    
pattern=r"(\d+)-(\d+)-(\d+)"
text="The event is on 2025-03-26"
match=re.search(pattern,text)
if match:
    print("year:",match.group(1))
    print("Month-Day:",match.group(2))
    print("Date:",match.group(3))
    
    
    
# email=r"[a-zA-Z0-9._%+-]    +@[a-zA-Z0-9.-]     +\.[a-zA-Z]{2,}"
# text="please contact us at remya@revature.com"
# match=re.search(email,text)
# if match:
#     print("Email found :",match.group())
# else:
#     print("Not match")
    
    
    
import re

email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text = "please contact us at remya@revature.com"
match = re.search(email, text)

if match:
    print("Email found:", match.group())
else:
    print("Not match")

    
    
    
    
