import json

student = {
    "ashwin":70,
    "charann":80,
    "surendhar":90,
    "kavin":100
}


# writing into json file
file = open("file.json","w")
json.dump(student,file)
file.close()

#writing json into text file
file = open("file.txt","w")
y = json.dumps(student)
file.write(y)
file.close()