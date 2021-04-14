"""
Que:3
Write a Python program to create a file of numbers by taking input from the user. Split this file 
into two files where one file contains odd numbers and the other file contains even numbers 
from the file. You can take input of non-zero numbers, with an appropriate prompt, from the 
user until the user enters a zero to create the file assuming that the numbers are non-zero.
"""
file = "mainFile.txt"
try:
    f = open(file,"+r")
    while True:
        try:
            number = int(input("Enter a number [0 - Exit]: "))            
            if number == 0:
                print(f.name,"is closed successfully")
                f.close()
                break
            f.write(f"{number}\n")
        except:
            print("Please input number only")
    f1 = open(file,'r')
    f2 = open("odd.txt",'+w')
    f3 = open("even.txt",'+w')
    for data in f1:
        data = int(data)
        if data % 2 == 0:
            f3.write(f"{data}\n")
        else:
            f2.write(f"{data}\n")
    f1.close()
    f2.close()
    f3.close()
    f1 = open(file,'r')
    f2 = open("odd.txt",'r')
    f3 = open("even.txt",'r')
    print("-"*10,"Main File '",f1.name,"'","-"*10)
    for data in f1:
        print(data)
    f1.close()
    print("-"*10,"Odd File '",f2.name,"'","-"*10)
    for data in f2:
        print(data)
    f2.close()
    print("-"*10,"Even File '",f3.name,"'","-"*10)
    for data in f3:
        print(data)
    f3.close()
except OSError:
    print("Failed to creating a file")
