"""
Que:6 
Write a Python program to create a file of strings by taking input from the user and then create
a dictionary containing each string along with their frequencies. (e.g. if the file contains ‘apple’,
‘banana’, ‘fig’, ‘apple’, ‘fig’, ‘banana’, ‘grapes’, ‘fig’, ‘grapes’, ‘apple’ then the output should
be {'apple': 3, 'banana': 2, 'fig': 3, 'grapes': 2}. 
"""
file = "fruitRecords.txt"
fruitDict = {}
try:
    f1 = open(file,"+w")
    while True:
        fruitName = input("Enter a Fruit name [Type 'End' for exit]: ")
        if fruitName.lower() == "end":
            print("Data are store in file",f1.name,"successfully")
            f1.close()
            break
        f1.write(f"{fruitName}\n")
    f1 = open(file,"r")
    for data in f1:
        data = data.split()
        if data[0].lower() not in fruitDict.keys():
            fruitDict[data[0].lower()] = 1
        else:
            fruitDict[data[0].lower()] += 1
    print("Dictionary is",fruitDict)
except OSError:
    print("Failed to open a file")