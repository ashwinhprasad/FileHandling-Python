# Text File Handling

list of operations 
1. read
2. write
3. modify

### Mode of operations

modes of operation specify the reason to open the file. whether to write, read or append

- w - write
- a - append
- r - read
- r+ - read and write


## Write.py
- open() - function that takes file name and mode of operation as a paramter returns the file object
- write() - function that takes in a string and writes it on a file

## Read.py
- read() - returns all the content of the file as a string
- readline() - returns a line from the file as a string
- readlines() - returns each line from the file as an element of a list