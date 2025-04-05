#Validate password
import re
# from Day4.Exception_handling import NotEligible
# def val_password(password):
#     if len(password)<8:
#         return "password must be at least 8 characters long"
#     if not re.search(r"[A-Z]",password):
#         return "password must contain at least one uppercase letter"
#     if not re.search(r"[a-z]",password):
#         return "password must contain at least one lowercase letter"
#     if not re.search(r"[0-9]",password):
#         return "password must contain at least one digit"
#     if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/\\|`~]",password):
#         return "password must contain at least one special character"
#     return "password is valid!"
# password=input("Enter your password")
# res=val_password(password)
# print(res)
    
    
    
    
    
#Validate url
# def validate_url(url):
#     pattern=re.compile(r'^(https?://)?'             # Optional http or https
#         r'(www\.)?'                  # Optional www.
#         r'[a-zA-Z0-9.-]+'            # Domain name
#         r'\.[a-zA-Z]{2,}'            # Top-level domain
#         r'(/[\w./?%&=-]*)?$'         # Optional path/query
# ) 
#     if pattern.fullmatch(url):
#         return "valid url"
#     else:
#         return "invalid url"
# url=input("Enter a url:")
# print(validate_url(url))


#implement all the errors using exception handling
class NotEligible(Exception):
    pass

#1.ZeroDivisionError
try:
    a=10/0
except ZeroDivisionError as e:
    print("Zero Division Error",e)
    
#2.ValueError
try:
    n=int("abc")
except ValueError as e:
    print("value error :",e)
#3.indexerror
try:
    lst = [1, 2, 3]
    print(lst[5])  # Invalid index
except IndexError as e:
    print("IndexError:", e)
# 4. KeyError
try:
    d = {'name': 'Alice'}
    print(d['age'])  # Key doesn't exist
except KeyError as e:
    print("KeyError:", e)

# 5. TypeError
try:
    res = "abc" + 5  # Wrong type
except TypeError as e:
    print("TypeError:", e)

# 6. FileNotFoundError
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError:", e)

# 7. Custom Exception (NotEligible)
def checkage(age):
    if age < 18:
        raise NotEligible("Age must be 18 or above.")
    else:
        print("You are eligible!")

try:
    checkage(16)
except NotEligible as e:
    print("Custom NotEligible Exception:", e)