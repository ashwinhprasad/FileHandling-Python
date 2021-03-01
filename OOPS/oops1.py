class student:
    def __init__(self,name=None,age=None,section=None,dept=None):
        self.__name = name
        self.__age = age
        self.__section = section
        self.__dept = dept 
    
    def setter(self,name,age,section,dept):
        self.__name = name
        self.__age = age
        self.__section = section
        self.__dept = dept

    def getter(self):
        print(f"{self.__name}, who is {self.__age} years old is studying in {self.__dept}-{self.__section}")

s1 = student()
s1.setter("Ashwin",18,'A','CSBS')
s1.getter()