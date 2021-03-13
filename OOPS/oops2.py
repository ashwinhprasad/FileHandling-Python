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
    ch = int(input("1.Add\n2.Display\n3.Delete\n4.exit\nEnter Your Choice: "))
    if ch == 1:
        is_teacher = input("Is this a teacher ? : ")
        if is_teacher=="yes":
            name = input("Enter Name of the Teacher: ")
            age = int(input("Enter age of the Teacher: "))
            subject = input("Enter the subject of the Teacher: ")
            degree = input("Enter the  Degree of the Teacher: ")
            t = Teacher(name,age,subject,degree)
            people.append(t)
        else:
            name = input("Enter Name of the Student: ")
            age = int(input("Enter age of the Student: "))
            dept = input("Enter the department of the Student: ")
            section = input("Enter the section of the student: ")
            s = Student(name,age,dept,section)
            people.append(s)
    elif ch == 2:
        for person in people:
            person.getter()
    elif ch==3:
        usr = int(input("Enter the index of the person you need to delete: "))
        people[usr].getter()
        people.pop(usr)
        print("Person Deleted from the database")
    elif ch == 4:
        print("Terminating")
        exit()
    else:
        print("Enter Valid Option")
