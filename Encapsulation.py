class private:
    def __init__(self):
        self.__salary=50000#private attribute double underscore __
    def salary(self):
        return self.__salary#Access through public method
obj=private()
print(obj.salary())#works
# print(obj.__salary)#Raises attribute error
