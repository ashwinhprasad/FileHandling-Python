# reading the entire file
print("_____________________________________________")
print("//Reading the entire file\n")
file = open("file1.txt","r")
fileContent = file.read()
print(fileContent)
file.close()

#reading a line from the file
print("\n_____________________________________________")
print("//reading the first line from the file\n")
file = open("file1.txt","r")
print(file.readline())
file.close()

#read the first 2 lines from the file
print("_____________________________________________")
print("//Reading the first 2 lines from the file\n")
file = open("file1.txt","r")
print(file.readline())
print(file.readline())
file.close()

#readlines
print("_____________________________________________")
print("readlines function")
file = open("file1.txt","r")
print(file.readlines())
file.close()

#read a file and print the number of words in each line
print("_____________________________________________")
print("  Number of words at each line")
file = open("file1.txt","r")
i = 0
for line in file.readlines():
    print("Number of words in line ",i+1," = ",len(line.split(' ')))
    i += 1
file.close()



