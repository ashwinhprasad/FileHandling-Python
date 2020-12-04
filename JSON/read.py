import json

#dictionary
file = open("file.json","r")
students = json.load(file)
print(students,type(students))
file.close()


student = "{ \"mark\" : \"500\" }"
studentMark = json.loads(student)
print(studentMark,type(studentMark))
