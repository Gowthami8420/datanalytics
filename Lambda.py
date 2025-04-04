s1="Hello Good Morning"
s2=lambda func:func.upper()
print(s2(s1))


n=lambda x :"Positive " if x>0 else "Negitive" if x<0 else "Zero"
print(n(8))


sq=lambda x:x**2
print(sq(3))




li=[lambda arg=x:arg*10 for x in range(1,5)]
for i in li:
    print(i)#Not readable
    print(i())#Readability



#Even or Odd
checking=lambda x:"Even " if x%2==0 else "Odd"
print(checking(2))
print(checking(3))




#Cal with lambda
calc=lambda x,y:(x+y,x-y,x*y,x/y)
res=calc(3,4)
print(res)



n=[1,2,3,4,5,6]
even=filter(lambda x:x%2==0,n)
# print(even)#Not readable
print(list(even))




a=[1,2,3,4]
b=map(lambda x:x*2,a)
# b=lambda x:x*2,a   Map()  iterates thriugha a and applies the transformation(x*2)
print(list(b))


from functools import reduce
a=[1,2,3,4,5]
b=reduce(lambda x,y:x*y,a)#reduce() applies this operation across the list
print(b)




a="Revature"
b=22
msg="My name is {0} and i am {1} years old.".format(a,b)
print(msg)



a="Python"
print("The article is written in {}.".format(a))
print("Hii! My name is {} and i am {} years old".format("User",22))

#fstring
name="Om"
age=22
print(f"Hello,My name is{name} and I am {age}years old")#f before the string allows you to directly insert variables or expressions into the string.



#Inner Function

def fun1(msg):
    def fun2():
        print(msg)
    fun2()
fun1("Hello")



#Decorator
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper


@decorator #greet=decorator(greet)
def greet():
    print("Hello World")
greet()




#Function Signature
import inspect
print(inspect.signature(decorator))