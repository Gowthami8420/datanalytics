#Encapsulation Using Public Modifier
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name",self.name)
        print("Age",self.age)
        
s=student("Gowthami",22)#object creation

print("Name",s.name)#Accessing public variables directly
print("Age",s.age)

s.name="Gayathri"#Modify the variables
s.age=21
s.display()



#Encapsulation using protected modifier
class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary#protected modifier with single underscore
    def display(self):
        print("Name:",self.name)
        print("Salary:",self._salary)
        
e=employee("Gowthami",40000)#object creation
#Accessing directly
print(e.name)
print(e._salary)
#modifying
e._salary=50000
e.display()


#Encapsulation using private modifier
class Bank:
    def __init__(self,name,bal):
        self.name=name
        self.__bal=bal#private variable with double underscore__
    def display(self):
        print("Name:",self.name)
        print("Balance:",self.__bal)
        return self.__bal
b=Bank("gowthami",30000)
print(b.name)#Access Directly
# print(b.__bal)#cannot access
b.__bal=50000
print(b.display())