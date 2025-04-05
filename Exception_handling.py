# from Day4.Exception_handling import checkage

try:
    x=10/0
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("Completed execution")
    
    
    
    
    
    
# try:
#     num=int(input("Enter a number"))
#     res=10/num
# except ValueError as e:
#     print(f"Invalid Input:{e}")
# except ZeroDivisionError as e:
#     print("Cannot divided by zero")
# except Exception as e:
#     print("An unexcepted")
# else:
#     print(f"Result:{res}")
# finally:
#     print("code execued successfully")   
    
    
    
    
    
# def checkage(age):
#     if age<18:
#         raise ValueError("Age must be 18")
#     else:
#         print("You are eligible")
        
# try:
#     checkage(16)
# except ValueError as e:
#     print(f"Error")
    
    
    
    
    
#User defined execption
class NotEligible(Exception):
    pass
def checkage(age):
    if age<18:
        raise NotEligible("Age must be 18")
    else:
        print("You are eligible")
    
try:
    checkage(16)
    
except NotEligible as e:
    print(f"Error")
    print(e)