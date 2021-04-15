"""
Que:5
Write a Python program to create a file containing student records where each record contain 
rollno and marks in 3 subjects separated by a comma (marks to be considered as list of 3 values). 
e.g. records of students: 1, [45, 40, 35], 2, [41, 38, 39], 3, [35, 30, 37] (each line of the file 
containing record of only 1 student). Prepare mark list in the following format: 
Roll No.    Mark-1      Mark-2      Mark-3      Total 
  1          45          40          35          120 
"""
import json
file = "studentRecord.txt"
try:
    f1 = open(file,"+w")
    while True:
        try:
            number = int(input("Enter student roll number: "))
            # if number.lower() == "end":
            #     break
            marksList =  []
            for i in range(0,3):
                marksList.append(int(input(f"Enter {i+1} Subject Marks: ")))
            fileInputedData = f'{number}, {marksList}'
            f1.write(f"{fileInputedData}\n")
            checkTurmination = input("Do you want to add another record? (Y/N): ")
            if checkTurmination.lower() == "n":
                print(f"Data successfully added on the file {f1.name}")
                f1.close()
                break
        except ValueError:
            print("Please insert valid input")
    print("-"*30,"Data from the file","-"*30)
    f1 = open(file,"r") 
    print("%15s %15s %15s %15s %15s"%("Roll No.","Marks-1","Marks-2","Marks-3","Total"))
    # print(f1.readlines()[0][2:])
    i = 1
    no = ""
    for data in f1:
        i = 1
        no = ""
        marks = ""
        for char in data:
            if char == "," and i == 1:
                i += 1
                continue
            elif i == 1:
                no += char
            elif i == 2:

            # print(char,end="")
        print("No =>",no)
        # print(data.split(',')[0])
        # marks = data[2:-1]
        # # print(marks)
        # # marks = marks.strip('][').split(', ')
        # # marks = json.loads(marks)
        # print(data[0],"=>",marks)
        # print(data[0],type(marks))
        # print(data.split())

except IOError:
    print("Failed to creating a file")
