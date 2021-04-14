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
        #     #Here if data is staring then it will be execute on exception
        #     inputData = float(inputData)
        #     #check integer
        #     if int(inputData)/inputData == 1:
        #         print("Integer")
        #     elif inputData/int(inputData) > 1:
        #         print("float")
        # except ValueError:
        #     print("String")
except OSError:
    print("Failed to creating a file")