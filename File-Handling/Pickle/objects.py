import pickle

class student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    
    def print(self):
        print(f'The student name is : {self.name}')
        print(f'The mark is : {self.mark}')


while(1):
    print("1.write")
    print("2.read")
    print("3.exit")
    ch = int(input("enter your choice : "))

    if ch == 1:
        name = input("Enter the name of the student: ")
        mark = int(input("Enter the mark  : "))
        studObj = student(name,mark)
        try:
            studList = pickle.load(open("objects.bin","rb"))
        except FileNotFoundError:
            studList = []
        studList.append(studObj)
        pickle.dump(studList,open("objects.bin","wb"))
    
    elif ch == 2:
        studList = pickle.load(open("objects.bin","rb"))
        for studObj in studList:
            studObj.print()
            print("")
    else:
        break