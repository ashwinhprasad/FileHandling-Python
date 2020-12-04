#opening a file - method 1
file = open("file1.txt","w")
userInput = input("Enter something : ")
file.write(userInput)
file.close()

#opeing a file - method 2
with open("file1.txt",'w') as file:
    file.write("hey there\n")


#appending to a file - 1
file = open("file1.txt","a")
string = "This is the appended content\n"
file.write(string)
file.close()

#appending to a file - method 2
with open("file1.txt","a") as file:
    file.write("This is the appended content 2")
