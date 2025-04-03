a=10
b=20
if a>b:
    print("a is greater then b")
elif b>a:
    print("b is greater then a")
else:
    print("Both are equal")
    
    
    
i=1
if i!=0:
    if i>0:
        print("Positive Number")
    else:
        print("Negitive number")
else:
    print("i is zero")
    




print("****************************************************************")
# marks=int(input("Enter the marks : "))
# if marks>90 and marks<=100:
#     print("A grade")
# elif marks>80 and marks<=90:
#     print("B grade")
# elif marks>70 and marks<=60:
#     print("C grade")
# elif marks<60:
#     print("fail")



n=5
while n>0:
    n-=1
    print(n)


n=5
while n>0:
    n-=1
    if n==2:
        break
    print(n)
print("Loop ended ")


n=6
while n>0:
    n-=1
    if n==2:
        continue
    print(n)
print("Ended")

n=1,2,3,4,5,6
for x in n:
    print(x)
    
x=[1,2]
y=[4,5]
for i in x:
    for j in y:
        print(i,j)
        
        
        
        
        
state_dict={1:"Gowthami",2:"suma",3:"sri",4:"hii"}
for i in state_dict.keys():
    print(i)
    
    
    
    
def great():
    print("Hii how are you")
great()


def great(name):
    print(name)
great("Gowthami")


def add(a,b):
    return a+b
res=add(2,3)
print(res)



def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Bob")


#To return two return values
def get_details():
    name="Gowthami"
    age=22
    return name,age
n,a=get_details()
print("Name:",n,"Age :",a)


#n number of arguments
def add_all(*num):
    return sum(num)#sum is a predefined funtion
res=add_all(1,2,3,4,5,6)
print(res)

#Function with keyword arguments
def info(**details):
    for key,value in details.items():
        print(key,":",value)
info(name="Gowthami",age=22,city="hyd")



# print("----------------------prime number-------------------")
# num=int(input("Enter a number : "))
# count=0
# for i in range(2,num):
#     if num%i==0 and num!=0:
#         count+=1
# if count==0:
#     print("Prime number")
# else:
#     print("Composite number")
    
    
    
import array
fruits=array.array("u","applebananacherry")#Type error---For characters string we have to use 'u'
print(fruits[1])



num=array.array('i',[1,2,3,4,5])#In case of interger we have to use 'i'
length=len(num)
num_sort=sorted(num)
print(length)
print(num_sort)


# print("----------------------Fibnocci Series---------------")
# n=int(input("Enter a number "))
# a=0
# b=1
# for i in range(n):
#     print(a ,end=" ")
#     a,b= b,a + b 
    
    
    
# print("------------------------Palindrome-------------------")
# s=input("Enter a string")
# rev=s[::-1]
# if rev==s:
#     print("Palindrome")
# else:
#     print("Not palindrome")
    
    
# print("======================Even or Odd===========================")
# num=int(input("Enter a number"))
# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd number")






# print("--------------------prime number from user---------------")
# n=int(input("Enter a number"))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count+=1
# if count==0:
#     print("Prime number")
# else:
#     print("Not a prime number")
    
    
# print("-------------------------even number change to '@'-------------------------")  
# for i in range(1,100):
#     if i%2==0:
#         print("@")
#         continue
#     print(i)


# print("***************************************************")
# # a=[1,2,3,4,5]
# a=list(map(int,input("Enter a collection").split(" ")))
# for i in a:
#     sq=i*i
#     print(sq)


# print("---------------------- key display the value----------------------------")
# # a={1:"Gowthami",2:"Hiii",3:"Bye"}

# n=int(input("Enter the  key-value pairs"))
# a={}
# for i in range(n):
#     key=input("Enter the key ")
#     value=input("Enter the value")
#     a[key]=value
# for i in a.values():
#     print(i)









# print("---------------------By Using Two Functions-------------------------")
# def get_data():
#     name=input("Enter your name :")
#     age=input("Enter your age :")
#     city=input("Enter your city :")
#     return name,age,city
# def display_data():
#     name,age,city=get_data()
#     print("Name :",name)
#     print("Age:",age)
#     print("city:",city)
# display_data()





print("************************List Functions***************************")
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
# Append
numbers.append(100)
print("After append(100):", numbers)
# Extend
numbers.extend([200, 300])
print("After extend([200, 300]):", numbers)
# Insert
numbers.insert(2, 50)
print("After insert(2, 50):", numbers)
# Remove
numbers.remove(100)  # Removes the first occurrence of 100
print("After remove(100):", numbers)
# Pop
popped_value = numbers.pop()  # Removes the last element
print(f"After pop(): {numbers}, Popped Value: {popped_value}")
# Index
print("Index of 50:", numbers.index(50))
# Count
print("Count of 200:", numbers.count(200))
# Reverse
numbers.reverse()
print("After reverse():", numbers)
# Sort
numbers.sort()
print("After sort():", numbers)
# Copy
new_list = numbers.copy()
print("Copied List:", new_list)
# Clear
numbers.clear()
print("After clear():", numbers)





















# print("*****************Tuple Functions**********************************")

# numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))


# value_to_count = int(input("Enter a number to count its occurrences: "))
# print(f"Count of {value_to_count}: {numbers.count(value_to_count)}")

# value_to_find = int(input("Enter a number to find its index: "))
# print(f"Index of {value_to_find}: {numbers.index(value_to_find)}")
