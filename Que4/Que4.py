"""
Que:4
Write a Python program to create a file of elements of any data type (mixed data type, i.e. some 
elements maybe of type int, some elements of type float and some elements of type string). Split 
this file into three file containing elements of same data type (i.e. 1st file of integers only, 2nd
file of float only and 3rd file of strings only). Take input from the user to create the file. 
"""
file1 = "mainFile.txt"
file2 = "integerFile.txt"
file3 = "floatFile.txt"
file4 = "stringFile.txt"
try:
    f1 = open(file1,"+w")
    while True:
        # try:
        inputData = input("Enter data [Type 'End' for exit]:")
        if inputData.lower() == "end":
            print("Input process terminate successfully")
            f1.close()
            break
        f1.write(f"{inputData}\n")
    f1 = open(file1,"r")
    f2 = open(file2,"+w")
    f3 = open(file3,"+w")
    f4 = open(file4,"+w")
    for data in f1:
        try:
            #Here if data is staring then it will be execute on exception
            data = float(data)
            #check integer
            if int(data)/data == 1 or int(data) == 0:
                # print("Integer")
                f2.write(f"{int(data)}\n")
            elif data/int(data) > 1:
                f3.write(f"{data}\n")
                # print("float")
        except ValueError:
            f4.write(f"{data}")
            # print("String")
    f1.close()
    f2.close()
    f3.close()
    f4.close()
except OSError:
    print("Failed to creating a file")