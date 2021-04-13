"""
Que: 2
Write a Python program to create a text file of multiple lines. Display the following: 
1. Entire text file 
2. 1st n lines of the text tile. 
3. m lines starting from the nth line 
4. number of words in each line 
"""
file = "myFile.txt"
try:
    f = open(file,'w')
    text = "Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.\
        \nIt is used for:\
        \nweb development (server-side),\
        \nsoftware development,\
        \nmathematics,\
        \nsystem scripting.\
        \nWhat can Python do?\
        \nPython can be used on a server to create web applications.\
        \nPython can be used alongside software to create workflows.\
        \nPython can connect to database systems. It can also read and modify files.\
        \nPython can be used to handle big data and perform complex mathematics.\
        \nPython can be used for rapid prototyping, or for production-ready software development."
    f.write(text)
    f.close()
    f = open(file,"r")
except OSError:
    print("File to creating a file")
else:
    while True:
        print("1.  Entire text file ")
        print("2.  1st n lines of the text file ")
        print("3.  m lines starting from the nth line  ")
        print("4.  number of words in each line  ")
        print("5.  Exit  ")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print('-'*10,'Entire File','-'*10)
                #Set File pointer at begning of file
                f.seek(0,0)
                for data in f:
                    print(data)
            elif choice == 2:
                f.seek(0,0)
                print("First line of file : ",f.readline())
            elif choice == 3:
                n = int(input("Staring line numbers: "))
                m = int(input("How many lines you want to retrieve: "))
                f.seek(0,0)
                for data in f.readlines()[n-1:m+1]:
                    print(data)
            elif choice == 4:
                data = f.read()
                words = data.split()
                print(f"Total numbers of words in file : {len(words)}")
            elif choice == 5:
                print("Thank you for performing task")
                break
            else:
                print("Invali input! Please input valid choice")
        except:
            print("Invalid input! Please select number only")
