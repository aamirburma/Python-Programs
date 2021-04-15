"""
Que:7
Write a Python program to create a text file of multiple lines. Take input of a word from the
user and then display all the lines from the file containing this word along with the frequency of
the word in that line. 
"""
file = "myFile.text"
try:
    flag = 0
    f1 = open(file,"+w")
    while True:
        statement = input("Enter a Line :")
        f1.write(f"{statement}\n")
        while True:
            choice = input("Do you want add new line (Y/N): ")
            if choice.lower() == "y":
                break;
            elif choice.lower() == 'n':
                flag = 1
                break
            print("Please select valid choice")
        if flag == 1:
            print("Data added on file '",f1.name,"' seccessfully")
            break
    f1.seek(0,0)
    specialCharacters = "@.,'\""
    i = 1
    for data in f1:
        lineDictinory = {}
        data = data.split()
        for lineData in data:
            #Remove Special Characters from the String
            for characters in specialCharacters:
                lineData = lineData.replace(characters,'')
            #Check Words availibility and count numbers of repetations
            if lineData.lower() not in lineDictinory.keys():
                lineDictinory[lineData.lower()] = 1
            else:
                lineDictinory[lineData.lower()] += 1
        print("-"*15,f"Line : {i}","-"*15)
        for words in lineDictinory:
            print(words,"=>",lineDictinory[words],end=" ")
        print()
        i += 1
    f1.close()
except OSError:
    print("Failed to open a file")