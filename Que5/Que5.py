"""
Que:5
Write a Python program to create a file containing student records where each record contain 
rollno and marks in 3 subjects separated by a comma (marks to be considered as list of 3 values). 
e.g. records of students: 1, [45, 40, 35], 2, [41, 38, 39], 3, [35, 30, 37] (each line of the file 
containing record of only 1 student). Prepare mark list in the following format: 
Roll No.    Mark-1      Mark-2      Mark-3      Total 
  1          45          40          35          120 
"""
file = "studentRecord.txt"
try:
    f1 = open(file,"+w")
    while True:
        try:
            number = int(input("Enter student roll number: "))
            marksList =  []
            for i in range(0,3):
                marksList.append(float(input(f"Enter {i+1} Subject Marks: ")))
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
    for data in f1.readlines():
        rollNo = data.split(',',1)[0]
        list = data.split(',',1)[1]
        marks = (list.split('[', 1)[1].split(']')[0]).split(',')
        print("%15s %15.2f %15.2f %15.2f %15.2f"%(rollNo,float(marks[0]),float(marks[1]),float(marks[2]),(float(marks[0])+float(marks[1])+float(marks[2]))))
except IOError:
    print("Failed to creating a file")
