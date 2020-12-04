# # reading the entire file
# print("_____________________________________________")
# print("//Reading the entire file\n")
# file = open("file1.txt","r")
# fileContent = file.read()
# print(fileContent)
# file.close()

# #reading a line from the file
# print("\n_____________________________________________")
# print("//reading the first line from the file\n")
# file = open("file1.txt","r")
# print(file.readline())
# file.close()

# #read the first 2 lines from the file
# print("_____________________________________________")
# print("//Reading the first 2 lines from the file\n")
# file = open("file1.txt","r")
# print(file.readline())
# print(file.readline())
# file.close()

# #readlines
# print("_____________________________________________")
# print("readlines function")
# file = open("file1.txt","r")
# print(file.readlines())
# file.close()

# #read a file and print the number of words in each line
# print("_____________________________________________")
# print("  Number of words at each line")
# file = open("file1.txt","r")
# i = 0
# for line in file.readlines():
#     print("Number of words in line ",i+1," = ",len(line.split(' ')))
#     i += 1
# file.close()


#read a file and add the word "end" at the end of each line of a file
print("_____________________________________________")
print("add 'End' at the end of each line")
file1 = open("file1.txt","r")
file2 = open("file2.txt","w")
for line in file1.readlines():
    line = line.split("\n")[0]
    file2.write(line+" END\n")
file1.close()
file2.close()
#copying file2 to file 1
file1 = open("file1.txt","w")
file2 = open("file2.txt","r")
file1.writelines(file2.readlines())
file1.close()
file2.close()
