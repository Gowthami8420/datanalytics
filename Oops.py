class Dog:
    sound="bark"
    
dog1=Dog()#Dog dog1=new Dog() in java object creation
print(dog1.sound)





class Dog:
    species="Canine"#Class attribute
    def __init__(self,name,age):#Creating a constructor and self is same class 
        self.name=name#instance attribute
        self.age=age
dog1=Dog("Buddy",3)
print(dog1.name)
print(dog1.species)



class Dog:
    def __init__(self,name,age):#constructor
        self.name=name
        self.age=age
    def __str__(self):#toString
        return f"{self.name} is {self.age}years old."#Directly add the variables and expressions directly 
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",2)
print(dog1)
print(dog2)
        

class Dog:
    species="Canine"#Class Vaariables
    def __init__(self,name,age):
        self.name=name
        self.age=age
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",2)

print(dog1.species)
print(dog2.name)

dog1.name="Max"
print(dog1.name)

dog1.species="Bochu"
print(dog1.species)


print("------------------Iterator---------------")
num=[1,2,3,4,5]
iter_num=iter(num)
print(next(iter_num))
print(next(iter_num))


def myfun():
    a=300
    print(a)
myfun()

#Enclosing Scope
def myfun():
    x=300
    def myinnerfun():
        print(x)
    myinnerfun()
myfun()




#Global Scope
x=300
def myfun():
    print(x)
myfun()
print(x)


