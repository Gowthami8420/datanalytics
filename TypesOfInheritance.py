#Single Inheritance
class Animal:
    def speak(self):
        print("Animal can speak")
class Dog(Animal):
    def bark(self):
        print("Dog bark")
d1=Dog()
d1.speak()
d1.bark()


#Multiple Inheritance
class Father:
    def skills(self):
        print("Working")
class mother:
    def skills(self):
        print("cooking")
class child(Father,mother):
    def own_skills(self):
        print("Programming")
c1=child()
c1.skills()
c1.own_skills()


#Multi level inheritance
class grandfather:
    def house(self):
        print("House")
class father:
    def car(self):
        print("car")
class son(grandfather,father):
    def bike(self):
        print("bike")
s=son()
s.house()
s.car()
s.bike()


#Hierarchical inheritance
class parent:
    def show(self):
        print("parent properities")
class child1(parent):
    def show1(self):
        print("child1 properties")
class child2(parent):
    def show2(self):
        print("child2 properties")
        
c1=child1()
c2=child2()
c1.show()
c1.show1()
c2.show()
c2.show2()


#Hybrid inheritance
class person:
    def per_info(self):
        print("Name:Gowthami")
class student(person):
    def stu_info(self):
        print("Btech")
class employee(person):
    def emp_info(self):
        print("training")
class parttime(student,employee):
    def part_time_info(self):
        print("part time employee")
        
p=parttime()
p.per_info()
p.stu_info()
p.emp_info()
p.part_time_info()