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