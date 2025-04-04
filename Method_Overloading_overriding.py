#Method overloading
class calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c
    
cal=calculator()
print(cal.add())
print(cal.add(10))
print(cal.add(10,20))
print(cal.add(10,20,30))


#Method overriding
class Animal:
    def sound(self):
        print("Animal sounds")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
d=Dog()
d.sound()


#Polymorphism
print(len("hello"))
print(len([1,2,3,4]))
print(len({1:'a',2:'b',3:'c'}))