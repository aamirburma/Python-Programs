"""
Que:1 
Write a Python program to create a file of numbers by taking input from the user and then
display the content of the file. You can take input of non-zero numbers, with an appropriate
prompt, from the user until the user enters a zero to create the file assuming that the numbers
are non-zero.
"""
file = 'number.txt'
try:
    f = open(file, '+w')
    print("File is opening on write mode")
except OSError:
    print('Failed creating the file')
else:
    while True:
        number = input("Enter a Number [0 for Exit]: ")
        if number == "0":
            f.close()
            print("File is closed which was opened on write mode")
            break
        else:
            try:
                number = int(number)
                f.write(f"{number}\n")
            except:
                print("Please Input valid Number")
try:
    f = open(file, 'r')
    print("File is opening on read mode")
except OSError:
    print('Failed creating the file')
else:
    i = 1
    print('-'*10,'File Data','-'*10)
    for data in f:
        print(f"{i} => {data}")          
        i += 1
    f.close()
    print("File is closed which was opened on read mode")
