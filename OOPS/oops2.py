class Person():
    def __init__(self,name=None,age=None):
        self.__name = name
        self.__age = age
    def getter(self):
        print(f"Name: {self.__name}\nAge:{self.__age}")


class Student(Person):
    def __init__(self,name,age,dept=None,section=None):
        super().__init__(name,age)
        self.__dept = dept
        self.__section = section
    def getter(self):
        super(Student,self).getter()
        print(f"Dept:{self.__dept}\nSection:{self.__section}")


class Teacher(Person):
    def __init__(self,name,age,subject=None,degree=None):
        super().__init__(name,age)
        self.__subject = subject
        self.__degree = degree
    def getter(self):
        super(Teacher,self).getter()
        print(f"Subject:{self.__subject}\nDegree:{self.__degree}")

people = []
while(True):
    ch = int(input("1.Add\n2.Delete\n3.exit\nEnter Your Choice: "))
    if ch == 1:
        pass
    elif ch == 2:
        pass
    elif ch == 3:
        print("Terminating")
        exit()
    else:
        print("Enter Valid Option")
