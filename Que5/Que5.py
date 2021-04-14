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
except IOError:
    print("Failed to creating a file")